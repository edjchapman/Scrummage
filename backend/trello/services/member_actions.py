import csv
import os

from django.utils import timezone as tz

from trello.utils.trello_api import get_from_trello

DESKTOP_PATH = os.path.join(os.path.expanduser("~"), "Desktop")


class MemberActions:
    """
    Get actions of members of a Trello board.
    """

    def __init__(self, board_id):
        self.board_id = board_id

    def get_members(self) -> list[tuple[str, str]]:
        """
        Get a list of names and ids of members of a Trello board.
        """
        members_data = get_from_trello(f"boards/{self.board_id}/memberships?member=true")
        return [
            (member["member"]["fullName"], member["idMember"]) for member in members_data
        ]

    def get_latest_member_actions(self) -> list[tuple[str, tz.datetime]]:
        """
        Get a list of names and the date of the most recent action of each member,
        sorted by the most recent action.
        """
        results = []
        members = self.get_members()
        total = len(members)
        for count, m in enumerate(members):
            print(f"{count} of {total}")
            latest_action = tz.localdate() - tz.timedelta(days=500)
            actions = get_from_trello(f"members/{m[1]}/actions")
            for action in actions:
                date = tz.datetime.strptime(action["date"], "%Y-%m-%dT%H:%M:%S.%fZ")
                if date > latest_action:
                    latest_action = date
            results.append((m[0], latest_action))
        return sorted(results, key=lambda x: x[1], reverse=True)

    def output_results(self, output_file=None):
        """
        Export the results to a CSV file.
        """
        output_file = output_file or os.path.join(DESKTOP_PATH, "member_actions.csv")
        with open(output_file, "w+") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Member", "Last Action"])
            for name, action in self.get_latest_member_actions():
                writer.writerow([name, action.strftime("%Y-%m-%d %H:%M:%S")])

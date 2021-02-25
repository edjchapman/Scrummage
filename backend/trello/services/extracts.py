from trello.utils.api import get_from_trello
from trello.utils.string_utils import get_est


class TrelloBoard:
    """
    Logic to extract data from Trello.
    """

    def __init__(self, board_id="x1iNAXZx"):
        self.board_id = board_id

    @staticmethod
    def get_lists(board_id):
        return get_from_trello(endpoint=f"boards/{board_id}/lists")

    @staticmethod
    def get_cards(list_id):
        return get_from_trello(endpoint=f"lists/{list_id}/cards")

    def poll_data(self):
        lists = self.get_lists(self.board_id)
        for lst in lists:
            cards = self.get_cards(lst.get("id"))
            for c in cards:
                list_name = lst.get("name")
                name = c.get("name")
                labels = ", ".join([label.get("name") for label in c.get("labels")])
                url = c.get("shortUrl")
                estimate = get_est(name)

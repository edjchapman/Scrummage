from trello.models import TrelloBoard, TrelloList, TrelloCard, TrelloLabel
from trello.utils.api import get_from_trello
from trello.utils.string_utils import get_est


class TrelloBoardService:
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

    @staticmethod
    def save_board(board_id):
        # tb = get_from_trello(f"boards/{board_id}/lists")
        tb = get_from_trello(f"boards/{board_id}")
        trello_board, _ = TrelloBoard.objects.update_or_create(
            trello_id=tb.get("id"),
            defaults={"name": tb.get("name")}
        )
        return trello_board

    @staticmethod
    def save_list(trello_id, trello_board, name):
        trello_list, _ = TrelloList.objects.update_or_create(
            trello_id=trello_id,
            defaults={
                "trello_board": trello_board,
                "name": name
            }
        )
        return trello_list

    @staticmethod
    def save_card(t_id, t_list, t_labels, t_name, t_url, t_estimate):
        trello_card, _ = TrelloCard.objects.update_or_create(
            trello_id=t_id,
            defaults={
                "trello_list": t_list,
                "name": t_name,
                "url": t_url,
                "estimate": t_estimate
            }
        )
        for tl in t_labels:
            trello_card.trello_labels.add(tl)

    @staticmethod
    def save_labels(t_labels):
        trello_labels = []
        for tl in t_labels:
            trello_label, _ = TrelloLabel.objects.update_or_create(
                trello_id=tl.get("id"),
                defaults={"name": tl.get("name")}
            )
            trello_labels.append(trello_label)
        return trello_labels

    def pull_data(self):
        trello_board = self.save_board(board_id=self.board_id)
        trello_lists = self.get_lists(board_id=trello_board.trello_id)
        for tl in trello_lists:
            trello_list = self.save_list(
                trello_id=tl.get("id"),
                trello_board=trello_board,
                name=tl.get("name")
            )
            cards = self.get_cards(list_id=trello_list.trello_id)
            for c in cards:
                trello_labels = self.save_labels(c.get("labels"))
                self.save_card(
                    t_id=c.get("id"),
                    t_list=trello_list,
                    t_labels=trello_labels,
                    t_name=c.get("name"),
                    t_url=c.get("shortUrl"),
                    t_estimate=get_est(c.get("name"))
                )

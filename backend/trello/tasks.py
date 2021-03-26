import logging

from celery import shared_task

from trello.services.extracts import TrelloBoardService

logger = logging.getLogger(__name__)


@shared_task
def extract_trello_board_data(board_id="x1iNAXZx"):
    """Run service to extract data from a Trello board and save it to the DB.

    :param board_id: From the Trello URL.
    """
    TrelloBoardService(board_id).pull_data()

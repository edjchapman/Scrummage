from django.db import models

from common.models import BaseModel


class TrelloBoard(BaseModel):
    """
    Trello Board
    """
    trello_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TrelloList(BaseModel):
    """
    Trello List
    """
    trello_id = models.CharField(max_length=50)
    trello_board = models.ForeignKey('trello.TrelloBoard', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TrelloCard(BaseModel):
    """
    Trello Card.
    """
    trello_id = models.CharField(max_length=50)
    trello_list = models.ForeignKey('trello.TrelloList', on_delete=models.CASCADE)
    trello_labels = models.ManyToManyField('trello.TrelloLabel', blank=True)
    name = models.CharField(max_length=50)
    url = models.URLField(null=True, blank=True)
    points_estimated = models.FloatField(default=0, null=True, blank=True)
    points_consumed_extra = models.FloatField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name

    def label_list(self):
        return [tl.name for tl in self.trello_labels.all()]


class TrelloLabel(BaseModel):
    """
    Trello Label.
    """
    trello_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

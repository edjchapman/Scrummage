from django.db import models


class TrelloBoard(models.Model):
    """
    Trello Board
    """
    trello_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TrelloList(models.Model):
    """
    Trello List
    """
    trello_id = models.CharField(max_length=50)
    trello_board = models.ForeignKey('trello.TrelloBoard', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TrelloCard(models.Model):
    """
    Trello Card.
    """
    trello_id = models.CharField(max_length=50)
    trello_list = models.ForeignKey('trello.TrelloList', on_delete=models.CASCADE)
    trello_labels = models.ManyToManyField('trello.TrelloLabel', blank=True)
    name = models.CharField(max_length=50)
    url = models.URLField(null=True, blank=True)
    estimate = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def label_list(self):
        return [l.name for l in self.trello_labels.all()]


class TrelloLabel(models.Model):
    """
    Trello Label.
    """
    trello_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

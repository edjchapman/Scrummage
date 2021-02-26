from django.contrib import admin
from django.utils.html import format_html

from trello.models import TrelloBoard, TrelloList, TrelloCard, TrelloLabel


@admin.register(TrelloBoard)
class TrelloBoardAdmin(admin.ModelAdmin):
    """
    Trello Board Admin.
    """
    fields = [
        "trello_id",
        "name"
    ]

    list_display = [
        "trello_id",
        "name"
    ]

    search_fields = [
        "name"
    ]


@admin.register(TrelloList)
class TrelloListAdmin(admin.ModelAdmin):
    """
    Trello List Admin.
    """
    fields = [
        "trello_id",
        "trello_board",
        "name"
    ]

    list_display = [
        "trello_id",
        "trello_board",
        "name"
    ]

    search_fields = [
        "trello_board",
        "name"
    ]

    list_filter = [
        "trello_board"
    ]


@admin.register(TrelloCard)
class TrelloCardAdmin(admin.ModelAdmin):
    """
    Trello Card Admin.
    """
    fields = [
        "trello_id",
        "trello_list",
        "trello_labels",
        "name",
        "url",
        "estimate"
    ]

    list_display = [
        "trello_id",
        "trello_list",
        "name",
        "clickable_url",
        "estimate",
        "label_list"
    ]

    search_fields = [
        "name",
        "url"
    ]

    list_filter = [
        "trello_list__trello_board",
        "trello_list",
        "estimate",
        "trello_labels"
    ]

    def clickable_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.url)


@admin.register(TrelloLabel)
class TrelloLabelAdmin(admin.ModelAdmin):
    """
    Trello Label Admin.
    """
    fields = [
        "trello_id",
        "name"
    ]

    list_display = [
        "trello_id",
        "name"
    ]

    search_fields = [
        "name"
    ]

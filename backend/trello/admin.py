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
        "created_at",
        "name"
    ]
    readonly_fields = fields

    list_display = [
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
        "created_at",
        "trello_board",
        "name"
    ]
    readonly_fields = fields

    list_display = [
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
        "created_at",
        "trello_list",
        "trello_labels",
        "name",
        "url",
        "points_estimated",
        "points_consumed_extra"
    ]
    readonly_fields = [
        "trello_id",
        "created_at",
        "trello_list",
        "trello_labels",
        "name",
        "url"
    ]

    list_display = [
        "name",
        "clickable_url",
        "trello_list",
        "created_at",
        "points_estimated",
        "points_consumed_extra"
    ]

    search_fields = [
        "name",
        "url"
    ]

    list_filter = [
        "created_at",
        "points_estimated",
        "points_consumed_extra",
        "trello_list",
        "trello_list__trello_board",
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
        "created_at",
        "name"
    ]
    readonly_fields = fields

    list_display = [
        "name"
    ]

    search_fields = [
        "name"
    ]

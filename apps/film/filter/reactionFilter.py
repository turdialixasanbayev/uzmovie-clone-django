import django_filters
from ..models import Reaction

class ReactionFilter(django_filters.FilterSet):
    film = django_filters.NumberFilter(
        field_name="film_id",
        lookup_expr="exact",
        label="Film ID"
    )
    user = django_filters.NumberFilter(
        field_name="user_id",
        lookup_expr="exact",
        label="User ID"
    )
    reaction = django_filters.ChoiceFilter(
        field_name="reaction",
        choices=Reaction.ReactionType.choices,
        label="Reaction Type"
    )
    created_at = django_filters.DateFromToRangeFilter(
        field_name="created_at",
        label="Created Between"
    )

    class Meta:
        model = Reaction
        fields = ["film", "user", "reaction", "created_at"]

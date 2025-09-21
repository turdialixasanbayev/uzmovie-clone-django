# film/filters.py
from django.db.models import Q
from django_filters import rest_framework as filters
from ..models import Film
from apps.category.models import Category, Tag
from ..models import Country


class FilmFilter(filters.FilterSet):
    # oddiy matn qidiruv (nom va description bo'yicha)
    search = filters.CharFilter(method='filter_search', label='Search (name/description)')

    # toifalar va taglar (ko'p tanlovli)
    category = filters.ModelChoiceFilter(queryset=Category.objects.all())
    tags = filters.ModelMultipleChoiceFilter(field_name='tags', queryset=Tag.objects.all())

    # mamlakat
    country = filters.ModelChoiceFilter(queryset=Country.objects.all())

    # yil diapazoni
    year = filters.NumericRangeFilter(field_name='year', label='Year range (min..max)')  # requires django-filter >= 23
    year_min = filters.NumberFilter(field_name='year', lookup_expr='gte', label='Year >= ')
    year_max = filters.NumberFilter(field_name='year', lookup_expr='lte', label='Year <= ')

    # til, age_type, p (video quality)
    language = filters.ChoiceFilter(field_name='language', choices=Film.LANGUAGE.choices)
    age_type = filters.ChoiceFilter(field_name='age_type', choices=Film.AGE_TYPE.choices)
    p = filters.ChoiceFilter(field_name='p', choices=Film.P)

    # ko'rilganlar diapazoni
    min_views = filters.NumberFilter(field_name='views', lookup_expr='gte')
    max_views = filters.NumberFilter(field_name='views', lookup_expr='lte')

    # sanalar (release_date bo'yicha from-to)
    release_date_after = filters.DateTimeFilter(field_name='release_date', lookup_expr='gte')
    release_date_before = filters.DateTimeFilter(field_name='release_date', lookup_expr='lte')

    # duration (sekund yoki ISO duration string bilan solishtirish mumkin)
    duration_min = filters.DurationFilter(field_name='duration', lookup_expr='gte')
    duration_max = filters.DurationFilter(field_name='duration', lookup_expr='lte')

    # trailer_link / bot_link qidiruvi (icontains)
    trailer_contains = filters.CharFilter(field_name='trailer_link', lookup_expr='icontains')
    bot_contains = filters.CharFilter(field_name='bot_link', lookup_expr='icontains')

    ordering = filters.OrderingFilter(
        fields=(
            ('release_date', 'release_date'),
            ('views', 'views'),
            ('year', 'year'),
            ('name', 'name'),
            ('p', 'p'),
        )
    )

    class Meta:
        model = Film
        # foydalanuvchi URL params misol: ?search=abc&category=1&tags=1&tags=2&min_views=10
        fields = []

    def filter_search(self, queryset, name, value):
        """
        Search in name and description (case-insensitive).
        """
        if not value:
            return queryset
        value = value.strip()
        return queryset.filter(
            Q(name__icontains=value) |
            Q(description__icontains=value)
        )

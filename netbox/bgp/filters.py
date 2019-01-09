from __future__ import unicode_literals

import django_filters
from django.db.models import Q
from extras.filters import CustomFieldFilterSet
from utilities.filters import NumericInFilter, TagFilter
from .constants import BGP_TYPE_CHOICES, BGP_STATE_CHOICES
from .models import Neighbor, NeighborState


class NeighborFilter(CustomFieldFilterSet, django_filters.FilterSet):
    id__in = NumericInFilter(name='id', lookup_expr='in')
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    tag = TagFilter()

    class Meta:
        model = Neighbor
        fields = ['remote_asn']

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(remote_asn__icontains=value)
        )

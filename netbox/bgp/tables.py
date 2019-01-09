import django_tables2 as tables
from django_tables2.utils import Accessor
from utilities.tables import BaseTable, ToggleColumn
from .models import Neighbor


class NeighborTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = Neighbor
        fields = ('pk', 'neighbor_address', 'remote_asn', 'description', 'import_policy', 'export_policy')

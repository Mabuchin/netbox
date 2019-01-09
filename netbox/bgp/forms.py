from __future__ import unicode_literals

from django import forms
from extras.forms import AddRemoveTagsForm, CustomFieldForm, CustomFieldBulkEditForm, CustomFieldFilterForm
from utilities.forms import (
    AnnotatedMultipleChoiceField, APISelect, add_blank_choice, BootstrapMixin, ChainedFieldsMixin,
    ChainedModelChoiceField, CommentField, CSVChoiceField, FilterChoiceField, SmallTextarea, SlugField,
)
from .models import Neighbor


class NeighborFilterForm(BootstrapMixin, CustomFieldFilterForm):
    model = Neighbor
    q = forms.CharField(required=False, label='Search')
    asn = forms.IntegerField(required=False, label='ASN')

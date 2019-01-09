from django.db import models
from ipam.constants import *
from .constants import *
from .fields import ASNField
from ipam.fields import IPNetworkField, IPAddressField
from extras.models import CustomFieldModel
from utilities.models import ChangeLoggedModel
from django.utils.encoding import python_2_unicode_compatible
from django.urls import reverse
from taggit.managers import TaggableManager


@python_2_unicode_compatible
class NeighborState(ChangeLoggedModel):
    state = models.PositiveSmallIntegerField(
        choices=BGP_STATE_CHOICES,
    )
    advertised_routes = models.PositiveIntegerField(
        verbose_name='ReceivedRoute',
        default=0,
        help_text='The neighbor bgp advertised routes'
    )
    received_routes = models.PositiveIntegerField(
        verbose_name='ReceivedRoute',
        default=0,
        help_text='The neighbor bgp received routes'
    )
    accepted_receive_routes = models.PositiveIntegerField(
        verbose_name='ReceivedRoute',
        default=0,
        help_text='The neighbor bgp received routes'
    )


@python_2_unicode_compatible
class Neighbor(ChangeLoggedModel, CustomFieldModel):
    """
     It is BGP session information.
     Includes both iBGP and eBGP.
    """
    type = models.PositiveSmallIntegerField(
        choices=BGP_TYPE_CHOICES
    )
    family = models.PositiveSmallIntegerField(
        choices=AF_CHOICES
    )
    neighbor_address = IPAddressField(
        help_text='IPv4 or IPv6 neighbor address (without mask)'
    )
    router_id = IPAddressField(
        help_text='IPv4 or IPv6 router-id'
    )
    remote_router_id = IPAddressField(
        help_text='IPv4 or IPv6 router-id',
        blank=True
    )
    local_asn = ASNField(
        blank=True,
        null=True,
        verbose_name='LocalASN'
    )
    remote_asn = ASNField(
        blank=True,
        null=True,
        verbose_name='RemoteASN'
    )
    vrf = models.ForeignKey(
        to='ipam.VRF',
        on_delete=models.PROTECT,
        related_name='vrfs',
        blank=True,
        null=True
    )
    interface = models.ForeignKey(
        to='dcim.Interface',
        on_delete=models.PROTECT,
        related_name='vrfs',
        blank=True,
        null=True
    )
    description = models.CharField(
        max_length=100,
        blank=True
    )

    import_policy = models.CharField(
        max_length=500,
        blank=True
    )

    export_policy = models.CharField(
        max_length=500,
        blank=True
    )

    state = models.ForeignKey(
        to='bgp.NeighborState',
        on_delete=models.PROTECT,
        related_name='vrfs',
        blank=True,
        null=True
    )

    # import_policy = models.ForeignKey(
    #    to='bgp.BGPRoutingPolicy',
    #    on_delete=models.PROTECT,
    #    related_name='import_policy',
    #    blank=True
    # )
    # export_policy = models.ForeignKey(
    #    to='bgp.BGPRoutingPolicy',
    #    on_delete=models.PROTECT,
    #    related_name='export_policy',
    #    blank=True
    # )
    tags = TaggableManager()
    csv_headers = ['neighbor', 'descr', 'vrf', 'local_asn', 'remote_asn', 'state', 'advertised_routes',
                   'received_routes', 'accepted_receive_routes']

    class Meta:
        ordering = ['remote_asn', 'local_asn', 'neighbor_address', 'interface']
        verbose_name = 'IP address'
        verbose_name_plural = 'IP addresses'

    def __str__(self):
        return str(self.display_name)

    def get_absolute_url(self):
        return reverse('bgp:neighbor', args=[self.pk])

    @property
    def display_name(self):
        if self.name and self.rd:
            return "{}({},{})".format(self.neighbor_address, self.remote_asn, self.description)
        return None

    def to_csv(self):
        return (
            self.neighbor_address,
            self.description,
            self.vrf,
            self.local_asn,
            self.remote_asn,
            self.state.state,
            self.state.advertised_routes,
            self.state.received_routes,
            self.state.accepted_receive_routes,
        )


class BGPRoutingPolicy(ChangeLoggedModel):
    """
     NOT IMPLEMENTED YET
     It is routing policy for bgp
    """
    pass

from __future__ import unicode_literals

BGP_TYPE_CHOICES = (
    (0, 'iBGP'),
    (1, 'eBGP'),
    (2, 'MPBGP'),
)

BGP_STATE_CHOICES = (
    (0, 'IDLE'),
    (1, 'CONNECT'),
    (2, 'ACTIVE'),
    (3, 'OPEN_CONFIRM'),
    (4, 'ESTABLISHED')
)
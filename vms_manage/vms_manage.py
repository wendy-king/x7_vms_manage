# vim: tabstop=4 shiftwidth=4 softtabstop=4

import logging
from steer.api.base import *

LOG = logging.getLogger(__name__)


def vms_manage_api(request):
    management_url = url_for(request, 'engine_billing')
    LOG.debug('billing_api connection created using token "%s"'
                     ' and url "%s"' %
                    (request.user.token, management_url))
#
#

def vms_manage_query(request, **kwargs):
    return vms_manage_api(request).query(**kwargs)

# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2011 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Copyright 2011 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Views for managing Engine instances.
"""
import datetime
import logging

from django import http
from django import shortcuts
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import SortedDict
from django.utils.translation import ugettext as _
import x7x.api.exceptions as api_exceptions

from steer.api.base import *

import steer
from steer import api
from steer import forms
from steer import test


from ..vms_manage import vms_manage_query
from ..forms import DateIntervalForm

LOG = logging.getLogger(__name__)



def vm_state(request, vm_id):
   pass


@login_required
#def usage_for_tenant(request, tenant_id=None):
#    return migrate_vm(request, tenant_id or request.user.tenant_id)


@login_required
def state(request, vm_id=None):
    return vm_state(request, None)

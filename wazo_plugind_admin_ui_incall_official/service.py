# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_admin_ui.helpers.confd import confd
from wazo_admin_ui.helpers.service import BaseConfdExtensionService


class IncallService(BaseConfdExtensionService):

    resource_confd = 'incalls'

    def get_first_incall_context(self, name=None):
        result = confd.contexts.list(type='incall', name=name, limit=1, direction='asc', order='id')
        for context in result['items']:
            return context

    def get_context(self, context):
        result = confd.contexts.list(name=context)
        for context in result['items']:
            return context

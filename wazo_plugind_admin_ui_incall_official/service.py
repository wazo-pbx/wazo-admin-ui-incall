# Copyright 2017-2018 The Wazo Authors  (see the AUTHORS file)
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

    def update(self, incall):
        super().update(incall)
        self._update_schedules_relations(incall)

    def _update_schedules_relations(self, incall):
        schedules = incall.get('schedules')
        if schedules:
            existing_incall = confd.incalls.get(incall)
            if existing_incall['schedules']:
                schedule_id = existing_incall['schedules'][0]['id']
                confd.incalls(incall).remove_schedule(schedule_id)

            if schedules[0].get('id'):
                confd.incalls(incall).add_schedule(schedules[0])

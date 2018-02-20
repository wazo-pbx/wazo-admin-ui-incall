# Copyright 2017-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_babel import lazy_gettext as l_
from flask_menu.classy import classy_menu_item

from wazo_admin_ui.helpers.classful import BaseView

from .form import IncallForm


class IncallView(BaseView):
    form = IncallForm
    resource = 'incall'

    @classy_menu_item('.incalls', l_('Incalls'), order=4, icon="long-arrow-right")
    def index(self):
        return super(IncallView, self).index()

    def _populate_form(self, form):
        form.extensions[0].exten.choices = self._build_set_choices_exten(form.extensions[0])
        form.extensions[0].context.choices = self._build_set_choices_context(form.extensions[0])
        form.schedules[0].form.id.choices = self._build_set_choices_schedule(form.schedules[0])
        return form

    def _build_set_choices_exten(self, extension):
        if not extension.exten.data or extension.exten.data == 'None':
            return []
        return [(extension.exten.data, extension.exten.data)]

    def _build_set_choices_context(self, extension):
        if not extension.context.data or extension.context.data == 'None':
            context = self.service.get_first_incall_context()
        else:
            context = self.service.get_context(extension.context.data)

        if context:
            return [(context['name'], context['label'])]

        return [(extension.context.data, extension.context.data)]

    def _build_set_choices_schedule(self, schedule):
        if not schedule.form.id.data or schedule.form.id.data == 'None':
            return []
        return [(schedule.form.id.data, schedule.form.name.data)]

    def _map_resources_to_form_errors(self, form, resources):
        form.populate_errors(resources.get('incall', {}))
        form.extensions[0].populate_errors(resources.get('extension', {}))
        return form

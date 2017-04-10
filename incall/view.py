# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask_menu.classy import classy_menu_item

from wazo_admin_ui.helpers.classful import BaseView

from .form import IncallForm


class IncallView(BaseView):

    form = IncallForm
    resource = 'incall'

    @classy_menu_item('.incalls', 'Incalls', order=4, icon="long-arrow-right")
    def index(self):
        return super(IncallView, self).index()

    def _map_resources_to_form(self, resources):
        return self.form(data=resources['incall'])

    def _map_form_to_resources(self, form, form_id=None):
        incall = form.to_dict()
        resources = {'incall': incall,
                     'extension': incall['extensions'][0]}
        if form_id:
            resources['incall']['id'] = form_id
        return resources

    def _map_resources_to_form_errors(self, form, resources):
        form.populate_errors(resources.get('incall', {}))
        form.extensions[0].populate_errors(resources.get('extension', {}))
        return form

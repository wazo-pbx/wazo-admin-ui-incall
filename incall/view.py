# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

from flask_menu.classy import classy_menu_item
from marshmallow import fields

from wazo_admin_ui.helpers.classful import BaseView
from wazo_admin_ui.helpers.mallow import BaseSchema, BaseAggregatorSchema, extract_form_fields

from .form import IncallForm


class IncallSchema(BaseSchema):

    class Meta:
        fields = extract_form_fields(IncallForm)


class AggregatorSchema(BaseAggregatorSchema):
    _main_resource = 'incall'

    incall = fields.Nested(IncallSchema)


class IncallView(BaseView):

    form = IncallForm
    resource = 'incall'
    schema = AggregatorSchema

    @classy_menu_item('.incalls', 'Incalls', order=4, icon="long-arrow-right")
    def index(self):
        return super(IncallView, self).index()

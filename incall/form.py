# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask_wtf import FlaskForm

from wtforms.fields import SubmitField
from wtforms.fields import StringField

from wtforms.validators import InputRequired

from wazo_admin_ui.helpers.destination import DestinationField


class IncallForm(FlaskForm):
    did = StringField('Did', [InputRequired()])
    destination = DestinationField()
    submit = SubmitField('Submit')

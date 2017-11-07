# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wtforms.fields import SubmitField, StringField, SelectField, FieldList, FormField

from wtforms.validators import InputRequired

from wazo_admin_ui.helpers.destination import DestinationField
from wazo_admin_ui.helpers.form import BaseForm


class ExtensionForm(BaseForm):
    exten = StringField('Did', [InputRequired()])
    context = SelectField('Context', choices=[])


class IncallForm(BaseForm):
    extensions = FieldList(FormField(ExtensionForm), min_entries=1)
    destination = DestinationField()
    submit = SubmitField('Submit')

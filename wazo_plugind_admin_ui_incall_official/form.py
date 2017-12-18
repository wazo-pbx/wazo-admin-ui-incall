# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wtforms.fields import SubmitField, StringField, SelectField, FieldList, FormField, HiddenField

from wtforms.validators import InputRequired, Length

from wazo_admin_ui.helpers.destination import DestinationField
from wazo_admin_ui.helpers.form import BaseForm


class ExtensionForm(BaseForm):
    id = HiddenField()
    exten = SelectField('Did', [InputRequired()], choices=[])
    context = SelectField('Context', choices=[])


class IncallForm(BaseForm):
    extensions = FieldList(FormField(ExtensionForm), min_entries=1)
    destination = DestinationField()
    preprocess_subroutine = StringField('Preprocess Subroutine', [Length(max=39)])
    caller_id_mode = SelectField('Callerid mode', choices=[
        ('', 'None'),
        ('prepend', 'Prepend'),
        ('overwrite', 'Overwrite'),
        ('append', 'Append')
    ])
    caller_id_name = StringField('Callerid name', [Length(max=80)])
    submit = SubmitField('Submit')

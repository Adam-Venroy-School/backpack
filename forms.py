from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

class AddForm(FlaskForm):
    name = StringField('Item Name', [validators.Length(min=1, max=100)])
    description = StringField('Description', [validators.Length(min=1, max=100)])
    add_submit = SubmitField('Add')

class DeleteForm(FlaskForm):
    name = StringField('Item Name', [validators.Length(min=1, max=100)])
    delete_submit = SubmitField('Delete')

class ClearForm(FlaskForm):
    clear_submit = SubmitField('Clear')

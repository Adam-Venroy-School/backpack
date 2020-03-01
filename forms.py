from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

class AddForm(FlaskForm):
    name = StringField('Item Name', [validators.Length(min=1,max=20,message="Ensure Item Name is less than 20 characters")])
    description = StringField('Description', [validators.Length(max=100)])
    add_submit = SubmitField('Add')

class DeleteForm(FlaskForm):
    name = StringField('Item Name', [validators.Length(min=1, max=20)])
    delete_submit = SubmitField('Delete')

class ClearForm(FlaskForm):
    clear_submit = SubmitField('Clear')

class EditForm(FlaskForm):
    name = StringField('New Name', [validators.Length(min=1, max=20)])
    description = StringField('New Description',[validators.length(min=1, max=100)])
    edit_submit = SubmitField('Edit')

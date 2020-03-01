from flask import render_template, redirect, url_for
from backpack_functions import *
from database import *
from forms import AddForm, DeleteForm, ClearForm, EditForm
app.secret_key = 'dev'


@app.route("/",methods=['GET'])
@app.route("/home",methods=['GET'])
def home():
    add_form = AddForm()
    delete_form = DeleteForm()
    clear_form = ClearForm()
    edit_form = EditForm()
    contents = view_backpack()
    return render_template("home.html",contents=contents,add_form=add_form,delete_form=delete_form,clear_form=clear_form,edit_form=edit_form,id=id)

@app.route("/add",methods=['POST', 'GET'])
def add():
    add_form = AddForm()
    if not add_form.validate_on_submit():
        return redirect(url_for('home'))
    item_name = add_form.name.data
    description = add_form.description.data
    if len(description) < 1:
        description = "No Description"
    add_backpack(item_name, description)
    return redirect(url_for('home'))

@app.route("/deletename",methods=['POST', 'GET'])
def deletename():
    delete_form = DeleteForm()
    if not delete_form.validate_on_submit():
        return redirect(url_for('home'))
    print(delete_form.name.data)
    item_name = delete_form.name.data
    delete_name_backpack(item_name)
    return redirect(url_for('home'))

@app.route("/deletebutton/<int:id>",methods=['POST', 'GET'])
def deletebutton(id):
    delete_form = DeleteForm()
    delete_button_backpack(id)
    return redirect(url_for('home'))


@app.route("/clear",methods=['POST', 'GET'])
def clear():
    clear_backpack()
    return redirect(url_for('home'))

@app.route("/edit/<int:id>",methods=['POST', 'GET'])
def edit(id):
    edit_form = EditForm()
    name = edit_form.name.data
    description = edit_form.description.data
    if len(description) < 1:
        description = "No Description"
    edit_backpack(id, name, description)
    return redirect('/')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

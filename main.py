from flask import Flask, render_template
import sqlite3
from backpack_functions import *
from forms import AddForm, DeleteForm

app = Flask(__name__)
app.secret_key = 'dev'
db = "backpackdb.db"

@app.route("/",methods=['GET', 'POST'])
@app.route("/home",methods=['GET', 'POST'])
def home():
    add_form = AddForm()
    delete_form = DeleteForm()
    if add_form.add_submit.data and add_form.validate():
        item_name = add_form.name.data
        description = add_form.description.data
        if description == None:
            description = 'No Description'
            if item_name != None:
                add_backpack(db, item_name, description)

    if delete_form.delete_submit.data and delete_form.validate():
        item_name = delete_form.name.data
        delete_backpack(db,item_name)

    list = view_backpack(db)
    return render_template("home.html",list=list,add_form=add_form,delete_form=delete_form)


if __name__ == '__main__':
    app.run(debug=True)

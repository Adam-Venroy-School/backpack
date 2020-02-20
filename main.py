from flask import Flask, render_template, redirect, url_for
from backpack_functions import *
from forms import AddForm, DeleteForm, ClearForm

app = Flask(__name__)
app.secret_key = 'dev'
db = "backpackdb.db"

@app.route("/",methods=['GET'])
@app.route("/home",methods=['GET'])
def home():
    add_form = AddForm()
    delete_form = DeleteForm()
    clear_form = ClearForm()
    list = view_backpack(db)
    return render_template("home.html",list=list,add_form=add_form,delete_form=delete_form,clear_form=clear_form)

@app.route("/add",methods=['POST', 'GET'])
def add():
    add_form = AddForm()
    item_name = add_form.name.data
    description = add_form.description.data
    if len(description) < 1:
        description = "No Description"
    add_backpack(db, item_name, description)
    return redirect(url_for('home'))

@app.route("/delete",methods=['POST', 'GET'])
def delete():
    delete_form = DeleteForm()
    print(delete_form.name.data)
    item_name = delete_form.name.data
    delete_backpack(db, item_name)
    return redirect(url_for('home'))

@app.route("/clear",methods=['POST', 'GET'])
def clear():
    clear_backpack(db)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

from flask import render_template, redirect, url_for
from backpack_functions import *
from database import *
from forms import AddForm, DeleteForm, ClearForm, EditForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash

app.secret_key = 'dev'
db.create_all()

# Home Page. Users can see the items in the backpack and interact with them.
@app.route("/",methods=['GET'])
@app.route("/home",methods=['GET'])
def home():
    # Adding all the forms to home page to be able to input data
    add_form = AddForm()
    delete_form = DeleteForm()
    clear_form = ClearForm()
    edit_form = EditForm()
    contents = view_backpack()
    return render_template("home.html",contents=contents,add_form=add_form,delete_form=delete_form,clear_form=clear_form,edit_form=edit_form,id=id)

# Add Page. Users can type names and description to add to the backpack.
@app.route("/add",methods=['POST', 'GET'])
def add():
    # Adding Addform so we can get the data from the home page
    add_form = AddForm()
    #If it does not validate, return home
    if not add_form.validate_on_submit():
        flash("Name or Description too long")
        return redirect(url_for('home'))
    # Setting variable to data for easy reading
    item_name = add_form.name.data
    description = add_form.description.data
    add_backpack(item_name, description)
    return redirect(url_for('home'))

# Delete by Name Page. When the user deletes by typing in a name, items with that name are deleted.
@app.route("/deletename",methods=['POST', 'GET'])
def delete_name():
    delete_form = DeleteForm()
    #If it does not validate, return home
    if not delete_form.validate_on_submit():
        return redirect(url_for('home'))
    item_name = delete_form.name.data
    delete_name_backpack(item_name)

    return redirect(url_for('home'))

# Delete by Button Page. When the delete button is pressed, the item get deleted by ID.
@app.route("/deletebutton/<int:id>",methods=['POST', 'GET'])
def delete_button(id):
    delete_form = DeleteForm()
    delete_button_backpack(id)
    return redirect(url_for('home'))

# Clear Page. Deletes everything
@app.route("/clear",methods=['POST', 'GET'])
def clear():
    clear_backpack()
    return redirect(url_for('home'))

# Edit Page. Edits an item that the user changes.
@app.route("/edit/<int:id>",methods=['POST', 'GET'])
def edit(id):
    edit_form = EditForm()
    #If it does not validate, it will return home without doing code.
    if not edit_form.validate_on_submit():
        flash("Name or Description too Long")
        return redirect(url_for('home'))
    name = edit_form.name.data
    description = edit_form.description.data
    edit_backpack(id, name, description)
    return redirect('/')

@app.route("/createuser", methods=['POST', 'GET'])
def createuser():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        username = register_form.name.data
        password = generate_password_hash(register_form.password.data,method='sha256',salt_length=8)
        print(username, password)
        register_user(username, password)
    return render_template('createuser.html', register_form=register_form)

@app.route("/login", methods=['POST', 'GET'])
def loginuser():
    login_form = LoginForm()
    username = login_form.username.data
    password = login_form.userpassword.data
    user = session.query(User).filter(User.name == username)
    userpassword = session.query(User).filter()
    return render_template('login.html')



#If anything other than home is reached, it will be redirected to home page
@app.errorhandler(404)
def error(e):
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)


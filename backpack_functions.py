from database import *

def view_backpack():
    contents = Content.query.all()
    return contents # Returns every item in table

def add_backpack(item_name, item_description):
    if len(item_description) == 0:
        item_description = "No Description" #If the user inputs no description, we set it to this
    entry = Content(name=item_name,description=item_description)
    db.session.add(entry)
    db.session.commit()


def delete_name_backpack(item_name):
    Content.query.filter(Content.name==item_name).delete() # Finds row with item name and deletes item

def clear_backpack():
    items = Content.query.all()
    print(items)
    for item in items: # For every item in the database, delete it. This clears the DB
        db.session.delete(item)
    db.session.commit()

def edit_backpack(id, new_item, new_description):
    if len(new_item) != 0: # If the length of the name is 0, keep the old name
        Content.query.filter(Content.id==id).update({"name": new_item}) # Find by ID and change name to new_item
    if len(new_description) == 0: # If the length of description is 0, replace with 'No Description'
        new_description = "No Description"
    Content.query.filter(Content.id==id).update({"description": new_description}) # Find by ID and change description to new_description
    db.session.commit()

def delete_button_backpack(id):
    Content.query.filter(Content.id==id).delete() # Find item by ID and delete it
    db.session.commit()

def register_user(name, password):
    entry = User(username=name,password=password)
    db.session.add(entry)
    db.session.commit()



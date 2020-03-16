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
    Content.query.filter(Content.name==item_name).delete() # Runs query and deletes item
    db.session.commit()

def clear_backpack():
    items = Content.query.all()
    # For every item in backpack, it will delete it.
    for item in items:
        db.session.delete(item)
    db.session.commit()

def edit_backpack(id, new_item, new_description):
    if len(new_item) != 0: # If the new name has text it will be replaced
        Content.query.filter(Content.id==id).update({"name": new_item})
    Content.query.filter(Content.id==id).update({"description": new_description})
    db.session.commit()

def delete_button_backpack(id):
    Content.query.filter(Content.id==id).delete()
    db.session.commit()

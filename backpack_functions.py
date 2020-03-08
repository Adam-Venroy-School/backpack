from database import *

def view_backpack():
    contents = Content.query.all()
    return contents

def add_backpack(item_name, item_description):
    entry = Content(name=item_name,description=item_description) # Makes entry equal to a row that can be inputted into DB
    print(entry)
    db.session.add(entry) # Adds a row with item name and description in Content Table
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
    Content.query.filter(Content.id==id).update({"description": new_description}) # Find by ID and change description to new_description
    db.session.commit()

def delete_button_backpack(id):
    Content.query.filter(Content.id==id).delete() # Find item by ID and delete it
    db.session.commit()

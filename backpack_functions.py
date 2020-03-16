from database import *

def view_backpack():
    contents = Content.query.all()
    return contents # Returns every item in table

def add_backpack(item_name, item_description):
<<<<<<< HEAD
    if len(item_description) == 0:
        item_description = "No Description" #If the user inputs no description, we set it to this
    entry = Content(name=item_name,description=item_description)
    db.session.add(entry)
=======
    entry = Content(name=item_name,description=item_description) # Makes entry equal to a row that can be inputted into DB
    print(entry)
    db.session.add(entry) # Adds a row with item name and description in Content Table
>>>>>>> e72323b1e8a9c6e4e75a60f8a7ab020155632863
    db.session.commit()


def delete_name_backpack(item_name):
    Content.query.filter(Content.name==item_name).delete() # Finds row with item name and deletes item

def clear_backpack():
    items = Content.query.all()
<<<<<<< HEAD
    # For every item in backpack, it will delete it.
    for item in items:
=======
    print(items)
    for item in items: # For every item in the database, delete it. This clears the DB
>>>>>>> e72323b1e8a9c6e4e75a60f8a7ab020155632863
        db.session.delete(item)
    db.session.commit()

def edit_backpack(id, new_item, new_description):
<<<<<<< HEAD
    if len(new_item) != 0: # If the new name has text it will be replaced
        Content.query.filter(Content.id==id).update({"name": new_item})
    Content.query.filter(Content.id==id).update({"description": new_description})
=======
    if len(new_item) != 0: # If the length of the name is 0, keep the old name
        Content.query.filter(Content.id==id).update({"name": new_item}) # Find by ID and change name to new_item
    Content.query.filter(Content.id==id).update({"description": new_description}) # Find by ID and change description to new_description
>>>>>>> e72323b1e8a9c6e4e75a60f8a7ab020155632863
    db.session.commit()

def delete_button_backpack(id):
    Content.query.filter(Content.id==id).delete() # Find item by ID and delete it
    db.session.commit()

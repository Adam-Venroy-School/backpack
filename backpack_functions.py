from database import *

def view_backpack():
    contents = Content.query.all()
    return contents

def add_backpack(item_name, item_description):
    entry = Content(name=item_name,description=item_description)
    print(entry)
    db.session.add(entry)
    db.session.commit()


def delete_name_backpack(item_name):
    Content.query.filter(Content.name==item_name).delete()
    db.session.commit()

def clear_backpack():
    items = Content.query.all()
    print(items)
    for item in items:
        db.session.delete(item)
    db.session.commit()

def edit_backpack(id, new_item, new_description):
    Content.query.filter(Content.id==id).update({"name": new_item})
    Content.query.filter(Content.id==id).update({"description": new_description})
    db.session.commit()

def delete_button_backpack(id):
    Content.query.filter(Content.id==id).delete()
    db.session.commit()

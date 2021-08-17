from model.contact import Contact
from model.group import Group
import random


def check_empty(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="CONTACT", lastname="TEST", address="REMOVE", email="FROM", workphone="GROUP"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="REMOVE FROM GROUP"))
    if len(db.get_groups_list_with_contacts()) == 0:
        list_contacts = db.get_contact_list()
        list_groups = db.get_group_list()
        contact = random.choice(list_contacts)
        group = random.choice(list_groups)
        app.contact.add_contact_to_group(contact, group)


def test_remove_contact_from_group(app, db, orm):
    check_empty(app, db)
    list_groups = db.get_groups_list_with_contacts()
    group = random.choice(list_groups)
    contacts = orm.get_contacts_in_group(group)
    contact = random.choice(contacts)
    list_before = orm.get_contacts_in_group(group)
    app.contact.delete_contact_from_group(contact, group)
    list_after = orm.get_contacts_in_group(group)
    list_before.remove(contact)
    assert sorted(list_before, key=Contact.id_or_max) == sorted(list_after, key=Contact.id_or_max)
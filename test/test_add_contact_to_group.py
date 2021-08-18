from model.contact import Contact
from model.group import Group
import random


def check_empty(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="CONTACT", lastname="TEST", address="ADD", email="TO", workphone="GROUP"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="ADD TO GROUP"))
    # Получить список групп, в которых свободен хотя бы один контакт
    if len(app.group.get_free_group_list(db, orm)) == 0:
        app.contact.create(Contact(firstname="CONTACT", lastname="TEST", address="ADD", email="TO", workphone="GROUP"))


def test_add_contact_to_group(app, db, orm):
    check_empty(app, db, orm)
    list_groups = app.group.get_free_group_list(db, orm)
    group = random.choice(list_groups)
    list_avaliable_contacts = orm.get_contacts_not_in_group(group)
    list_contacts_in_group_before = orm.get_contacts_in_group(group)
    contact = random.choice(list_avaliable_contacts)
    app.contact.add_contact_to_group(contact, group)
    list_contacts_in_group_after = orm.get_contacts_in_group(group)
    list_contacts_in_group_before.append(contact)
    assert sorted(list_contacts_in_group_before, key=Contact.id_or_max) == sorted(list_contacts_in_group_after, key=Contact.id_or_max)


from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def check_empty(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="CONTACT", lastname="TEST", address="ADD", email="TO", workphone="GROUP"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="ADD TO GROUP"))


def test_add_contact_to_group(app, db):
    check_empty(app, db)
    list_contacts = db.get_contact_list()
    list_groups = db.get_group_list()
    contact = random.choice(list_contacts)
    group = random.choice(list_groups)
    list_before = orm.get_contacts_in_group(group)
    app.contact.add_contact_to_group(contact, group)
    list_after = orm.get_contacts_in_group(group)
    list_before.append(contact)
    assert sorted(list_before, key=Contact.id_or_max) == sorted(list_after, key=Contact.id_or_max)


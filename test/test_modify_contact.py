from model.contact import Contact
import random


def check_empty_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Vasiliy", lastname="Kamyshkin", middlename="Petrovich",
                       bday="11", bmonth="December", byear="1984"))


def test_modify_random_contact(app, db, check_ui):
    check_empty_contact_list(app, db)
    mod_contact = (Contact(firstname="FIRSTNAME TO MODIFY"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    app.contact.modify_contact_by_id(contact.id, mod_contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = mod_contact
    old_contacts[index].id = new_contacts[index].id
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
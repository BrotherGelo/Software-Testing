# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Vasya", middlename="Vasiylyevich", lastname="Pupkin", nickname="Vasyan3000",
                               title="SYPER VASYA", company="international", address="bassejnaya street", home="homeless",
                               mobile="8800553535", email="vasyanT1000@vasya.ru", bday="10", bmonth="September", byear="1901")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

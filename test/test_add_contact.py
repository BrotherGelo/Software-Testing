# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Vasya", middlename="Vasiylyevich", lastname="Pupkin", nickname="Vasyan3000",
                      title="SYPER VASYA", company="international", address="bassejnaya street",
                      homephone="8-626-256-27-27", workphone="+7(777)227 27 27", mobilephone="8(800)555-35-35",
                      secondaryphone="682828", email="vasyanT1000@vasya.ru", email2="vasyanT1001@vasya.ru",
                      email3="vasyanT1002@vasya.ru", bday="10", bmonth="September", byear="1901")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    #old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="Vasya", middlename="Vasiylyevich", lastname="Pupkin", nickname="Vasyan3000",
                               title="SYPER VASYA", company="international", address="bassejnaya street", home="homeless",
                               mobile="8800553535", email="vasyanT1000@vasya.ru", bday="10", bmonth="September", byear="1901"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) + 1 == len(new_contacts)
# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits #+ string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# Ошибка при лишних пробелах в начале поля. Нужно сортировать при проверке.
testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                    homephone="", workphone="", mobilephone="", secondaryphone="", email="", email2="", email3="")] + [
           Contact(firstname=random_string("firstname", 5), lastname=random_string("lastname", 6),
                   address=random_string("address", 20), homephone=random_string("homephone", 6),
                   workphone=random_string("workphone", 6), mobilephone=random_string("mobilephone", 13),
                   secondaryphone="", email=random_string("email", 15), email2=random_string("email2", 10),
                   email3=random_string("email3", 10)) for i in range(3)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#Contact(firstname="Vasya", middlename="Vasiylyevich", lastname="Pupkin", nickname="Vasyan3000",
#        title="SYPER VASYA", company="international", address="bassejnaya street",
#        homephone="8-626-256-27-27", workphone="+7(777)227 27 27", mobilephone="8(800)555-35-35",
#        secondaryphone="682828", email="vasyanT1000@vasya.ru", email2="vasyanT1001@vasya.ru",
#        email3="vasyanT1002@vasya.ru", bday="10", bmonth="September", byear="1901")
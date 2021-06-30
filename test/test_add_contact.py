# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Vasya", middlename="Vasiylyevich", lastname="Pupkin", nickname="Vasyan3000",
                               title="SYPER VASYA", company="international", address="bassejnaya street", home="homeless",
                               mobile="8800553535", email="vasyanT1000@vasya.ru", bday="10", bmonth="September", byear="1901"))
    app.session.logout()

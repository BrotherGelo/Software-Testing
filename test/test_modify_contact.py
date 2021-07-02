from model.contact import Contact


def test_modify_contact(app):
    app.contact.modify_first_contact(Contact(firstname="Vasiliy", middlename="Petrovich", lastname="Pupkin", nickname="SuperPupkin",
                               title="SYPER VASYA", company="Umbrella inc", address="bassejnaya street", home="23",
                               mobile="8800553535", email="vasyanT1000@vasya.ru", bday="11", bmonth="December", byear="1984"))
    app.session.logout()
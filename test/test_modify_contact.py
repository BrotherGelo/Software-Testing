from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(title="TEST TITLE FOR DELETE"))
    app.contact.modify_first_contact(Contact(firstname="Vasiliy", middlename="Petrovich", lastname="Pupkin",
                                             bday="11", bmonth="December", byear="1984"))
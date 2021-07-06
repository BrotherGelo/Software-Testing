from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="TEST TITLE FOR MODIFY"))
    contact = (Contact(firstname="Vasiliy", lastname="Kamyshkin", middlename="Petrovich",
                       bday="11", bmonth="December", byear="1984"))
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    #contact.firstname = old_contacts[0].firstname
    #contact.lastname = old_contacts[0].lastname
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
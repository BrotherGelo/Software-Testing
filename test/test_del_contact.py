from model.contact import Contact
import time
t = 10

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(title="TEST TITLE FOR DELETE"))
    old_contacts = app.contact.get_contact_list()
    print(len(old_contacts))
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    print(len(new_contacts))
    #time.sleep(t)
    assert len(old_contacts) - 1 == app.contact.count()
    #assert len(old_contacts) - 1 == len(new_contacts)
    #old_contacts[0:1] = []
    #assert old_contacts == new_contacts

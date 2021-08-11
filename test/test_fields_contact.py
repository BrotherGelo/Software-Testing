import re
from model.contact import Contact


def check_empty_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact(firstname="TEST_Vasya", middlename="TEST_Vasiylyevich", lastname="TEST_Pupkin", nickname="TEST_Vasyan3000",
                    title="TEST_SYPER VASYA", company="TEST_international", address="TEST_bassejnaya street",
                    homephone="8-626-256-27-27", workphone="+7(777)227 27 27", mobilephone="8(800)555-35-35",
                    secondaryphone="682828", email="TEST_vasyanT1000@vasya.ru", email2="TEST_vasyanT1001@vasya.ru",
                    email3="TEST_vasyanT1002@vasya.ru", bday="10", bmonth="September", byear="1901"))


def test_compare_all_fields(app, db):
    check_empty_list(app, db)
    list_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    list_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(list_db)):
        contact_ui = list_ui[i]
        contact_db = list_db[i]
        a = contact_ui.address
        b = contact_db.address
        c = contact_ui.all_phones_from_home_page
        d = merge_phones_like_on_home_page(contact_db)
        e = contact_ui.all_emails_from_home_page
        f = merge_emails_like_on_home_page(contact_db)
        assert contact_ui.id == contact_db.id
        assert contact_ui.firstname == contact_db.firstname
        assert contact_ui.lastname == contact_db.lastname
        assert contact_ui.address == contact_db.address
        assert contact_ui.all_phones_from_home_page == merge_phones_like_on_home_page(contact_db)
        assert contact_ui.all_emails_from_home_page == merge_emails_like_on_home_page(contact_db)

"""
def test_compare_firstname_on_home_page(app):
    contact_from_edit_page, contact_from_home_page = preconditions_home_page(app)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname


def test_compare_lastname_on_home_page(app):
    contact_from_edit_page, contact_from_home_page = preconditions_home_page(app)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname


def test_compare_address_on_home_page(app):
    contact_from_edit_page, contact_from_home_page = preconditions_home_page(app)
    assert contact_from_home_page.address == contact_from_edit_page.address


def test_emails_on_home_page(app):
    contact_from_edit_page, contact_from_home_page = preconditions_home_page(app)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_phones_on_home_page(app):
    contact_from_edit_page, contact_from_home_page = preconditions_home_page(app)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    check_empty_list(app)
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone
    
def preconditions_home_page(app):
    check_empty_list(app)
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    return contact_from_edit_page, contact_from_home_page
"""

def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone,
                                        contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))





import re
from model.contact import Contact

def check_empty_list(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="TEST_Vasya", middlename="TEST_Vasiylyevich", lastname="TEST_Pupkin", nickname="TEST_Vasyan3000",
                    title="TEST_SYPER VASYA", company="TEST_international", address="TEST_bassejnaya street",
                    homephone="8-626-256-27-27", workphone="+7(777)227 27 27", mobilephone="8(800)555-35-35",
                    secondaryphone="682828", email="TEST_vasyanT1000@vasya.ru", email2="TEST_vasyanT1001@vasya.ru",
                    email3="TEST_vasyanT1002@vasya.ru", bday="10", bmonth="September", byear="1901")

def test_phones_on_home_page(app):
    check_empty_list()
    
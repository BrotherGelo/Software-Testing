import optparse

from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:


    def __init__(self, app):
        self.app = app

    def init_creation_of_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def select_first_contact(self, index):
        self.select_contact_by_index(index)

    def open_first_contact_for_editing(self):
        self.open_contact_by_index_for_editing(0)

    def open_contact_by_index_for_editing(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)
        self.change_field_value("byear", contact.byear)
        self.change_select_value("bday", contact.bday)
        self.change_select_value("bmonth", contact.bmonth)

    def change_select_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, contact):
        wd = self.app.wd
        self.init_creation_of_new_contact()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.return_to_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self, contact):
        self.delete_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.return_to_home_page()
        self.open_contact_by_index_for_editing(index)
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.return_to_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                firstname = element.find_elements_by_tag_name("td")[2].text
                lastname = element.find_elements_by_tag_name("td")[1].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname))
        return list(self.contact_cache)

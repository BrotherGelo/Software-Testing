from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

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

    def open_contact_by_id_for_editing(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector('a[href="edit.php?id=%s"]' % id).click()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
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

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.return_to_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.return_to_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        self.app.return_to_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

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

    def modify_contact_by_id(self, id, mod_contact):
        wd = self.app.wd
        self.app.return_to_home_page()
        self.open_contact_by_id_for_editing(id)
        self.fill_contact_form(mod_contact)
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
                address = element.find_elements_by_tag_name("td")[3].text
                all_emails = element.find_elements_by_tag_name("td")[4].text
                all_phones = element.find_elements_by_tag_name("td")[5].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                                                  all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        self.open_contact_by_index_for_editing(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name('address').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        return Contact(id=id, firstname=firstname, lastname=lastname, address=address, email=email,
                       email2=email2, email3=email3, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

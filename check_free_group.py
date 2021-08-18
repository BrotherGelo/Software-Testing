from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    list_contacts = db.get_contact_list()
    list_groups = db.get_group_list()
    free_groups = []
    for i in list_groups:
        contacts_number = len(db.get_contacts_in_group(i))
        if contacts_number != len(list_contacts):
            free_groups.append(i)
            contacts_not_in_group = db.get_contacts_not_in_group(i)
    groups = free_groups
finally:
    pass
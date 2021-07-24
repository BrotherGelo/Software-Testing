from model.contact import Contact
import random
import string
import os.path
import getopt
import sys
import jsonpickle


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    # print help information and exit:
    print(err)  # will print something like "option -a not recognized"
    getopt.usage()
    sys.exit(2)

n = 7
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits #+ string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                    homephone="", workphone="", mobilephone="", secondaryphone="", email="", email2="", email3="")] + [
Contact(firstname="Vasya", middlename="Vasiylyevich", lastname="Pupkin", nickname="Vasyan3000",
        title="SYPER VASYA", company="international", address="bassejnaya street",
        homephone="8-626-256-27-27", workphone="+7(777)227 27 27", mobilephone="8(800)555-35-35",
        secondaryphone="682828", email="vasyanT1000@vasya.ru", email2="vasyanT1001@vasya.ru",
        email3="vasyanT1002@vasya.ru", bday="10", bmonth="September", byear="1901")] + [
Contact(firstname=random_string("firstname", 5), lastname=random_string("lastname", 6),
        address=random_string("address", 20), homephone=random_string("homephone", 6),
        workphone=random_string("workphone", 6), mobilephone=random_string("mobilephone", 13),
        secondaryphone="", email=random_string("email", 15), email2=random_string("email2", 10),
        email3=random_string("email3", 10)) for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
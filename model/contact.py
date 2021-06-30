class Contact:

    def __init__(self, firstname, middlename, lastname, nickname, title, company, address, home, mobile, email, bday, bmonth, byear):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.email = email
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear


class Modify:

    def __init__(self, address):
        self.address = address
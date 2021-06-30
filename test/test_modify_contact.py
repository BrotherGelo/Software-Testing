from model.contact import Modify


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify(Modify(address="Bassejnaya street,\nNijnie cheryomushki Village"))
    app.session.logout()
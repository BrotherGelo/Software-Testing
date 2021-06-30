from model.group import Modify


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Modify(name="TEST GROUP"))
    app.session.logout()
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test name to delete"))
    app.group.modify_first_group(Group(name="TEST GROUP NAME"))

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="test header to delete"))
    app.group.modify_first_group(Group(header="TEST GROUP HEADER"))
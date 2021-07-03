from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test name to delete"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="TEST GROUP NAME"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="test header to delete"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="TEST GROUP HEADER"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
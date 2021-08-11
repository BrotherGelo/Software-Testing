from model.group import Group
import random


def check_empty_group_list(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="TEST GROUP NAME TO CHANGE", header="TEST GROUP HEADER TO CHANGE"))


def test_modify_random_group(app, db, check_ui):
    check_empty_group_list(app, db)
    mod_group = Group(name="TEST_MOD_NAME")
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    app.group.modify_group_by_id(group.id, mod_group)
    new_groups = db.get_group_list()
    old_groups[index] = mod_group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

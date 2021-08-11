# -*- coding: utf-8 -*-
from model.group import Group


# Баг: Ошибка при добавлении группы, в полях которой есть символ "'".


def test_add_group(app, db, check_ui, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list, key=Group.id_or_max)

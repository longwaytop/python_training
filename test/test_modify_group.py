from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="tested_group"))
    app.group.modify_first_group(Group(name="modified_group_name"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="tested_group"))
    app.group.modify_first_group(Group(header="modified_group_header"))

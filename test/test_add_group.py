# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
        app.session.login("admin", "secret")
        app.create_group(Group(name="group_name", header="header", footer="footer"))
        app.session.logout()


def test_empty_group(app):
        app.session.login("admin", "secret")
        app.create_group(Group(name="", header="", footer=""))
        app.session.logout()

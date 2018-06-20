# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Andrey", last_name="Andreev", address="Minsk city",
                            home_phone="+375170000000", mobile_phone="+375255554433", work_phone="+375170011122",
                            fax="none", first_email="andrey_andreev@gmail.com", second_email="lullil@gmail.com",
                            third_email="bzzz@mail.ru")
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="", last_name="", address="",
                            home_phone="", mobile_phone="", work_phone="",
                            fax="", first_email="", second_email="",
                            third_email="")
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name="", last_name="", address="", home_phone="", mobile_phone="", work_phone="",
                            fax="", first_email="", second_email="", third_email="", secondary_phone="")] + [
        Contact(first_name=random_string("firstname", 5), last_name=random_string("lastname", 5),
                address=random_string("address", 5), home_phone=random_string("home", 5),
                mobile_phone=random_string("mobile", 5),
                work_phone=random_string("work", 5), fax=random_string("fax", 5),
                first_email=random_string("email", 5), second_email=random_string("email2", 5),
                third_email=random_string("email3", 5), secondary_phone=random_string("phone2", 5))
        for i in range(3)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


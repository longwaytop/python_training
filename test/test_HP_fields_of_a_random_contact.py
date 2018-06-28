from model.contact import Contact
from random import randrange
import re


def test_high_priority_fields_of_random_contact(app):
    app.open_home_page()
    app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="Andrey", last_name="Andreev", address="Minsk city",
                            home_phone="+375170000000", mobile_phone="+375255554433", work_phone="+375170011122",
                            secondary_phone="secondary_phone", first_email="andrey_andreev@gmail.com",
                            second_email="lullil@gmail.com", third_email="bzzz@mail.ru"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.select_random_contact(index)
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def clear(s):
        return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone,
                                        contact.work_phone, contact.secondary_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.first_email, contact.second_email,
                                        contact.third_email]))))




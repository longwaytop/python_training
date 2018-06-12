from model.contact import Contact


def test_modify_contact_name(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="tested_contact_name"))
    app.contact.modify_first_contact(Contact(first_name="modified_first_name"))


def test_modify_contact_address(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="tested_contact_name"))
    app.contact.modify_first_contact(Contact(address="modified_address"))

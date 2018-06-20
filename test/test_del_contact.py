from model.contact import Contact


def test_delete_first_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="Alex"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)


from model.contact import Contact


def test_modify_contact_name(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="tested_contact_name", last_name=""))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="modified_first_name", last_name="")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_address(app):
#    app.open_home_page()
#    if app.contact.count() == 0:
#        app.contact.create_contact(Contact(first_name="tested_contact_name"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(address="modified_address"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)


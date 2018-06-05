from model.contact import Contact


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(first_name="edited_first_name", last_name="edited_last_name",
                                           address="edited_adress", home_phone="edited_home_phone",
                                           mobile_phone="edited_mobile_phone", work_phone="edited_mobile_phone",
                                           fax="edited_fax", first_email="edited_first_email", second_email="edited_second_email",
                                           third_email="edited_third_email",))
    app.session.logout()

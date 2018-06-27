from sys import maxsize


class Contact:
    def __init__(self, first_name=None, last_name=None, address=None,
                 home_phone=None, mobile_phone=None, work_phone=None,
                 fax=None, first_email=None, second_email=None, third_email=None,
                 secondary_phone=None, id=None, all_phones_from_home_page=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.first_email = first_email
        self.second_email = second_email
        self.third_email = third_email
        self.secondary_phone = secondary_phone
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.last_name, self.first_name, self.id)

    def __eq__(self, other):
        return self.last_name == other.last_name and self.first_name == other.first_name and (self.id is None or other.id is None or self.id == other.id)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

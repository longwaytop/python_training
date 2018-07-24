from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
        for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

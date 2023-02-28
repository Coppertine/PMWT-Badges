## Read all lines from staff.txt
## Format is like so: Name;id;role;quote
## Place each line into a class called Staff that is into a list called staff_list
## For each staff member, copy a new file from Template.svg to name.svg
## Replace "STAFFNAME" with the name of the staff member
## Replace "STAFFQUOTE" with the quote of the staff member
## Replace "STAFFROLE" with the role of the staff member
## Replace "PROFILELINK" with the dataurl of the url: https://a.ppy.sh/id replacing id with the staff id.

import base64
import requests

class Staff:
    def __init__(self, name, id, role, quote):
        self.name = name
        self.id = id
        self.role = role
        self.quote = quote

staff_list = []

def read_file():
    with open("staff.txt", "r") as f:
        for line in f:
            name, id, role, quote = line.split(";")
            staff_list.append(Staff(name, id, role, quote))

def generate_files():
    for staff in staff_list:
        with open("Template.svg", "r") as f:
            data = f.read()
        data = data.replace("STAFFNAME", staff.name)
        data = data.replace("STAFFQUOTE", staff.quote)
        data = data.replace("STAFFROLE", staff.role)
        profilelink = "https://a.ppy.sh/" + staff.id
        ## turn profilelink into dataurl blob
        profileuri = "data:image/png;base64," + base64.b64encode(requests.get(profilelink).content).decode("utf-8")
        data = data.replace("PROFILELINK", profileuri)
        with open(staff.name + ".svg", "w") as f:
            f.write(data)

read_file()
generate_files()


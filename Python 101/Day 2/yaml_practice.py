import datetime
import json
import yaml


person = {
    "firstName":"John",
    "dateOfBirth":datetime.date(1969,12,31),
    "married":False,
    "spouse":None,
    "children":["Bobby","Molly"]
}

print(json.dumps(person,indent=4,default=str))

print(yaml.__with_libyaml__)

email_message = """\
message:
  date: 2022-01-16 12:46:17Z
  from: john.doe@domain.com
  to:
    - bobby@domain.com
    - molly@domain.com
  cc:
    - jane.doe@domain.com
  subject: Friendly reminder
  content: |
    Dear XYZ,

    Lorem ipsum dolor sit amet...
  attachments:
    image1.gif: !!binary
        R0lGODdhCAAIAPAAAAIGAfr4+SwAA
        AAACAAIAAACDIyPeWCsClxDMsZ3CgA7
"""

print(yaml.safe_load(email_message))

print(yaml.safe_load(b"name: \xd0\x98\xd0\xb2\xd0\xb0\xd0\xbd"))

stream = """\
---
3.14
---
name: John Doe
age: 53
---
- apple
- banana
- orange
"""

for document in yaml.safe_load_all(stream):
    print(document)

print(yaml.safe_load("""
Shipping Address: &shipping |
    1111 College Ave
    Palo Alto
    CA 94306
    USA
Invoice Address: *shipping
"""))

#Dump to YAMl

print(yaml.dump(3.14,Dumper=yaml.Dumper))
print(yaml.dump(3.14,Dumper=yaml.CDumper))


data = {"name":"John"}

print(yaml.dump(data))

with open("file.yaml", mode="wt", encoding="utf-8") as file:
    yaml.dump(data, file)

with open("filebin.yaml", mode="wb") as file:
    yaml.dump(data,file,encoding="utf-8")

#Single document
print(yaml.dump([
    {"title":"Document #1"},
    {"title":"Document #2"},
    {"title":"Document #3"},
]))

#Multiple documents
print(yaml.dump_all([
    {"title":"Document #1"},
    {"title":"Document #2"},
    {"title":"Document #3"},
]))



post1 = {"user_id":209, "message": "D5 E5 C5 C4 G4", "language": "English", "datetime":"202305T1", "location":(44.590533, -104.715556)}
print(post1)

post2 = dict(message = "D5 E5 C5 C4 G4", language = "English")
post2["user_id"] = 209
post2["datetime"] = "202305T1"
print(post2)
print(post2['user_id'])

if 'location' in post2:
    print(post2['location'])
else:
    print("The post does not contain a location value")


try:
    print(post2['location'])  
except  KeyError:
    print("The post does not contain a location value")


for key in post1.keys():
    value = post1[key]
    print(key,"=", value)

for key, value in post1.items():
    print(key, value)
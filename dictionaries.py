post = {"user_id":209,"message":"D5 E5 C5 C4 G4","Language":"English","datetime":"20230124578","Location":(44.590533,-104.715556)}
"""key        |  values
  user_id     |  209
  message     |  "D5 E5 C5 C4 G4"
  language    |  "English"
  """
print("Before added new item")
for key in post.keys():
    value = post[key]
    print(key, "=", value)

post["Country"] = "Bangladesh"
print("After added new item")

for key,value in post.items():
    print(key, "=", value)
    

record={'roll no':101,'name':'shivi','age':20}
print(type(record))
print(id(record))
print(record)
print("roll no:",record['roll no'])
print("name:",record['name'])
print("age:",record['age'])
print(record.keys())
print(record.values())
record['name']='shiva'
print(id(record))
print(record)
for key in record:
    print(key,":",record[key])
del record['age']
print(id(record))
print(record)
print('name' in record)
print('age' in record)
record.clear()
print(id(record))
print(record)

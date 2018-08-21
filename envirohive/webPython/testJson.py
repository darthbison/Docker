import json


#dict = {'result':[{'key1':'value1','key2':'value2'}, {'key1':'value3','key2':'value4'}]}
dict = {'reading':[]} 
json_data = json.dumps(dict)

dict['reading'].append({'key3':'26'})
dict['reading'].append({'key4':'100'})

json_data = json.dumps(dict)
print(json_data)
#data["list"].append({'b':'2'})

# coding=utf-8
from json_process import JsonProcess
from Helper.list_process import ListProcess
from db_connection import DbConnection


#towel programming
def fibonacci(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b


#fibonacci(50)

def incrementer(n):
    return lambda x: x ** 2 + n

#list

lp = ListProcess()
l = lp.create_list()
sorted_list = ListProcess.sort_list(l)
print(sorted_list)



#print(sort_list(item_list))
#new_list = sort_list(item_list)
j_process = JsonProcess("cities.json")
j_process.dump_json(sorted_list)

'''
db = DbConnection()

data_list = db.get_all_data()
for item in data_list:
    print(item["name"])

item = db.get_by_id("40363590")
print(item["name"])
'''


#func = incrementer(10)
#print(func(3))

'''
j_process = JsonProcess("Data\cities.json")
city_list = j_process.read_json()
print(city_list["68"])

city_list["99"] = "Bağcılar"
j_process.dump_json(city_list)
'''
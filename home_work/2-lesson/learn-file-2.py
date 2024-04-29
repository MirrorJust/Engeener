# def unique_val(list_p):
#     list_p = set(list_p)
#     list_p = list(list_p)
#     return list_p
#
#
# list1 = [1, 2, 3]
# list2 = [5, 6, 4, 2, 3]
# list3 = [7, 8, 3, 2, 1, 2]
# list4 = [1, 5, 2, 2, 3]
#
# dict1 = {
#     "list1": list1,
#     "list2": list2,
#     "list3": list3,
#     "list4": list4,
# }
#
# # print(unique_val(dict1["list1"]))
# # print(unique_val(dict1["list2"]))
# # print(unique_val(dict1["list3"]))
# # print(unique_val(dict1["list4"]))

dict_num = {
    'first', 1,
    'second', 2,
    'third', 3
}
dict_str = {
    'first', 'первый',
    'second', 'второй',
    'third', 'третий'
}
dict_float = {
    'first', 1.23,
    'second', 2.99,
    'third', 3.55
}
dict_bool = {
    'first', True,
    'second', False,
}

dict_list = {
    "list1": [1, 3, 5],
    "list2": [52, 12, 33]
}

dict3 = {
    "dict_first": {
        1: 'first',
        2: 'second', },
    "dict_second": {
        4: "fourth",
        5: "fifth",
    }
}

dict3['dict_list'] = dict_list

# list_key = dict3.keys()
# list_val = dict3.values()
#
# print(list_key)
# print(list_val)

dict3['dict_first'][1] = 'third'

print(dict3['dict_first'])
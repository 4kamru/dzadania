def dict_to_list(dict_):
    mypairs = list(zip(dict_.keys(), dict_.values()))
    llist = []
    for i in mypairs:
        for j in range(len(i)):
            llist.append(i[j])

    return llist

def tuple_to_list(tuple_):
    llist = []
    for i in tuple_:
        llist.append(i)

    return llist

def set_to_list(set_):
    llist = []
    for i in set_:
        llist.append(i)

    return llist

def calculate_structure_sum(*args):
    res = 0
    for i, arg in enumerate(args):
        if isinstance(arg, str):
            if arg.isnumeric():
                res += int(arg)
            else:
                res += len(str(arg))
            continue
        elif isinstance(arg, int):
            res += int(arg)
            continue
        elif isinstance(arg, list):
            for j in arg:
                res += calculate_structure_sum(j)

        elif isinstance(arg, dict):
            res += calculate_structure_sum(*dict_to_list(arg))
            # continue
        elif  isinstance(arg, tuple):
            res += calculate_structure_sum(*tuple_to_list(arg))
            # continue
        elif isinstance(arg, set):
            res += calculate_structure_sum(*set_to_list(arg))



    return res

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
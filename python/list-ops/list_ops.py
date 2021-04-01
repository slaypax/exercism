def append(list1, list2):
    list1[len(list1):]= list2
    return list1


def concat(lists):
    concat_list = []
    for sublist in lists:
        for item in sublist:
            concat_list.append(item)
    return concat_list


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    length = 0
    for item in list:
        length += 1
    return length


def map(function, list):
   return [function(item) for item in list]

# i do not understand these folds
# https://eli.thegreenplace.net/2017/right-and-left-folds-primitive-recursion-patterns-in-python-and-haskell/
def foldl(function, list, initial):
    if not list:
        return initial
    else:
        return foldl(function, list[1:],function(initial, list[0]))
    pass


def foldr(function, list, initial):
    if not list:
        return initial
    else: 
        return function(list[0], foldr(function, list[1:], initial))


def reverse(list):
    return list[::-1]
    pass

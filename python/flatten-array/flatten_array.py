# https://docs.python.org/3/whatsnew/3.3.html#pep-380
# the generator needed to be nested so that the yield could actually be
# converted to a list and returned

def flatten(iterable):
    def generator(l):
        for element in l:
            if element == None: continue
            if type(element) == list:
                yield from generator(element)
            else:
                yield element
    return(list(generator(iterable)))
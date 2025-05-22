
# do it all function
def get_ints(ints, odd=True, even=True):
    if odd and even:
        return [i for i in ints]
    elif odd:
        return [i for i in ints if i % 2]
    elif even:
        return [i for i in ints if not i % 2]
    else:
        return []
    
# cleaner approach
def get_even_ints(ints):
    return [i for i in ints if not i % 2]

def get_odd_ints(ints):
    return [i for i in ints if i % 2]
    
def get_all_ints(ints):
    return list(ints)
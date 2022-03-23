flatlist = []
def flatten(l):
    for e in l:
        if type(e)==list: 
            for item in e:
                flat(i)
        else:
            flatlist.append(e)
    return flat_list

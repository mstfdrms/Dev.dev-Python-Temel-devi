flatlist = []
def flatten(l):
    for e in l:
        if type(e) is list: 
            for item in e:
                flatten(l)
        elif:
            flatlist.append(e)
    return flatlist

dict = {'Peter':'white', 'Ann':'yellow', 'Quinn':'white', 'Ledo':'red', 'Selena':'pink'}
def reverseLookup(dict,v):
    out = list()
    for k in dict:
        if dict[k] == v:
            out.append(k)
    return out
print(reverseLookup(dict,'white'))
print(reverseLookup(dict,'yellow'))
print(reverseLookup(dict,'black'))

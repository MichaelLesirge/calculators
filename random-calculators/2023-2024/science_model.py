import itertools

keys = {"1s": 1, "2s" : 1, "2p": 3, "3s": 1, "3p": 3, "3s": 1, "3d": 5}

electrons = int(input("Number of elections: "))
order = (list(keys.keys()))

dict = {}

down = "↓"
up = "↑"

section = 0

ups, downs = [], []
while electrons > 0:
    size = keys[order[section]]
    
    if len(ups) < size:
        ups.append(up)
        electrons -= 1
    elif len(downs) < size:
        downs.append(down)
        electrons -= 1
    else:
        dict[order[section]] = (ups, downs)
        ups, downs = [], []
        section += 1
        
dict[order[section]] = (ups, downs)

print("\n".join([key + ": " + (" ".join(["".join(place) for place in itertools.zip_longest(*value, fillvalue="")])) for key, value in dict.items()]))
import json

with open('airlines.csv', 'r') as f:
    d = {}
    count, val = 0, 0
    for line in f:
        each = line.split(',')
        if each[1] == "Airport.Name":
            continue
        each = each[1] + "," + each[2]
        if each in d:
            d[each]+=1
        else:
            d[each] = 1
    Keymax = max(d, key=d.get) 
    Keymin = min(d, key=d.get)
    final_d = {Keymax.replace('"',''):d[Keymax], Keymin.replace('"',''):d[Keymin]}
    final = json.dumps(final_d)
    print(final)

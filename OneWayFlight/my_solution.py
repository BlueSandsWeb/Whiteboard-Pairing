def reconstructTrip(trip):
    tickets = {}
    for ticket in trip:
        tickets[ticket[0]] = ticket[1]
    key = "None"
    arr = []
    for i in range(len(tickets)):
        key = tickets[key]
        arr.append(key)
    return arr


tickets = [
    ['PIT', 'ORD'],
    ['XNA', 'CID'],
    ['SFO', 'BHM'],
    ['FLG', 'XNA'],
    ["None", 'LAX'], 
    ['LAX', 'SFO'],
    ['CID', 'SLC'],
    ['ORD', "None"],
    ['SLC', 'PIT'],
    ['BHM', 'FLG'],
  ];

print(reconstructTrip(tickets))
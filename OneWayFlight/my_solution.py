def reconstructTrip(trip):
    tickets = {}
    for ticket in trip:
        tickets[ticket[0]] = ticket[1]
    # print(tickets)
    key = "None"
    value = ''
    arr = []
    for i in range(len(tickets)):
        value = tickets[key]        // LAX, BHM
        key = tickets[value]        // SFO, 
        arr.append(value)
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
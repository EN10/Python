table = []

row = ["coke",1.5]
table.append(row)

row2 = ["pepsi",0.8]
table.append(row2)

row3 = ["7up",1.2]
table.append(row3)

print(sorted(table,key=lambda t:t[1]))

from prettytable import PrettyTable

Table = PrettyTable(["Name","Age","Occupation"])

Table.add_row(["A","12","student"])
Table.add_row(["B","24","Coder"])
Table.add_row(["C"," 30","Hacker"])

print(Table)
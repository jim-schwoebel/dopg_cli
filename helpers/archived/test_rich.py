# ------------------------------------------------ # 
## FOR LATER ##
# ------------------------------------------------ # 

# FUTURE 
    # if no databases, ask if user would like to create one (at lowest slug plan)?
        # what region?
        # what slug type?
        # multi-node?
        # -> pgcli will be configured to this in the future.

# # class for database from uuid
# class Database:
#   def __init__(self, name, date):
#     self.name = name
#     self.date = date
#     self.version = '14'

# get environment variables from setting.json 
# db = Database('sample', datetime.datetime.now())

import os, json, random, time
from rich import print_json
from rich.console import Console
from rich.table import Table


output=open('output.txt').read().split('\n')

## initialize table
console = Console()
table = Table(show_header=True, header_style="bold magenta")

# table titles
titles=output[0].split('  ')
print(titles)
columns=list()
for title in titles:
	if title=='':
		pass
	else:
		table.add_column(title.title(), style="dim", justify="left")
		columns.append(title.title())

for row in output[1:]:
	row_element=row.split('  ')
	elements=[]
	for element in row_element:
		if element == '':
			pass 
		else:
			elements.append(element.replace(' ',''))

	try:
		if len(columns) == 1:
			table.add_row(elements[0])
		elif len(columns) == 2:
			table.add_row(elements[0], elements[1])
		elif len(columns) == 3:
			table.add_row(elements[0], elements[1], elements[2])
		elif len(columns) == 4:
			table.add_row(elements[0], elements[1], elements[2], elements[3])
		elif len(columns) == 5:
			table.add_row(elements[0], elements[1], elements[2], elements[3], elements[4])
		elif len(columns) == 6:
			table.add_row(elements[0], elements[1], elements[2], elements[3], elements[4], elements[5])
		elif len(columns) == 7:
			table.add_row(elements[0], elements[1], elements[2], elements[3], elements[4], elements[5], elements[6])
		elif len(columns) == 8:
			table.add_row(elements[0], elements[1], elements[2], elements[3], elements[4], elements[5], elements[6], elements[7])
		elif len(columns) == 9:
			table.add_row(elements[0], elements[1], elements[2], elements[3], elements[4], elements[5], elements[6], elements[7], elements[8])
		elif len(columns) == 10:
			table.add_row(elements[0], elements[1], elements[2], elements[3], elements[4], elements[5], elements[6], elements[7], elements[8], elements[9])
	except:
		pass
		
console.print(table)
'''
 __  __  __  __  __  __  __  __  __  __  __  __  __  __  __  __  __ 
																																	
 _____   ____                 _____ _      _____ 
|  __ \ / __ \               / ____| |    |_   _|
| |  | | |  | |_ __   __ _  | |    | |      | |  
| |  | | |  | | '_ \ / _` | | |    | |      | |  
| |__| | |__| | |_) | (_| | | |____| |____ _| |_ 
|_____/ \____/| .__/ \__, |  \_____|______|_____|
			  | |     __/ |                      
			  |_|    |___/                       

									  _                                   
 /\    _   |_|_  _  _    _|. _ _ |_  (_ _  _   _|. _ .|_ _ | _  _ _ _  _  
/--\  |_)\/|_| )(_)| )  (_||(-| )|_  | (_)|   (_||(_)||_(_||(_)(_(-(_|| ) 
	  |  /                                        _/                      
									  
 _  _  _|_ _  _ _ _   _|    _|_ _ _ _ 
|_)(_)_)|_(_)| (-_)  (_||_|_)|_(-| _) 
|         _/                                                                                       
 __  __  __  __  __  __  __  __  __  __  __  __  __  __  __  __  __ 

The meat of the code where we convert doctl responses or API responses into 
nice rich-formatted outputs using the stdout from the terminal and reinjecting 
it back as a nicely formatted output.

Note that we also execute the following commands to help navigate creating and 
maintaining database clusters:

--query - to connect to query a database specified in settings.json
--pricing - to pull up pricing 
--docs - to pull up product docs

Links in case they are useful:
- pricing - https://www.digitalocean.com/pricing/managed-databases
- api docs - https://docs.digitalocean.com/reference/api/api-reference/#tag/Databases
- doctl docs - https://docs.digitalocean.com/reference/doctl/reference/databases/
'''
import os, json, random, time, sys, requests, click, re, ast
from rich import print_json
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from rich.columns import Columns
from rich.panel import Panel
from rich.markdown import Markdown
import webbrowser, readline, markdownify

# ------------------ < helpers below > ---------------------------- #

def input_with_prefill(prompt: str, text: str) -> str:
	'''
		Allows for a preformatted input form so that users type less when issuing doctl commands.
		e.g. 'doctl databases ' vs. '' for initial input response

		This should help improve the user experience if users need to type many times doctl commands.
	'''
	def hook():
		readline.insert_text(text)
		readline.redisplay()
	readline.set_pre_input_hook(hook)
	result = input(prompt)
	readline.set_pre_input_hook()
	return result

def markdownfromurl(url: str):
	'''
		Allows from markdown to be rendered using the requests library in python from a URL.
		Useful if we are pulling readmes online for various integrations.

		Docs: https://rich.readthedocs.io/en/stable/markdown.html
	'''
	r = requests.get(url)
	html = r.text
	h = markdownify.markdownify(html, heading_style="ATX")
	console = Console()
	markdown = Markdown(h)
	console.print(markdown)

# helper for markdown from url
def markdownfromtext(text: str):
	'''
		Allows you to take a string input and convert to markdown.
		Docs: https://rich.readthedocs.io/en/stable/markdown.html
		
		Example:
		--------------------
		MARKDOWN = """
		# This is an h1

		Rich can do a pretty *decent* job of rendering markdown.

		1. This is a list item
		2. This is another list item
		"""
		markdownfromtext(MARKDOWN)
		--------------------
	'''
	h = markdownify.markdownify(text, heading_style="ATX")
	console = Console()
	markdown = Markdown(h)
	console.print(markdown)

def open_url(url: str):
	'''
		Quick function to open url links in a new webbrowser tab.
	'''
	os.system('python3 -m webbrowser -t "%s"'%(url))

def doctl_make_bold(text: str) -> str:
	'''
		Quick way to reformat doctl output on helper screen to make it look nicer.
		Note that this may break as doctl changes, and could be unstable (probably needs reviewed).

		Implemented in October 2022.
	'''
	strings=['backups','connection', 'create', 'db', 'delete', 'firewalls', 'get', 'list', 
			'maintenance-window', 'migrate', 'options', 'pool', 'replica', 'resize', 'sql-mode',
			'user']
	for string in strings:
		# make bold
		text=text.replace('* '+string, '`'+string+'` -')

	stopwords=['doctl','databases','-h', '-t', '-u', '-c', '--context', '--interactive', '-o', '--trace', '-v']
	for stop in stopwords:
		text=text.replace('* '+stop, stop)
	return text

def doctl_output_table(output: str):
	'''
		Given tabular output doctl, takes it in and makes a beautiful table output instead.

		Uses standard formatting for rich columns and rows.

		Docs: https://rich.readthedocs.io/en/stable/tables.html
	'''
	output=output.split('\n')

	## initialize table
	console = Console()
	table = Table(show_header=True, header_style="bold white")

	# table titles
	titles=output[0].split('  ')
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
			if element.replace(' ','') in ['','[]']:
				pass 
			else:
				elements.append(element.replace(' ',''))

		try:
			if len(elements)== 0:
				pass
			else:
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



def api_loading_screen(message_1: str="Getting response", message_2: str= "Received response", spinner_1: str="material", spinner_2: str="hearts", immediate_response: bool=False):
	'''
		This function creates a nice waiting screen with Rich text editor for api responses.

		Note can addapt the spinner_1 and spinner_2 arguments with the rich documentation 
		(see python3 -m rich.spinner).

		If you want to skip the loading screen completely, just call this function with immediate_response == True

		https://rich.readthedocs.io/en/stable/reference/status.html
		https://www.brianlinkletter.com/2021/03/using-python-rich-library-status-module/
	'''
	if immediate_response == False:
		console = Console()
		with console.status("[bold white] %s..."%(message_1), spinner=spinner_1) as status:
			time.sleep(2)
			status.update("[bold blue] %s, rendering..."%(message_2), spinner=spinner_2)
			time.sleep(1)
	else: 
		pass 

def get_json_files(path: str) -> list:
	'''
		Get a sorted list of json files in a current directory
	'''
	listdir=os.listdir(path)
	jsonfiles=list()
	for file in listdir:
		if file.endswith('.json'): 
			jsonfiles.append(file)
	return sorted(jsonfiles)

def get_routes(jsonfiles: list) -> [list, list]:
	'''
		Get a sorted list of api routes from json file names.

		Output in 2 forms: snake case or camelcase 

		https://stackoverflow.com/questions/33945261/how-to-specify-multiple-return-types-using-type-hints
	'''
	snake_cases=list()
	camel_cases=list()
	for jsonfile in jsonfiles:
		route=jsonfile.replace('.json','')
		snake_cases.append(route)
		camel_cases.append(snake_to_camel(route))
	return snake_cases, camel_cases

def camel_to_snake(name: str) -> str:
	'''
		Some basic regular expression to convert camel case to snake case.

		https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
	'''
	name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
	return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

def snake_to_camel(name: str) -> str:
	'''
		Some basic regular expressions to convert snake case to camel case.

		Note this function matters more because all .json files are in snake case at default.

		https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
	'''
	name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
	name = re.sub('__([A-Z])', r'_\1', name)
	name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
	return name.lower()


# confirm all the k/v pairs of the payload (an abstracted way to do this)
def payload_confirm(payload: dict) -> dict:
	click.echo(click.style('This api route requires a payload - please confirm the defaults that follow \n', bold=True, fg='white'))

	# advanced config has a nested dictionary so need to account for this
	advanced_config = False 
	if list(payload) == ['config']:
		payload=payload['config']
		advanced_config = True 

	migration = False 
	if list(payload) == ['source', 'disable_ssl']:
		payload=payload['source']
		migration=True 

	# now go through and get payload via user settings
	keys=list(payload)
	values=list(payload.values())
	for i in range(len(keys)):
		payload_input=input_with_prefill('\n\nwhat is the %s? (%s)\n'%(str(keys[i]), str(type(values[i]))), str(values[i]))
		if payload_input == values[i]:
			pass 
		else:
			
			if type(values[i]) != str:
				# converts the type to the right type based in payload schema in json
				# deal withs all alt types https://www.w3schools.com/python/python_datatypes.asp 
				if type(values[i]) == int:
					payload_input=int(payload_input)
				elif type(values[i]) == float:
					payload_input=float(payload_input)
				elif type(values[i]) in [list, tuple, dict]:
					# from https://www.geeksforgeeks.org/python-convert-a-string-representation-of-list-into-list/
					payload_input=ast.literal_eval(payload_input)
				elif type(values[i]) == bool:
					payload_input=bool(payload_input)

			payload[keys[i]]=payload_input

	if advanced_config == True:
		payload={"config": payload}
	if migration == True:
		payload={"source": payload, "disable_ssl": False} 
		
	return payload

def tabulate_api_endpoints(api_dir: str):
	os.chdir(api_dir)
	listdir=sorted(os.listdir(api_dir))
	routes=list()

	## initialize table
	console = Console()
	table = Table(show_header=True, header_style="bold white")

	columns=['route', 'description', 'method', 'sample', 'payload']
	for column in columns:
		table.add_column(column.title(), style="dim", justify="left")

	for file in listdir:
		if file.endswith('.json'):
			try:
				file_data=json.dumps(open(file).read())
				data=str(json.loads(file_data))
				data=ast.literal_eval(data)
				table.add_row(file.replace('.json',''), str(data['description'])+'\n\n', str(data['method']), str(data['sample']), str(data['payload']))
			except:
				print(file)
	console.print(table)

# ------------------ ^ helpers above ^ ---------------------------- #

## API commands - https://docs.digitalocean.com/reference/api/api-reference/
def get_response(command: str, settings: dict, route: str):
	'''
	# DOCTL commands for databases (assuming you set this up)
	'''
	if command=='doctl':
		# spawn a window to show doctl commands 

		# could output this to markdown
		os.system('doctl databases > output.txt')
		output=open('output.txt').read().replace('\n ','\n- *')
		output=doctl_make_bold(output)
		markdownfromtext(output)

		# now get input
		doctl_input=input_with_prefill('\n\nwhat command do you want to use?\n', 'doctl databases ')
		os.system(doctl_input + '> output.txt')

		# need to process when there is an error or not 
		output=open('output.txt').read()

		if output.startswith('Error:') or output=='':
			''' this will just pass the standard error messages through doctl '''
			pass 
		elif doctl_input in ['doctl databases list', 'doctl databases options regions', 'doctl databases options slugs --engine pg', 'doctl databases options engines', 'doctl databases options versions --engine pg']:
			''' need a way to determine if the output is a table'''
			# now process output to create beautiful rich tables
			os.system('clear')
			doctl_output_table(output)
		else:
			markdownfromtext(output)

	elif command == 'query':
		'''
			opens up a new session with pgcli, which allows for autocompletion of postgres queries and makes it 
			easy to navigate common postgres commands.
			
			docs: https://github.com/dbcli/pgcli
		'''
		os.system('pgcli %s'%(settings['database_metadata']['connection']['uri']))

	elif command == 'api':
		'''
			Commands relating to querying the digitalocean API directly with an existing API key.
		'''
		curdir=os.getcwd()
		api_dir=curdir+'/api'
		# get all routes from jsonfile names 
		jsonfiles=get_json_files(api_dir)
		snake_cases, camel_cases=get_routes(jsonfiles)

		if route in snake_cases or route in camel_cases:
			# multiple levels of abstraction to reduce # of lines of codes just with some json configs
			if route in camel_cases:
				route=camel_to_snake(route)
			jsonfile=route+'.json'
			# get curl commands 
			data=json.load(open(curdir+'/api/'+jsonfile))
			curl=data['sample']
			payload=data['payload']
			# check if data requires a payload, if so use default api doc payloads and confirm with user
			if route in ['retrieve_read_replica', 'destroy_read_replica']:
				# ask user for replica name by calling list read replicas endpoint (could make this look better by loading output json instead)
				os.system('python3 cli.py --command api --route list_read_replicas')
				replica_name=input('what is the replica name? (listed above)\n')
				curl=curl.replace('$DIGITALOCEAN_TOKEN', settings['api_token']).replace('$DATABASE_UUID',settings['database_metadata']['id']).replace('$DATABASE_REPLICA_NAME',replica_name)+' &>/dev/null > api_response.json' 
			elif route in ['retrieve_database_user', 'remove_database_user', 'reset_database_user']:
				os.system('python3 cli.py --command api --route list_database_users')
				database_user=input('what is the database username? (listed above)\n')
				curl=curl.replace('$DIGITALOCEAN_TOKEN', settings['api_token']).replace('$DATABASE_UUID',settings['database_metadata']['id']).replace('$DATABASE_USER',database_user)+' &>/dev/null > api_response.json' 
			elif route in ['retrieve_database', 'delete_database']:
				os.system('python3 cli.py --command api --route list_all_databases')
				database_name=input('what is the database name? (listed above)\n')
				curl=curl.replace('$DIGITALOCEAN_TOKEN', settings['api_token']).replace('$DATABASE_UUID',settings['database_metadata']['id']).replace('$DATABASE_NAME',database_name)+' &>/dev/null > api_response.json' 		
			elif route in ['retrieve_connection_pool', 'delete_connection_pool']:
				os.system('python3 cli.py --command api --route list_connection_pools')
				connection_pool_name=input('what is the connection pool name? (listed above)\n')
				curl=curl.replace('$DIGITALOCEAN_TOKEN', settings['api_token']).replace('$DATABASE_UUID',settings['database_metadata']['id']).replace('$CONNECTION_POOL_NAME',connection_pool_name)+' &>/dev/null > api_response.json' 
			elif payload == {}:
				curl=curl.replace('$DIGITALOCEAN_TOKEN', settings['api_token']).replace('$DATABASE_UUID',settings['database_metadata']['id'])+' &>/dev/null > api_response.json'
			else:
				payload=payload_confirm(payload)
				# print(payload) - testing
				curl=curl.replace('$DIGITALOCEAN_TOKEN', settings['api_token']).replace('$DATABASE_UUID',settings['database_metadata']['id']).replace('$PAYLOAD',str(json.dumps(payload)))+' &>/dev/null > api_response.json'
			
			print(curl) # for testing
			os.system(curl)
			# get response (.json) and pretty print (this is cached in './api_response.json')
			api_loading_screen()
			# for immediate responses, change above line to: 
			# 		api_loading_screen(immediate_response=True)
			try:
				response=json.load(open('api_response.json'))
			except:
				response={"curl": curl,
						  "message": "no response"}
				jsonfile=open('api_response,json','w')
				json.dump(response,jsonfile)
				jsonfile.close()
			print_json(data=response)
		elif route == 'help':
			tabulate_api_endpoints(api_dir)
		else:
			click.echo(click.style('You have supplied an invalid api command (check the table below) \n', bold=True, fg='red'))
			
	elif command=='pricing':			  
		# pricing
		url = 'https://www.digitalocean.com/pricing/managed-databases'
		open_url(url)
		# markdownfromurl(url)
		return ''

	elif command=='docs':
		url='https://docs.digitalocean.com/reference/doctl/reference/databases/'
		open_url(url)
		url='https://docs.digitalocean.com/reference/api/api-reference/#tag/Databases'
		open_url(url)
		# markdownfromurl(url)
		return ''

	elif command == 'benchmark':
		# use standard benchmark on a database
		pass 

	elif command == 'test':
		# smoke test on the database 
		pass 
		
## API commands - https://docs.digitalocean.com/reference/api/api-reference/
def get_description(command: str, settings: dict):
	curdir=os.getcwd()
	os.chdir('api')
	if command=='database_options':
		# https://api.digitalocean.com/v2/databases/options
		route=json.load(open('database_options.json'))
	elif command=='database_list':
		# https://api.digitalocean.com/v2/databases
		route=json.load(open('database_list.json'))
	print_json(data=route)
	os.chdir(curdir)

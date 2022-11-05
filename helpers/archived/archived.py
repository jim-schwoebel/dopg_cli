		if route=='ListDatabaseOptions':
			# ['GET'] - https://api.digitalocean.com/v2/databases/options
			route=json.load(open('all_database_options.json'))['sample']

		elif route=='ListAllDatabaseClusters':
			# ['GET'] - https://api.digitalocean.com/v2/databases
			route=json.load(open('all_database_list.json'))['sample']

		elif route=='CreateANewDatabaseCluster':
			# just show some visual as to what migration could look like with statuses
			with Progress() as progress:

				task2 = progress.add_task("[green]Creating database... :shark:", total=100)

				while not progress.finished:
					progress.update(task2, advance=0.5)
					time.sleep(0.02)

			directories = ['Users', 'Organizations', 'Transactions', 'Messages']
			renderables = [Panel(directory) for directory in directories]
			console.print(Columns(renderables))
			route=''
			# elif command=='database_create':
			# 	# ['POST'] - 'https://api.digitalocean.com/v2/databases'
			# 	while prompt not in ['y','yes','no','n']:
			# 		prompt=input("Are these the settings you want? Yes (Y) or No (N) \n\n %s"%(str(settings['default_database_create'])))
			# 		if prompt.lower() in ['yes', 'y']:
			# 			name=input("what is the name of the cluster? (e.g. 'test-db')")
			# 			if name == '':
			# 				name='test-db'
			# 			database_create_settings['name']=name
			# 			break 
			# 		elif prompt.lower() in ['no', 'n']:
			# 			# doct strings
			# 			break
			# 	route=json.load(open('database_create.json'))['sample'].replace('$DATABASE_CREATE_SETTINGS',database_create_settings)


		elif route=='migrate':
			# just show some visual as to what migration could look like with statuses
			with Progress() as progress:

				task1 = progress.add_task("[red]Checking database... :shark:", total=100)
				task2 = progress.add_task("[green]Uploading database... :shark:", total=100)
				task3 = progress.add_task("[cyan]Migrating database... :shark:", total=100)

				while not progress.finished:
					progress.update(task1, advance=0.5)
					progress.update(task2, advance=0.3)
					progress.update(task3, advance=0.9)
					time.sleep(0.02)
			directories = ['Users', 'Organizations', 'Transactions', 'Messages']
			renderables = [Panel(directory) for directory in directories]
			console.print(Columns(renderables))
			return ''

		elif route=='database_options':
				with console.status("[bold white] Getting all database options...", spinner="material") as status:
					# status indictor https://www.brianlinkletter.com/2021/03/using-python-rich-library-status-module/
					# python3 -m rich.spinner
					time.sleep(2)
					route=json.load(open('database_options.json'))['sample']
					status.update("[bold blue] Received options, rendering...", spinner="hearts")
					time.sleep(1)

		command=route.replace('$DIGITALOCEAN_TOKEN', settings['api_token'])+' &>/dev/null > api_response.json'
		os.system(command)
		response=json.load(open('api_response.json'))
		print_json(data=response)
		os.chdir(curdir)

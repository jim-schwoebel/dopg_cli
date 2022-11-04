import os, click, rich, json, datetime, time
from rich.console import Console
from rich.table import Table

def reload():
    # setup the CLI properly using an existing digitalocean API token.
    valid_key = False

    while valid_key == False:
        api_token = click.prompt(click.style('what is your digitalocean api token', fg='cyan'), type=str,  hide_input=True)
        # test api key in a basic way
        command="curl -X GET -H 'Content-Type: application/json' -H 'Authorization: Bearer %s' 'https://api.digitalocean.com/v2/databases' &>/dev/null > databases.json"%(api_token)
        os.system(command)
        databases=json.load(open('databases.json'))
        if list(databases) == ['databases']:
            valid_key = True
        else:
            print(databases)
            click.echo(click.style('You have supplied an invalid api token \n', bold=True, fg='red'))

    # now show a nice table in rich on available databases 
    ids=list()
    names=list()
    engines=list()
    versions=list()

    columns=['id', 'name', 'database', 'versions']

    ## initialize table
    console = Console()
    table = Table(show_header=True, header_style="bold white")
    for column in columns:
        table.add_column(column.title(), style="dim", justify="left")

    for database in list(databases['databases']):
        if database['engine'] == 'pg':
            ids.append(database['id'])
            names.append(database['name'])
            engines.append(database['engine'])
            versions.append(database['version'])
            table.add_row(database['id'], database['name'], database['engine'], database['version'])
        else:
            # skip the engine with black ids or names
            ids.append('[]')
            names.append('[]')
            engines.append('[]')
            versions.append('[]')

    console.print(table)

    # which database would you like to pair with the CLI?
    
    in_ids=False
    while in_ids == False:
        input_ = click.prompt(click.style('which database (uuid or name) would you like to pair with the cli?', fg='cyan'), type=str)
        if input_ in ids:
            in_ids=True 
            index=ids.index(input_)
        elif input_ in names:
            in_ids=True 
            index=names.index(input_)   
        else:
            click.echo(click.style('You have supplied an invalid database name or id (check the table below) \n', bold=True, fg='red'))
            console.print(table)

    # only take the listed database 
    settings={"api_token": api_token,
              "database_metadata": databases['databases'][index]}
    jsonfile=open('settings.json','w')
    json.dump(settings,jsonfile)
    jsonfile.close()
    click.echo(click.style('\n\n✅ Congrats! You are ready to go. \n', bold=True, fg='white'))

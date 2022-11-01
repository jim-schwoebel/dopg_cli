# DOpg: a python client for DigitalOcean postgres clusters
```
 _____   ____                 _____ _      _____ 
|  __ \ / __ \               / ____| |    |_   _|
| |  | | |  | |_ __   __ _  | |    | |      | |  
| |  | | |  | | '_ \ / _` | | |    | |      | |  
| |__| | |__| | |_) | (_| | | |____| |____ _| |_ 
|_____/ \____/| .__/ \__, |  \_____|______|_____|
              | |     __/ |                      
              |_|    |___/                       
```

🦈 An unofficial python client for digitalocean postgres clusters (5+ integrations).

Uses [click](https://click.palletsprojects.com/en/8.1.x/) and [rich](https://github.com/Textualize/rich) to create beautiful command line interactions for postgres databases. 

## setup (<3 minutes)
First, install python3 and doctl [using homebrew](https://brew.sh/).
```
brew install python3, doctl
```
Next, install python dependencies within a virtual environment
```
git clone 
cd 
virtualenv env 
source env/bin/activate
pip3 install -r requirements.txt
```
Next, you can setup the cli (you will need your api key and must have already created a managed database postgres instance).
```
python3 cli.py
```
After this, you will see ```settings.json``` and ```databases.json``` in your dopg_cli directory that will be used to configure all the commands that follow. 

## commands 
There are 3 main ways to use the DOpg CLI client, sectioned out below.

### query databases
Connects with BSD-licensed [pgcli](https://github.com/dbcli/pgcli), a really nice interface to connect to postgres and query postgres databases.

### doctl commands
[doctl](https://github.com/digitalocean/doctl) is the python command line interface.

More on doctl database docs here.

You can also get doctl docs using (pulls up doctl and api docs).
```
python3 cli.py --command docs
```

### api commands
[The DigitalOcean API](https://docs.digitalocean.com/reference/api/api-reference/#tag/Databases) is a great way to get json responses from common routes related to databases.

You can also get doctl docs using (pulls up doctl and api docs).
```
python3 cli.py --command docs
```

### pricing
You can get pricing of managed databases within digitalocean using public links:
```
python3 cli.py --command pricing
```

### test 
You can do some smoke tests on newly created databases with the following command:
```
python3 cli.py --command tests
```

This command opens up a postgres cluster, inserts a users schema, and inserts a few pieces of data, reads this data, then deletes this data and schema. If tests passed they will be shown using the [unittest module](https://docs.python.org/3/library/unittest.html) in python.

## references
Here are some additional (python-centric) references that may help you as you learn PostgresSQL, as a beginner or an expert:

* [postgres14 features](https://severalnines.com/blog/best-new-features-in-postgresql-14) - why use postgres14 over postgres13
* [api docs](https://docs.digitalocean.com/reference/api/api-reference/#tag/Databases) - api docs with cuRL commands
* [doctl docs](https://github.com/digitalocean/doctl) - the official command line client for digitalocean
* [psycopg2 module](https://zetcode.com/python/psycopg2/) - for querying databases in python code
* [pgcli](https://www.pgcli.com/) - command line interface for postgres 
* [click](https://click.palletsprojects.com/en/8.1.x/) - click CLI docs
* [rich](https://github.com/Textualize/rich) - a Python library for rich text and beautiful formatting in the terminal.
* [sqlalchemy](https://www.sqlalchemy.org/) - database toolkit for python
* [pgloader](https://github.com/dimitri/pgloader) - migrate to PostgreSQL in a single command
* [asyncpg](https://github.com/MagicStack/asyncpg) - a fast PostgreSQL Database Client Library for Python/asyncio
* [flask-migrate](https://github.com/miguelgrinberg/Flask-Migrate) - database migrations in flask

<p align="center"><img src="https://github.com/jim-schwoebel/dopg_cli/blob/main/assets/logo.png" alt="logo" width="300"></img></p>
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
&nbsp;
[![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)](https://github.com/jim-schwoebel/allie/blob/master/Dockerfile)
[![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/jim-schwoebel/allie/blob/master/requirements.txt)
[![GitHub Issues](https://img.shields.io/github/issues/anfederico/Clairvoyant.svg)](https://github.com/jim-schwoebel/allie/issues)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)](https://github.com/jim-schwoebel/allie/projects)
[![License](https://img.shields.io/badge/license-Apache%202-blue)](https://www.apache.org/licenses/LICENSE-2.0.html)

🦈 An unofficial python client for digitalocean postgres clusters (5+ integrations).

Uses [click](https://click.palletsprojects.com/en/8.1.x/) and [rich](https://github.com/Textualize/rich) to create beautiful command line interactions for postgres databases. 

## MacOS setup (<3 minutes)
This first version has only been tested on MacOS.

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
🐍 **Python modules** that may help you as you build PostgreSQL applications, as a beginner or an expert:
* [asyncpg](https://github.com/MagicStack/asyncpg) - a fast PostgreSQL Database Client Library for Python/asyncio
* [click](https://click.palletsprojects.com/en/8.1.x/) - click CLI docs
* [flask-migrate](https://github.com/miguelgrinberg/Flask-Migrate) - database migrations in flask
* [marshmellow](https://marshmallow.readthedocs.io/en/stable/) - schemas in python
* [psycopg2 module](https://zetcode.com/python/psycopg2/) - for querying databases in python code
* [pgcli](https://www.pgcli.com/) - command line interface for postgres 
* [pgloader](https://github.com/dimitri/pgloader) - migrate to PostgreSQL in a single command
* [rich](https://github.com/Textualize/rich) - a Python library for rich text and beautiful formatting in the terminal.
* [sqlalchemy](https://www.sqlalchemy.org/) - database toolkit for python
* [unittest](https://docs.python.org/3/library/unittest.html) - unit testing in python

🐘 **Standard postgres references** that may help you:
* [postgres](https://www.postgresql.org/) - official postgres website
* [postgres14 features](https://severalnines.com/blog/best-new-features-in-postgresql-14) - why use postgres14 over postgres13

🦈 **DigitalOcean references** that may help you as you use this CLI client:
* [careers page](https://www.digitalocean.com/careers?gh_src=bc47f6b61us) - careers page (we're always hiring!)
* [digitalocean database api docs](https://docs.digitalocean.com/reference/api/api-reference/#tag/Databases) - api docs with cuRL commands
* [doctl docs](https://github.com/digitalocean/doctl) - the official command line client for digitalocean
* [managed databases page](https://www.digitalocean.com/products/managed-databases) - managed databases product page
* [postgres community page](https://www.digitalocean.com/community/tags/digitalocean-managed-postgresql-database) - community page for managed postgresql databases

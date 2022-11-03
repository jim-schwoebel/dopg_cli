# DOpg CLI
<p align="center"><img src="https://github.com/jim-schwoebel/dopg_cli/blob/main/assets/logo.png" alt="logo" width="300"></img></p>
<p align="center"><img src="https://github.com/jim-schwoebel/dopg_cli/blob/main/assets/logo_2.png" alt="logo" width="500"></img></p>

[![Python](https://img.shields.io/badge/python-v3.9+-blue.svg)]()
[![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/anfederico/Clairvoyant.svg)](https://github.com/jim-schwoebel/dopg_cli/issues)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)](https://github.com/jim-schwoebel/dopg_cli/issues)
[![License](https://img.shields.io/badge/license-Apache%202-blue)](https://www.apache.org/licenses/LICENSE-2.0.html)
[![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=Check%20out%20DOpg,%20an%20awesome%20new%20CLI%20framework%20for%20postgres%20on%20@DigitalOcean%20https://github.com/jim-schwoebel/dopg_cli&hashtags=digitalocean,postgres,doctl,do) 
[![Follow me](https://img.shields.io/github/followers/jim-schwoebel?style=social)]([https://jim-schwoebel](https://github.com/jim-schwoebel?tab=followers))
&nbsp;

🦈 An unofficial python client for digitalocean postgres clusters (5+ integrations).

Uses [click](https://click.palletsprojects.com/en/8.1.x/), [pgcli](https://github.com/dbcli/pgcli), and [rich](https://github.com/Textualize/rich) to create beautiful command line interactions for postgres databases. 

You can easily extend this framework to fit your particular use case.

Some things that DOpg can do include:
- [query databases](https://github.com/jim-schwoebel/dopg_cli/blob/main/README.md#query-databases) directly through a nice autocompletion widget 
- cache doctl/api responses (within a cache_limit) so you don't need to log this elsewhere
- get postgres doctl and api docs from DigitalOcean for easy access
- visualize api responses in a more intuitive way (e.g. in tables and pretty printed json)
- benchmark new postgres databases on digitalocean with standard tools
- run smoke tests with commmon commands on your postgres database

## MacOS setup (<3 minutes)
This first version has only been tested on MacOS.

First, install python3 and doctl [using homebrew](https://brew.sh/):
```
brew install python3, doctl
```
Next, install python dependencies within a virtual environment:
```
git clone https://github.com/jim-schwoebel/dopg_cli.git
cd dopg_cli
virtualenv env 
source env/bin/activate
pip3 install -r requirements.txt
```
Next, you can setup the cli (you will need your api key and must have already created a managed database postgres instance):
```
python3 cli.py
```

![](https://github.com/jim-schwoebel/dopg_cli/blob/main/assets/setup.gif)

After this, you will see ```settings.json``` and ```databases.json``` in your dopg_cli directory used to configure all the commands that follow. 

## commands 
There are many ways to use the DOpg CLI client, sectioned out below.

### query databases
```
python3 cli.py --command query
```

Connects with [pgcli](https://github.com/dbcli/pgcli), a really nice interface to connect to postgres and query postgres databases (e.g. with autocompletion).

![](https://github.com/jim-schwoebel/dopg_cli/blob/main/assets/query.gif)

### doctl commands
You can also use [doctl](https://github.com/digitalocean/doctl)'s database commands directly - with a nicely formatted output for tables and other types of data. Note that doctl is the python command line interface for digitalocean.
```
python3 cli.py --command doctl
```

![](https://github.com/jim-schwoebel/dopg_cli/blob/main/assets/doctl.gif)

### api commands
[The DigitalOcean API](https://docs.digitalocean.com/reference/api/api-reference/#tag/Databases) is a great way to get json responses from common routes related to databases.

Put into a table of commands
```
Commands tba
```

![](https://github.com/jim-schwoebel/dopg_cli/blob/main/assets/api.gif)

### docs
You can also get [doctl docs](https://github.com/digitalocean/doctl) and [api docs](https://docs.digitalocean.com/reference/api/api-reference/#tag/Databases) with this command:
```
python3 cli.py --command docs
```

![](https://github.com/jim-schwoebel/dopg_cli/blob/main/assets/docs.gif)

### pricing
You can get pricing of managed databases within digitalocean using public links:

```
python3 cli.py --command pricing
```

![](https://github.com/jim-schwoebel/dopg_cli/blob/main/assets/pricing.gif)

### benchmarking
WIP - working on adding benchmarking for your configured postgres database:

```
python3 cli.py --command benchmark
```
```diff
- Note: you should probably only use this on a newly created database.
```

### tests
You can do some smoke tests on newly created databases with the following command:

```
python3 cli.py --command tests
```
```diff
- Note: you should probably only use this on a newly created database.
```

This command opens up a postgres cluster, inserts a users schema, and inserts a few pieces of data, reads this data, then deletes this data and schema. If tests passed they will be shown using the [unittest module](https://docs.python.org/3/library/unittest.html) in python.

## references
🐍 **Python modules** that may help you as you build PostgreSQL applications, as a beginner or an expert:
* [asyncpg](https://github.com/MagicStack/asyncpg) - a fast PostgreSQL Database Client Library for Python/asyncio
* [click](https://click.palletsprojects.com/en/8.1.x/) - click CLI docs
* [cr8](https://github.com/mfussenegger/cr8) - benchmarking postgres clusters
* [flask-migrate](https://github.com/miguelgrinberg/Flask-Migrate) - database migrations in flask
* [marshmellow](https://marshmallow.readthedocs.io/en/stable/) - schemas in python
* [psycopg2 module](https://zetcode.com/python/psycopg2/) - for querying databases in python code
* [pgcli](https://www.pgcli.com/) - command line interface for postgres 
* [pgloader](https://github.com/dimitri/pgloader) - migrate to PostgreSQL in a single command
* [rich](https://github.com/Textualize/rich) - a Python library for rich text and beautiful formatting in the terminal
* [sqlalchemy](https://www.sqlalchemy.org/) - database toolkit for python
* [tpch-pgsql](https://github.com/Data-Science-Platform/tpch-pgsql) - implementing the tpch benchmark for postgres databases
* [unittest](https://docs.python.org/3/library/unittest.html) - unit testing in python

🐘 **Standard postgres references** that may help you:
* [pgbench](https://www.postgresql.org/docs/current/pgbench.html) - pgbench can help you benchmark your database
* [postgres](https://www.postgresql.org/) - official postgres website
* [postgres14 features](https://severalnines.com/blog/best-new-features-in-postgresql-14) - why use postgres14 over postgres13

🦈 **DigitalOcean references** that may help you as you use this CLI client:
* [careers page](https://www.digitalocean.com/careers?gh_src=bc47f6b61us) - careers page (we're always hiring!)
* [digitalocean database api docs](https://docs.digitalocean.com/reference/api/api-reference/#tag/Databases) - api docs with cuRL commands
* [doctl docs](https://github.com/digitalocean/doctl) - the official command line client for digitalocean
* [hacktoberfest](https://hacktoberfest.com/) - DigitalOcean's annual hack-a-thon in October every year (open to anyone)
* [managed databases page](https://www.digitalocean.com/products/managed-databases) - managed databases product page
* [postgres community page](https://www.digitalocean.com/community/tags/digitalocean-managed-postgresql-database) - community page for managed postgresql databases

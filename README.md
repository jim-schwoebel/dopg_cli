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
- visualize api responses in an intuitive and beautiful way (e.g. in tables and pretty printed json)
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

To get a tabular list of possible commands, follow:
```
python3 cli.py --command api --route help
```
And it should output something like:
```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Route                                               ┃ Description                                             ┃ Method ┃ Sample                                                  ┃ Payload                                                 ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ list_all_database_clusters                          │ To list all of the database clusters available on your  │ GET    │ curl -X GET -H 'Content-Type: application/json' -H      │ {}                                                      │
│                                                     │ account, send a GET request to /v2/databases. To limit  │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'             │                                                         │
│                                                     │ the results to database clusters with a specific tag,   │        │ 'https://api.digitalocean.com/v2/databases'             │                                                         │
│                                                     │ include the tag_name query parameter set to the name of │        │                                                         │                                                         │
│                                                     │ the tag. For example, /v2/databases?tag_name=$TAG_NAME. │        │                                                         │                                                         │
│                                                     │ The result will be a JSON object with a databases key.  │        │                                                         │                                                         │
│                                                     │ This will be set to an array of database objects, each  │        │                                                         │                                                         │
│                                                     │ of which will contain the standard database attributes. │        │                                                         │                                                         │
│                                                     │ The embedded connection and private_connection objects  │        │                                                         │                                                         │
│                                                     │ will contain the information needed to access the       │        │                                                         │                                                         │
│                                                     │ database cluster: The embedded maintenance_window       │        │                                                         │                                                         │
│                                                     │ object will contain information about any scheduled     │        │                                                         │                                                         │
│                                                     │ maintenance for the database cluster.                   │        │                                                         │                                                         │
│                                                     │                                                         │        │                                                         │                                                         │
│                                                     │                                                         │        │                                                         │                                                         │
│ list_database_options                               │ To list all of the options available for the offered    │ GET    │ curl -X GET -H 'Content-Type: application/json' -H      │ {}                                                      │
│                                                     │ database engines, send a GET request to                 │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'             │                                                         │
│                                                     │ /v2/databases/options. The result will be a JSON object │        │ 'https://api.digitalocean.com/v2/databases'             │                                                         │
│                                                     │ with an options key.                                    │        │                                                         │                                                         │
│                                                     │                                                         │        │                                                         │                                                         │
│                                                     │                                                         │        │                                                         │                                                         │
│ destroy_a_database_cluster                          │ To destroy a specific database, send a DELETE request   │ DEL    │ curl -X DELETE -H 'Content-Type: application/json' -H   │ {}                                                      │
│                                                     │ to /v2/databases/$DATABASE_ID. A status of 204 will be  │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'             │                                                         │
│                                                     │ given. This indicates that the request was processed    │        │ 'https://api.digitalocean.com/v2/databases/$DATABASE_U… │                                                         │
│                                                     │ successfully, but that no response body is needed.      │        │                                                         │                                                         │
│                                                     │                                                         │        │                                                         │                                                         │
│                                                     │                                                         │        │                                                         │                                                         │
│ stop_an_online_migration                            │ To stop an online migration, send a DELETE request to   │ DEL    │ curl -X DELETE -H 'Content-Type: application/json' -H   │ {}                                                      │
│                                                     │ /v2/databases/$DATABASE_ID/online-migration/$MIGRATION… │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'             │                                                         │
│                                                     │ A status of 204 will be given. This indicates that the  │        │ 'https://api.digitalocean.com/v2/databases/$DATABASE_U… │                                                         │
│                                                     │ request was processed successfully, but that no         │        │                                                         │                                                         │
│                                                     │ response body is needed.                                │        │                                                         │                                                         │
│                                                     │                                                         │        │                                                         │                                                         │
│                                                     │                                                         │        │                                                         │                                                         │
│ retrieve_an_existing_database_cluster_configuration │ Shows configuration parameters for an existing database │ GET    │ curl -X GET -H 'Content-Type: application/json' -H      │ {}                                                      │
│                                                     │ cluster by sending a GET request to                     │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'             │                                                         │
│                                                     │ /v2/databases/$DATABASE_ID/config. The response is a    │        │ 'https://api.digitalocean.com/v2/databases/$DATABASE_U… │                                                         │
│                                                     │ JSON object with a config key, which is set to an       │        │                                                         │                                                         │
│                                                     │ object containing any database configuration            │        │                                                         │                                                         │
│                                                     │ parameters.                                             │        │                                                         │                                                         │
│                                                     │                                                         │        │                                                         │                                                         │
│                                                     │                                                         │        │                                                         │                                                         │
│ create_a_new_database_cluster                       │ To create a database cluster, send a POST request to    │ POST   │ curl -X POST -H 'Content-Type: application/json' -H     │ {'name': 'backend-test', 'engine': 'pg', 'version':     │
│                                                     │ /v2/databases. The response will be a JSON object with  │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN' -d          │ '14', 'region': 'nyc3', 'size': 'db-s-2vcpu-4gb',       │
│                                                     │ a key called database. The value of this will be an     │        │ '$PAYLOAD' 'https://api.digitalocean.com/v2/databases'  │ 'num_nodes': 2, 'tags': ['production']}                 │
│                                                     │ object that contains the standard attributes associated │        │                                                         │                                                         │
│                                                     │ with a database cluster. The initial value of the       │        │                                                         │                                                         │
│                                                     │ database cluster's status attribute will be creating.   │        │                                                         │                                                         │
│                                                     │ When the cluster is ready to receive traffic, this will │        │                                                         │                                                         │
│                                                     │ transition to online. The embedded connection and       │        │                                                         │                                                         │
│                                                     │ private_connection objects will contain the information │        │                                                         │                                                         │
│                                                     │ needed to access the database cluster. DigitalOcean     │        │                                                         │                                                         │
│                                                     │ managed PostgreSQL and MySQL database clusters take     │        │                                                         │                                                         │
│                                                     │ automated daily backups. To create a new database       │        │                                                         │                                                         │
│                                                     │ cluster based on a backup of an existing cluster, send  │        │                                                         │                                                         │
│                                                     │ a POST request to /v2/databases. In addition to the     │        │                                                         │                                                         │
│                                                     │ standard database cluster attributes, the JSON body     │        │                                                         │                                                         │
│                                                     │ must include a key named backup_restore with the name   │        │                                                         │                                                         │
│                                                     │ of the original database cluster and the timestamp of   │        │                                                         │                                                         │
│                                                     │ the backup to be restored. Creating a database from a   │        │                                                         │                                                         │
│                                                     │ backup is the same as forking a database in the control │        │                                                         │                                                         │
│                                                     │ panel. Note: Backups are not supported for Redis        │        │                                                         │                                                         │
│                                                     │ clusters.                                               │        │                                                         │                                                         │
│                                                     │                                                         │        │                                                         │                                                         │
│                                                     │                                                         │        │                                                         │                                                         │
│ retrieve_an_existing_database_cluster               │ To show information about an existing database cluster, │ GET    │ curl -X GET -H 'Content-Type: application/json' -H      │ {}                                                      │
│                                                     │ send a GET request to /v2/databases/$DATABASE_ID. The   │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'             │                                                         │
│                                                     │ response will be a JSON object with a database key.     │        │ 'https://api.digitalocean.com/v2/databases/$DATABASE_U… │                                                         │
│                                                     │ This will be set to an object containing the standard   │        │                                                         │                                                         │
│                                                     │ database cluster attributes. The embedded connection    │        │                                                         │                                                         │
│                                                     │ and private_connection objects will contain the         │        │                                                         │                                                         │
│                                                     │ information needed to access the database cluster. The  │        │                                                         │                                                         │
│                                                     │ embedded maintenance_window object will contain         │        │                                                         │                                                         │
│                                                     │ information about any scheduled maintenance for the     │        │                                                         │                                                         │
│                                                     │ database cluster.                                       │        │                                                         │                                                         │
│                                                     │                                                         │        │                                                         │                                                         │
│                                                     │                                                         │        │                                                         │                                                         │
│ migrate_a_database_cluster_to_a_new_region          │ To migrate a database cluster to a new region, send a   │ PUT    │ curl -X PUT -H 'Content-Type: application/json' -H      │ {'region': 'lon1'}                                      │
│                                                     │ PUT request to /v2/databases/$DATABASE_ID/migrate. The  │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN' -d          │                                                         │
│                                                     │ body of the request must specify a region attribute. A  │        │ '$PAYLOAD'                                              │                                                         │
│                                                     │ successful request will receive a 202 Accepted status   │        │ 'https://api.digitalocean.com/v2/databases/$DATABASE_U… │                                                         │
│                                                     │ code with no body in response. Querying the database    │        │                                                         │                                                         │
│                                                     │ cluster will show that its status attribute will now be │        │                                                         │                                                         │
│                                                     │ set to migrating. This will transition back to online   │        │                                                         │                                                         │
│                                                     │ when the migration has completed.                       │        │                                                         │                                                         │
│                                                     │                                                         │        │                                                         │                                                         │
│                                                     │                                                         │        │                                                         │                                                         │
│ retrieve_the_public_certificate                     │ To retrieve the public certificate used to secure the   │ GET    │ curl -X GET -H 'Content-Type: application/json' -H      │ {}                                                      │
│                                                     │ connection to the database cluster send a GET request   │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'             │                                                         │
│                                                     │ to /v2/databases/$DATABASE_ID/ca. The response will be  │        │ 'https://api.digitalocean.com/v2/databases/$DATABASE_U… │                                                         │
│                                                     │ a JSON object with a ca key. This will be set to an     │        │                                                         │                                                         │
│                                                     │ object containing the base64 encoding of the public key │        │                                                         │                                                         │
│                                                     │ certificate.                                            │        │                                                         │                                                         │
│                                                     │                                                         │        │                                                         │                                                         │
│                                                     │                                                         │        │                                                         │                                                         │
└─────────────────────────────────────────────────────┴─────────────────────────────────────────────────────────┴────────┴─────────────────────────────────────────────────────────┴─────────────────────────────────────────────────────────┘
```
And then you can run any of these commands in snake or camel case; for example:
```
python3 cli.py --command api --route list_database_options
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

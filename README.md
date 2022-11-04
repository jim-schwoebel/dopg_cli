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
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Route                                        ┃ Description                                  ┃ Method ┃ Sample                                        ┃ Payload                                      ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ add_connection_pool                          │ For PostgreSQL database clusters, connection │ POST   │ curl -X POST -H 'Content-Type:                │ {'name': 'backend-pool', 'mode':             │
│                                              │ pools can be used to allow a database to     │        │ application/json' -H 'Authorization: Bearer   │ 'transaction', 'size': 10, 'db':             │
│                                              │ share its idle connections. The popular      │        │ $DIGITALOCEAN_TOKEN' -d '$PAYLOAD'            │ 'defaultdb', 'user': 'doadmin'}              │
│                                              │ PostgreSQL connection pooling utility        │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ PgBouncer is used to provide this service.   │        │                                               │                                              │
│                                              │ See here for more information about how and  │        │                                               │                                              │
│                                              │ why to use PgBouncer connection pooling      │        │                                               │                                              │
│                                              │ including details about the available        │        │                                               │                                              │
│                                              │ transaction modes. To add a new connection   │        │                                               │                                              │
│                                              │ pool to a PostgreSQL database cluster, send  │        │                                               │                                              │
│                                              │ a POST request to                            │        │                                               │                                              │
│                                              │ /v2/databases/$DATABASE_ID/pools specifying  │        │                                               │                                              │
│                                              │ a name for the pool, the user to connect     │        │                                               │                                              │
│                                              │ with, the database to connect to, as well as │        │                                               │                                              │
│                                              │ its desired size and transaction mode.       │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ add_database_user                            │ To add a new database user, send a POST      │ POST   │ curl -X POST -H 'Content-Type:                │ {'name': 'app-01'}                           │
│                                              │ request to /v2/databases/$DATABASE_ID/users  │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ with the desired username. Note: User        │        │ $DIGITALOCEAN_TOKEN' -d '$PAYLOAD'            │                                              │
│                                              │ management is not supported for Redis        │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ clusters. When adding a user to a MySQL      │        │                                               │                                              │
│                                              │ cluster, additional options can be           │        │                                               │                                              │
│                                              │ configured in the mysql_settings object. The │        │                                               │                                              │
│                                              │ response will be a JSON object with a key    │        │                                               │                                              │
│                                              │ called user. The value of this will be an    │        │                                               │                                              │
│                                              │ object that contains the standard attributes │        │                                               │                                              │
│                                              │ associated with a database user including    │        │                                               │                                              │
│                                              │ its randomly generated password.             │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ add_new_database                             │ To add a new database to an existing         │ POST   │ curl -X POST -H 'Content-Type:                │ {'name': 'alpha'}                            │
│                                              │ cluster, send a POST request to              │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ /v2/databases/$DATABASE_ID/dbs. Note:        │        │ $DIGITALOCEAN_TOKEN' -d '$PAYLOAD'            │                                              │
│                                              │ Database management is not supported for     │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ Redis clusters. The response will be a JSON  │        │                                               │                                              │
│                                              │ object with a key called db. The value of    │        │                                               │                                              │
│                                              │ this will be an object that contains the     │        │                                               │                                              │
│                                              │ standard attributes associated with a        │        │                                               │                                              │
│                                              │ database.                                    │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ configure_a_database_cluster_maintenance_wi… │ To configure the window when automatic       │ PUT    │ curl -X PUT -H 'Content-Type:                 │ {'day': 'tuesday', 'hour': '14:00'}          │
│                                              │ maintenance should be performed for a        │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ database cluster, send a PUT request to      │        │ $DIGITALOCEAN_TOKEN' -d '$PAYLOAD'            │                                              │
│                                              │ /v2/databases/$DATABASE_ID/maintenance. A    │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ successful request will receive a 204 No     │        │                                               │                                              │
│                                              │ Content status code with no body in          │        │                                               │                                              │
│                                              │ response.                                    │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ create_a_new_database_cluster                │ To create a database cluster, send a POST    │ POST   │ curl -X POST -H 'Content-Type:                │ {'name': 'backend-test', 'engine': 'pg',     │
│                                              │ request to /v2/databases. The response will  │        │ application/json' -H 'Authorization: Bearer   │ 'version': '14', 'region': 'nyc3', 'size':   │
│                                              │ be a JSON object with a key called database. │        │ $DIGITALOCEAN_TOKEN' -d '$PAYLOAD'            │ 'db-s-2vcpu-4gb', 'num_nodes': 2, 'tags':    │
│                                              │ The value of this will be an object that     │        │ 'https://api.digitalocean.com/v2/databases'   │ ['production']}                              │
│                                              │ contains the standard attributes associated  │        │                                               │                                              │
│                                              │ with a database cluster. The initial value   │        │                                               │                                              │
│                                              │ of the database cluster's status attribute   │        │                                               │                                              │
│                                              │ will be creating. When the cluster is ready  │        │                                               │                                              │
│                                              │ to receive traffic, this will transition to  │        │                                               │                                              │
│                                              │ online. The embedded connection and          │        │                                               │                                              │
│                                              │ private_connection objects will contain the  │        │                                               │                                              │
│                                              │ information needed to access the database    │        │                                               │                                              │
│                                              │ cluster. DigitalOcean managed PostgreSQL and │        │                                               │                                              │
│                                              │ MySQL database clusters take automated daily │        │                                               │                                              │
│                                              │ backups. To create a new database cluster    │        │                                               │                                              │
│                                              │ based on a backup of an existing cluster,    │        │                                               │                                              │
│                                              │ send a POST request to /v2/databases. In     │        │                                               │                                              │
│                                              │ addition to the standard database cluster    │        │                                               │                                              │
│                                              │ attributes, the JSON body must include a key │        │                                               │                                              │
│                                              │ named backup_restore with the name of the    │        │                                               │                                              │
│                                              │ original database cluster and the timestamp  │        │                                               │                                              │
│                                              │ of the backup to be restored. Creating a     │        │                                               │                                              │
│                                              │ database from a backup is the same as        │        │                                               │                                              │
│                                              │ forking a database in the control panel.     │        │                                               │                                              │
│                                              │ Note: Backups are not supported for Redis    │        │                                               │                                              │
│                                              │ clusters.                                    │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ create_a_read_replica                        │ To create a read-only replica for a          │ POST   │ curl -X POST -H 'Content-Type:                │ {'name': 'read-nyc3-01', 'region': 'nyc3',   │
│                                              │ PostgreSQL or MySQL database cluster, send a │        │ application/json' -H 'Authorization: Bearer   │ 'size': 'db-s-2vcpu-4gb'}                    │
│                                              │ POST request to                              │        │ $DIGITALOCEAN_TOKEN' -d '$PAYLOAD'            │                                              │
│                                              │ /v2/databases/$DATABASE_ID/replicas          │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ specifying the name it should be given, the  │        │                                               │                                              │
│                                              │ size of the node to be used, and the region  │        │                                               │                                              │
│                                              │ where it will be located. Note: Read-only    │        │                                               │                                              │
│                                              │ replicas are not supported for Redis         │        │                                               │                                              │
│                                              │ clusters. The response will be a JSON object │        │                                               │                                              │
│                                              │ with a key called replica. The value of this │        │                                               │                                              │
│                                              │ will be an object that contains the standard │        │                                               │                                              │
│                                              │ attributes associated with a database        │        │                                               │                                              │
│                                              │ replica. The initial value of the read-only  │        │                                               │                                              │
│                                              │ replica's status attribute will be forking.  │        │                                               │                                              │
│                                              │ When the replica is ready to receive         │        │                                               │                                              │
│                                              │ traffic, this will transition to active.     │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ delete_connection_pool                       │ To delete a specific connection pool for a   │ DEL    │ curl -X DELETE -H 'Content-Type:              │ {}                                           │
│                                              │ PostgreSQL database cluster, send a DELETE   │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ request to                                   │        │ $DIGITALOCEAN_TOKEN'                          │                                              │
│                                              │ /v2/databases/$DATABASE_ID/pools/$POOL_NAME. │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ A status of 204 will be given. This          │        │                                               │                                              │
│                                              │ indicates that the request was processed     │        │                                               │                                              │
│                                              │ successfully, but that no response body is   │        │                                               │                                              │
│                                              │ needed.                                      │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ delete_database                              │ To delete a specific database, send a DELETE │ DEL    │ curl -X DELETE -H 'Content-Type:              │ {}                                           │
│                                              │ request to                                   │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ /v2/databases/$DATABASE_ID/dbs/$DB_NAME. A   │        │ $DIGITALOCEAN_TOKEN'                          │                                              │
│                                              │ status of 204 will be given. This indicates  │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ that the request was processed successfully, │        │                                               │                                              │
│                                              │ but that no response body is needed. Note:   │        │                                               │                                              │
│                                              │ Database management is not supported for     │        │                                               │                                              │
│                                              │ Redis clusters.                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ destroy_a_database_cluster                   │ To destroy a specific database, send a       │ DEL    │ curl -X DELETE -H 'Content-Type:              │ {}                                           │
│                                              │ DELETE request to                            │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ /v2/databases/$DATABASE_ID. A status of 204  │        │ $DIGITALOCEAN_TOKEN'                          │                                              │
│                                              │ will be given. This indicates that the       │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ request was processed successfully, but that │        │                                               │                                              │
│                                              │ no response body is needed.                  │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ destroy_read_replica                         │ To destroy a specific read-only replica,     │ DEL    │ curl -X DELETE -H 'Content-Type:              │ {}                                           │
│                                              │ send a DELETE request to                     │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ /v2/databases/$DATABASE_ID/replicas/$REPLIC… │        │ $DIGITALOCEAN_TOKEN'                          │                                              │
│                                              │ Note: Read-only replicas are not supported   │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ for Redis clusters. A status of 204 will be  │        │                                               │                                              │
│                                              │ given. This indicates that the request was   │        │                                               │                                              │
│                                              │ processed successfully, but that no response │        │                                               │                                              │
│                                              │ body is needed.                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ list_all_database_clusters                   │ To list all of the database clusters         │ GET    │ curl -X GET -H 'Content-Type:                 │ {}                                           │
│                                              │ available on your account, send a GET        │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ request to /v2/databases. To limit the       │        │ $DIGITALOCEAN_TOKEN'                          │                                              │
│                                              │ results to database clusters with a specific │        │ 'https://api.digitalocean.com/v2/databases'   │                                              │
│                                              │ tag, include the tag_name query parameter    │        │                                               │                                              │
│                                              │ set to the name of the tag. For example,     │        │                                               │                                              │
│                                              │ /v2/databases?tag_name=$TAG_NAME. The result │        │                                               │                                              │
│                                              │ will be a JSON object with a databases key.  │        │                                               │                                              │
│                                              │ This will be set to an array of database     │        │                                               │                                              │
│                                              │ objects, each of which will contain the      │        │                                               │                                              │
│                                              │ standard database attributes. The embedded   │        │                                               │                                              │
│                                              │ connection and private_connection objects    │        │                                               │                                              │
│                                              │ will contain the information needed to       │        │                                               │                                              │
│                                              │ access the database cluster: The embedded    │        │                                               │                                              │
│                                              │ maintenance_window object will contain       │        │                                               │                                              │
│                                              │ information about any scheduled maintenance  │        │                                               │                                              │
│                                              │ for the database cluster.                    │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ list_all_databases                           │ To list all of the databases in a clusters,  │ GET    │ curl -X GET -H 'Content-Type:                 │ {}                                           │
│                                              │ send a GET request to                        │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ /v2/databases/$DATABASE_ID/dbs. The result   │        │ $DIGITALOCEAN_TOKEN'                          │                                              │
│                                              │ will be a JSON object with a dbs key. This   │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ will be set to an array of database objects, │        │                                               │                                              │
│                                              │ each of which will contain the standard      │        │                                               │                                              │
│                                              │ database attributes. Note: Database          │        │                                               │                                              │
│                                              │ management is not supported for Redis        │        │                                               │                                              │
│                                              │ clusters.                                    │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ list_backups_for_a_database_cluster          │ To list all of the available backups of a    │ GET    │ curl -X GET -H 'Content-Type:                 │ {}                                           │
│                                              │ PostgreSQL or MySQL database cluster, send a │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ GET request to                               │        │ $DIGITALOCEAN_TOKEN'                          │                                              │
│                                              │ /v2/databases/$DATABASE_ID/backups. Note:    │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ Backups are not supported for Redis          │        │                                               │                                              │
│                                              │ clusters. The result will be a JSON object   │        │                                               │                                              │
│                                              │ with a backups key. This will be set to an   │        │                                               │                                              │
│                                              │ array of backup objects, each of which will  │        │                                               │                                              │
│                                              │ contain the size of the backup and the       │        │                                               │                                              │
│                                              │ timestamp at which it was created.           │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ list_connection_pools                        │ To list all of the connection pools          │ GET    │ curl -X GET -H 'Content-Type:                 │ {}                                           │
│                                              │ available to a PostgreSQL database cluster,  │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ send a GET request to                        │        │ $DIGITALOCEAN_TOKEN'                          │                                              │
│                                              │ /v2/databases/$DATABASE_ID/pools. The result │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ will be a JSON object with a pools key. This │        │                                               │                                              │
│                                              │ will be set to an array of connection pool   │        │                                               │                                              │
│                                              │ objects.                                     │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ list_database_options                        │ To list all of the options available for the │ GET    │ curl -X GET -H 'Content-Type:                 │ {}                                           │
│                                              │ offered database engines, send a GET request │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ to /v2/databases/options. The result will be │        │ $DIGITALOCEAN_TOKEN'                          │                                              │
│                                              │ a JSON object with an options key.           │        │ 'https://api.digitalocean.com/v2/databases'   │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ list_database_users                          │ To list all of the users for your database   │ GET    │ curl -X GET -H 'Content-Type:                 │ {}                                           │
│                                              │ cluster, send a GET request to               │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ /v2/databases/$DATABASE_ID/users. Note: User │        │ $DIGITALOCEAN_TOKEN'                          │                                              │
│                                              │ management is not supported for Redis        │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ clusters. The result will be a JSON object   │        │                                               │                                              │
│                                              │ with a users key. This will be set to an     │        │                                               │                                              │
│                                              │ array of database user objects, each of      │        │                                               │                                              │
│                                              │ which will contain the standard database     │        │                                               │                                              │
│                                              │ user attributes. For MySQL clusters,         │        │                                               │                                              │
│                                              │ additional options will be contained in the  │        │                                               │                                              │
│                                              │ mysql_settings object.                       │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ list_firewall_rules_for_a_database           │ To list all of a database cluster's firewall │ GET    │ curl -X GET -H 'Content-Type:                 │ {}                                           │
│                                              │ rules (known as trusted sources in the       │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ control panel), send a GET request to        │        │ $DIGITALOCEAN_TOKEN'                          │                                              │
│                                              │ /v2/databases/$DATABASE_ID/firewall. The     │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ result will be a JSON object with a rules    │        │                                               │                                              │
│                                              │ key.                                         │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ list_read_replicas                           │ To list all of the read-only replicas        │ GET    │ curl -X GET -H 'Content-Type:                 │ {}                                           │
│                                              │ associated with a database cluster, send a   │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ GET request to                               │        │ $DIGITALOCEAN_TOKEN'                          │                                              │
│                                              │ /v2/databases/$DATABASE_ID/replicas. Note:   │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ Read-only replicas are not supported for     │        │                                               │                                              │
│                                              │ Redis clusters. The result will be a JSON    │        │                                               │                                              │
│                                              │ object with a replicas key. This will be set │        │                                               │                                              │
│                                              │ to an array of database replica objects,     │        │                                               │                                              │
│                                              │ each of which will contain the standard      │        │                                               │                                              │
│                                              │ database replica attributes.                 │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ migrate_a_database_cluster_to_a_new_region   │ To migrate a database cluster to a new       │ PUT    │ curl -X PUT -H 'Content-Type:                 │ {'region': 'lon1'}                           │
│                                              │ region, send a PUT request to                │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ /v2/databases/$DATABASE_ID/migrate. The body │        │ $DIGITALOCEAN_TOKEN' -d '$PAYLOAD'            │                                              │
│                                              │ of the request must specify a region         │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ attribute. A successful request will receive │        │                                               │                                              │
│                                              │ a 202 Accepted status code with no body in   │        │                                               │                                              │
│                                              │ response. Querying the database cluster will │        │                                               │                                              │
│                                              │ show that its status attribute will now be   │        │                                               │                                              │
│                                              │ set to migrating. This will transition back  │        │                                               │                                              │
│                                              │ to online when the migration has completed.  │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ remove_database_user                         │ To remove a specific database user, send a   │ DEL    │ curl -X DELETE -H 'Content-Type:              │ {}                                           │
│                                              │ DELETE request to                            │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ /v2/databases/$DATABASE_ID/users/$USERNAME.  │        │ $DIGITALOCEAN_TOKEN'                          │                                              │
│                                              │ A status of 204 will be given. This          │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ indicates that the request was processed     │        │                                               │                                              │
│                                              │ successfully, but that no response body is   │        │                                               │                                              │
│                                              │ needed. Note: User management is not         │        │                                               │                                              │
│                                              │ supported for Redis clusters.                │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ reset_database_user                          │ To reset the password for a database user,   │ POST   │ curl -X POST -H 'Content-Type:                │ {}                                           │
│                                              │ send a POST request to                       │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ /v2/databases/$DATABASE_ID/users/$USERNAME/… │        │ $DIGITALOCEAN_TOKEN'                          │                                              │
│                                              │ For mysql databases, the authentication      │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ method can be specifying by including a key  │        │                                               │                                              │
│                                              │ in the JSON body called mysql_settings with  │        │                                               │                                              │
│                                              │ the auth_plugin value specified. The         │        │                                               │                                              │
│                                              │ response will be a JSON object with a user   │        │                                               │                                              │
│                                              │ key. This will be set to an object           │        │                                               │                                              │
│                                              │ containing the standard database user        │        │                                               │                                              │
│                                              │ attributes.                                  │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ resize_a_database_cluster                    │ To resize a database cluster, send a PUT     │ PUT    │ curl -X PUT -H 'Content-Type:                 │ {'size': 'db-s-4vcpu-8gb', 'num_nodes': 3}   │
│                                              │ request to                                   │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ /v2/databases/$DATABASE_ID/resize. The body  │        │ $DIGITALOCEAN_TOKEN' -d '$PAYLOAD'            │                                              │
│                                              │ of the request must specify both the size    │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ and num_nodes attributes. A successful       │        │                                               │                                              │
│                                              │ request will receive a 202 Accepted status   │        │                                               │                                              │
│                                              │ code with no body in response. Querying the  │        │                                               │                                              │
│                                              │ database cluster will show that its status   │        │                                               │                                              │
│                                              │ attribute will now be set to resizing. This  │        │                                               │                                              │
│                                              │ will transition back to online when the      │        │                                               │                                              │
│                                              │ resize operation has completed.              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ retrieve_an_existing_database_cluster        │ To show information about an existing        │ GET    │ curl -X GET -H 'Content-Type:                 │ {}                                           │
│                                              │ database cluster, send a GET request to      │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ /v2/databases/$DATABASE_ID. The response     │        │ $DIGITALOCEAN_TOKEN'                          │                                              │
│                                              │ will be a JSON object with a database key.   │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ This will be set to an object containing the │        │                                               │                                              │
│                                              │ standard database cluster attributes. The    │        │                                               │                                              │
│                                              │ embedded connection and private_connection   │        │                                               │                                              │
│                                              │ objects will contain the information needed  │        │                                               │                                              │
│                                              │ to access the database cluster. The embedded │        │                                               │                                              │
│                                              │ maintenance_window object will contain       │        │                                               │                                              │
│                                              │ information about any scheduled maintenance  │        │                                               │                                              │
│                                              │ for the database cluster.                    │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ retrieve_an_existing_database_cluster_confi… │ Shows configuration parameters for an        │ GET    │ curl -X GET -H 'Content-Type:                 │ {}                                           │
│                                              │ existing database cluster by sending a GET   │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ request to                                   │        │ $DIGITALOCEAN_TOKEN'                          │                                              │
│                                              │ /v2/databases/$DATABASE_ID/config. The       │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ response is a JSON object with a config key, │        │                                               │                                              │
│                                              │ which is set to an object containing any     │        │                                               │                                              │
│                                              │ database configuration parameters.           │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ retrieve_connection_pool                     │ To show information about an existing        │ GET    │ curl -X GET -H 'Content-Type:                 │ {}                                           │
│                                              │ connection pool for a PostgreSQL database    │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ cluster, send a GET request to               │        │ $DIGITALOCEAN_TOKEN'                          │                                              │
│                                              │ /v2/databases/$DATABASE_ID/pools/$POOL_NAME. │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ The response will be a JSON object with a    │        │                                               │                                              │
│                                              │ pool key.                                    │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ retrieve_database                            │ To show information about an existing        │ GET    │ curl -X GET -H 'Content-Type:                 │ {}                                           │
│                                              │ database cluster, send a GET request to      │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ /v2/databases/$DATABASE_ID/dbs/$DB_NAME.     │        │ $DIGITALOCEAN_TOKEN'                          │                                              │
│                                              │ Note: Database management is not supported   │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ for Redis clusters. The response will be a   │        │                                               │                                              │
│                                              │ JSON object with a db key. This will be set  │        │                                               │                                              │
│                                              │ to an object containing the standard         │        │                                               │                                              │
│                                              │ database attributes.                         │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ retrieve_database_user                       │ To show information about an existing        │ GET    │ curl -X GET -H 'Content-Type:                 │ {}                                           │
│                                              │ database user, send a GET request to         │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ /v2/databases/$DATABASE_ID/users/$USERNAME.  │        │ $DIGITALOCEAN_TOKEN'                          │                                              │
│                                              │ Note: User management is not supported for   │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ Redis clusters. The response will be a JSON  │        │                                               │                                              │
│                                              │ object with a user key. This will be set to  │        │                                               │                                              │
│                                              │ an object containing the standard database   │        │                                               │                                              │
│                                              │ user attributes. For MySQL clusters,         │        │                                               │                                              │
│                                              │ additional options will be contained in the  │        │                                               │                                              │
│                                              │ mysql_settings object.                       │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ retrieve_read_replica                        │ To show information about an existing        │        │ curl -X GET -H 'Content-Type:                 │ {}                                           │
│                                              │ database replica, send a GET request to      │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ /v2/databases/$DATABASE_ID/replicas/$REPLIC… │        │ $DIGITALOCEAN_TOKEN'                          │                                              │
│                                              │ Note: Read-only replicas are not supported   │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ for Redis clusters. The response will be a   │        │                                               │                                              │
│                                              │ JSON object with a replica key. This will be │        │                                               │                                              │
│                                              │ set to an object containing the standard     │        │                                               │                                              │
│                                              │ database replica attributes.                 │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ retrieve_the_public_certificate              │ To retrieve the public certificate used to   │ GET    │ curl -X GET -H 'Content-Type:                 │ {}                                           │
│                                              │ secure the connection to the database        │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ cluster send a GET request to                │        │ $DIGITALOCEAN_TOKEN'                          │                                              │
│                                              │ /v2/databases/$DATABASE_ID/ca. The response  │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ will be a JSON object with a ca key. This    │        │                                               │                                              │
│                                              │ will be set to an object containing the      │        │                                               │                                              │
│                                              │ base64 encoding of the public key            │        │                                               │                                              │
│                                              │ certificate.                                 │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ stop_an_online_migration                     │ To stop an online migration, send a DELETE   │ DEL    │ curl -X DELETE -H 'Content-Type:              │ {}                                           │
│                                              │ request to                                   │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ /v2/databases/$DATABASE_ID/online-migration… │        │ $DIGITALOCEAN_TOKEN'                          │                                              │
│                                              │ A status of 204 will be given. This          │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ indicates that the request was processed     │        │                                               │                                              │
│                                              │ successfully, but that no response body is   │        │                                               │                                              │
│                                              │ needed.                                      │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│ update_firewall_rules_for_a_database         │ To update a database cluster's firewall      │ PUT    │ curl -X PUT -H 'Content-Type:                 │ {'rules': []}                                │
│                                              │ rules (known as trusted sources in the       │        │ application/json' -H 'Authorization: Bearer   │                                              │
│                                              │ control panel), send a PUT request to        │        │ $DIGITALOCEAN_TOKEN' -d '$PAYLOAD'            │                                              │
│                                              │ /v2/databases/$DATABASE_ID/firewall          │        │ 'https://api.digitalocean.com/v2/databases/$… │                                              │
│                                              │ specifying which resources should be able to │        │                                               │                                              │
│                                              │ open connections to the database. You may    │        │                                               │                                              │
│                                              │ limit connections to specific Droplets,      │        │                                               │                                              │
│                                              │ Kubernetes clusters, or IP addresses. When a │        │                                               │                                              │
│                                              │ tag is provided, any Droplet or Kubernetes   │        │                                               │                                              │
│                                              │ node with that tag applied to it will have   │        │                                               │                                              │
│                                              │ access. The firewall is limited to 100 rules │        │                                               │                                              │
│                                              │ (or trusted sources). When possible, we      │        │                                               │                                              │
│                                              │ recommend placing your databases into a VPC  │        │                                               │                                              │
│                                              │ network to limit access to them instead of   │        │                                               │                                              │
│                                              │ using a firewall. A successful               │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
│                                              │                                              │        │                                               │                                              │
└──────────────────────────────────────────────┴──────────────────────────────────────────────┴────────┴───────────────────────────────────────────────┴──────────────────────────────────────────────┘
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

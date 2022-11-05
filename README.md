# DOpg CLI
<p align="center"><img src="https://github.com/jim-schwoebel/dopg_cli/blob/main/assets/logo.png" alt="logo" width="300"></img></p>
<p align="center"><img src="https://github.com/jim-schwoebel/dopg_cli/blob/main/assets/logo_2.png" alt="logo" width="500"></img></p>

[![Python](https://img.shields.io/badge/python-v3.9+-blue.svg)]()
[![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/anfederico/Clairvoyant.svg)](https://github.com/jim-schwoebel/dopg_cli/issues)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)](https://github.com/jim-schwoebel/dopg_cli/issues)
[![License](https://img.shields.io/badge/license-Apache%202-blue)](https://www.apache.org/licenses/LICENSE-2.0.html)
[![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=Check%20out%20DOpg,%20an%20awesome%20new%20CLI%20framework%20for%20postgres%20on%20@DigitalOcean%20https://github.com/jim-schwoebel/dopg_cli&hashtags=digitalocean,postgres,doctl,do) 
[![Follow me](https://img.shields.io/github/followers/jim-schwoebel?style=social)](https://github.com/jim-schwoebel?tab=followers)
&nbsp;

🦈 An unofficial python client for digitalocean postgres clusters (5+ integrations).

Uses [click](https://click.palletsprojects.com/en/8.1.x/), [pgcli](https://github.com/dbcli/pgcli), and [rich](https://github.com/Textualize/rich) to create beautiful command line interactions for postgres databases. 

You can easily extend this framework to fit your particular use case.

Some things that DOpg can do include:
- [query databases](https://github.com/jim-schwoebel/dopg_cli/blob/main/README.md#query-databases) directly through a nice autocompletion widget 
- [use the DO databases API seamlessly](https://github.com/jim-schwoebel/dopg_cli/blob/main/README.md#api-commands) in an intuitive and beautiful way (e.g. in tables and pretty printed json); cache api responses in ```api_response.json``` in core folder so you don't need to log this elsewhere
- [work with doctl](https://github.com/jim-schwoebel/dopg_cli/blob/main/README.md#doctl-commands) - if you prefer DO's command line interface (though we do recommend using [the API](https://github.com/jim-schwoebel/dopg_cli/blob/main/README.md#api-commands))
- [get postgres doctl and api docs](https://github.com/jim-schwoebel/dopg_cli/blob/main/README.md#docs) from DigitalOcean for easy access
- [get db pricing from public links](https://github.com/jim-schwoebel/dopg_cli/blob/main/README.md#pricing) - to make it easy to make purchasing decisions

## MacOS setup (<3 minutes)
This first version has only been tested on MacOS.

First, install python3 and doctl [using homebrew](https://brew.sh/):
```
brew install python@3.9, doctl
```
Now that doctl is installed, initialize it with an auth token:
```
doctl auth init
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

### api commands
[The DigitalOcean API](https://docs.digitalocean.com/reference/api/api-reference/#tag/Databases) is a great way to get json responses from common routes related to databases.

To get a tabular list of possible commands, follow:
```
python3 cli.py --command api --route help
```
And it should output [api doc commands as of 2022-11-04](https://docs.digitalocean.com/reference/api/api-reference/#operation/databases_delete_connectionPool) - something like:
```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Route                                           ┃ Description                                         ┃ Method ┃ Sample                                              ┃ Payload                                             ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ add_connection_pool                             │ For PostgreSQL database clusters, connection pools  │ POST   │ curl -X POST -H 'Content-Type: application/json' -H │ {'name': 'backend-pool', 'mode': 'transaction',     │
│                                                 │ can be used to allow a database to share its idle   │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN' -d      │ 'size': 10, 'db': 'defaultdb', 'user': 'doadmin'}   │
│                                                 │ connections. The popular PostgreSQL connection      │        │ '$PAYLOAD'                                          │                                                     │
│                                                 │ pooling utility PgBouncer is used to provide this   │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ service. See here for more information about how    │        │                                                     │                                                     │
│                                                 │ and why to use PgBouncer connection pooling         │        │                                                     │                                                     │
│                                                 │ including details about the available transaction   │        │                                                     │                                                     │
│                                                 │ modes. To add a new connection pool to a PostgreSQL │        │                                                     │                                                     │
│                                                 │ database cluster, send a POST request to            │        │                                                     │                                                     │
│                                                 │ /v2/databases/$DATABASE_ID/pools specifying a name  │        │                                                     │                                                     │
│                                                 │ for the pool, the user to connect with, the         │        │                                                     │                                                     │
│                                                 │ database to connect to, as well as its desired size │        │                                                     │                                                     │
│                                                 │ and transaction mode.                               │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ add_database_user                               │ To add a new database user, send a POST request to  │ POST   │ curl -X POST -H 'Content-Type: application/json' -H │ {'name': 'app-01'}                                  │
│                                                 │ /v2/databases/$DATABASE_ID/users with the desired   │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN' -d      │                                                     │
│                                                 │ username. Note: User management is not supported    │        │ '$PAYLOAD'                                          │                                                     │
│                                                 │ for Redis clusters. When adding a user to a MySQL   │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ cluster, additional options can be configured in    │        │                                                     │                                                     │
│                                                 │ the mysql_settings object. The response will be a   │        │                                                     │                                                     │
│                                                 │ JSON object with a key called user. The value of    │        │                                                     │                                                     │
│                                                 │ this will be an object that contains the standard   │        │                                                     │                                                     │
│                                                 │ attributes associated with a database user          │        │                                                     │                                                     │
│                                                 │ including its randomly generated password.          │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ add_new_database                                │ To add a new database to an existing cluster, send  │ POST   │ curl -X POST -H 'Content-Type: application/json' -H │ {'name': 'alpha'}                                   │
│                                                 │ a POST request to /v2/databases/$DATABASE_ID/dbs.   │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN' -d      │                                                     │
│                                                 │ Note: Database management is not supported for      │        │ '$PAYLOAD'                                          │                                                     │
│                                                 │ Redis clusters. The response will be a JSON object  │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ with a key called db. The value of this will be an  │        │                                                     │                                                     │
│                                                 │ object that contains the standard attributes        │        │                                                     │                                                     │
│                                                 │ associated with a database.                         │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ configure_a_database_cluster_maintenance_window │ To configure the window when automatic maintenance  │ PUT    │ curl -X PUT -H 'Content-Type: application/json' -H  │ {'day': 'tuesday', 'hour': '14:00'}                 │
│                                                 │ should be performed for a database cluster, send a  │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN' -d      │                                                     │
│                                                 │ PUT request to                                      │        │ '$PAYLOAD'                                          │                                                     │
│                                                 │ /v2/databases/$DATABASE_ID/maintenance. A           │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ successful request will receive a 204 No Content    │        │                                                     │                                                     │
│                                                 │ status code with no body in response.               │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ create_a_new_database_cluster                   │ To create a database cluster, send a POST request   │ POST   │ curl -X POST -H 'Content-Type: application/json' -H │ {'name': 'backend-test', 'engine': 'pg', 'version': │
│                                                 │ to /v2/databases. The response will be a JSON       │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN' -d      │ '14', 'region': 'nyc3', 'size': 'db-s-2vcpu-4gb',   │
│                                                 │ object with a key called database. The value of     │        │ '$PAYLOAD'                                          │ 'num_nodes': 2, 'tags': ['production']}             │
│                                                 │ this will be an object that contains the standard   │        │ 'https://api.digitalocean.com/v2/databases'         │                                                     │
│                                                 │ attributes associated with a database cluster. The  │        │                                                     │                                                     │
│                                                 │ initial value of the database cluster's status      │        │                                                     │                                                     │
│                                                 │ attribute will be creating. When the cluster is     │        │                                                     │                                                     │
│                                                 │ ready to receive traffic, this will transition to   │        │                                                     │                                                     │
│                                                 │ online. The embedded connection and                 │        │                                                     │                                                     │
│                                                 │ private_connection objects will contain the         │        │                                                     │                                                     │
│                                                 │ information needed to access the database cluster.  │        │                                                     │                                                     │
│                                                 │ DigitalOcean managed PostgreSQL and MySQL database  │        │                                                     │                                                     │
│                                                 │ clusters take automated daily backups. To create a  │        │                                                     │                                                     │
│                                                 │ new database cluster based on a backup of an        │        │                                                     │                                                     │
│                                                 │ existing cluster, send a POST request to            │        │                                                     │                                                     │
│                                                 │ /v2/databases. In addition to the standard database │        │                                                     │                                                     │
│                                                 │ cluster attributes, the JSON body must include a    │        │                                                     │                                                     │
│                                                 │ key named backup_restore with the name of the       │        │                                                     │                                                     │
│                                                 │ original database cluster and the timestamp of the  │        │                                                     │                                                     │
│                                                 │ backup to be restored. Creating a database from a   │        │                                                     │                                                     │
│                                                 │ backup is the same as forking a database in the     │        │                                                     │                                                     │
│                                                 │ control panel. Note: Backups are not supported for  │        │                                                     │                                                     │
│                                                 │ Redis clusters.                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ create_a_read_replica                           │ To create a read-only replica for a PostgreSQL or   │ POST   │ curl -X POST -H 'Content-Type: application/json' -H │ {'name': 'read-nyc3-01', 'region': 'nyc3', 'size':  │
│                                                 │ MySQL database cluster, send a POST request to      │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN' -d      │ 'db-s-2vcpu-4gb'}                                   │
│                                                 │ /v2/databases/$DATABASE_ID/replicas specifying the  │        │ '$PAYLOAD'                                          │                                                     │
│                                                 │ name it should be given, the size of the node to be │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ used, and the region where it will be located.      │        │                                                     │                                                     │
│                                                 │ Note: Read-only replicas are not supported for      │        │                                                     │                                                     │
│                                                 │ Redis clusters. The response will be a JSON object  │        │                                                     │                                                     │
│                                                 │ with a key called replica. The value of this will   │        │                                                     │                                                     │
│                                                 │ be an object that contains the standard attributes  │        │                                                     │                                                     │
│                                                 │ associated with a database replica. The initial     │        │                                                     │                                                     │
│                                                 │ value of the read-only replica's status attribute   │        │                                                     │                                                     │
│                                                 │ will be forking. When the replica is ready to       │        │                                                     │                                                     │
│                                                 │ receive traffic, this will transition to active.    │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ delete_connection_pool                          │ To delete a specific connection pool for a          │ DEL    │ curl -X DELETE -H 'Content-Type: application/json'  │ {}                                                  │
│                                                 │ PostgreSQL database cluster, send a DELETE request  │        │ -H 'Authorization: Bearer $DIGITALOCEAN_TOKEN'      │                                                     │
│                                                 │ to /v2/databases/$DATABASE_ID/pools/$POOL_NAME. A   │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ status of 204 will be given. This indicates that    │        │                                                     │                                                     │
│                                                 │ the request was processed successfully, but that no │        │                                                     │                                                     │
│                                                 │ response body is needed.                            │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ delete_database                                 │ To delete a specific database, send a DELETE        │ DEL    │ curl -X DELETE -H 'Content-Type: application/json'  │ {}                                                  │
│                                                 │ request to /v2/databases/$DATABASE_ID/dbs/$DB_NAME. │        │ -H 'Authorization: Bearer $DIGITALOCEAN_TOKEN'      │                                                     │
│                                                 │ A status of 204 will be given. This indicates that  │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ the request was processed successfully, but that no │        │                                                     │                                                     │
│                                                 │ response body is needed. Note: Database management  │        │                                                     │                                                     │
│                                                 │ is not supported for Redis clusters.                │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ destroy_a_database_cluster                      │ To destroy a specific database, send a DELETE       │ DEL    │ curl -X DELETE -H 'Content-Type: application/json'  │ {}                                                  │
│                                                 │ request to /v2/databases/$DATABASE_ID. A status of  │        │ -H 'Authorization: Bearer $DIGITALOCEAN_TOKEN'      │                                                     │
│                                                 │ 204 will be given. This indicates that the request  │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ was processed successfully, but that no response    │        │                                                     │                                                     │
│                                                 │ body is needed.                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ destroy_read_replica                            │ To destroy a specific read-only replica, send a     │ DEL    │ curl -X DELETE -H 'Content-Type: application/json'  │ {}                                                  │
│                                                 │ DELETE request to                                   │        │ -H 'Authorization: Bearer $DIGITALOCEAN_TOKEN'      │                                                     │
│                                                 │ /v2/databases/$DATABASE_ID/replicas/$REPLICA_NAME.  │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ Note: Read-only replicas are not supported for      │        │                                                     │                                                     │
│                                                 │ Redis clusters. A status of 204 will be given. This │        │                                                     │                                                     │
│                                                 │ indicates that the request was processed            │        │                                                     │                                                     │
│                                                 │ successfully, but that no response body is needed.  │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ list_all_database_clusters                      │ To list all of the database clusters available on   │ GET    │ curl -X GET -H 'Content-Type: application/json' -H  │ {}                                                  │
│                                                 │ your account, send a GET request to /v2/databases.  │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'         │                                                     │
│                                                 │ To limit the results to database clusters with a    │        │ 'https://api.digitalocean.com/v2/databases'         │                                                     │
│                                                 │ specific tag, include the tag_name query parameter  │        │                                                     │                                                     │
│                                                 │ set to the name of the tag. For example,            │        │                                                     │                                                     │
│                                                 │ /v2/databases?tag_name=$TAG_NAME. The result will   │        │                                                     │                                                     │
│                                                 │ be a JSON object with a databases key. This will be │        │                                                     │                                                     │
│                                                 │ set to an array of database objects, each of which  │        │                                                     │                                                     │
│                                                 │ will contain the standard database attributes. The  │        │                                                     │                                                     │
│                                                 │ embedded connection and private_connection objects  │        │                                                     │                                                     │
│                                                 │ will contain the information needed to access the   │        │                                                     │                                                     │
│                                                 │ database cluster: The embedded maintenance_window   │        │                                                     │                                                     │
│                                                 │ object will contain information about any scheduled │        │                                                     │                                                     │
│                                                 │ maintenance for the database cluster.               │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ list_all_databases                              │ To list all of the databases in a clusters, send a  │ GET    │ curl -X GET -H 'Content-Type: application/json' -H  │ {}                                                  │
│                                                 │ GET request to /v2/databases/$DATABASE_ID/dbs. The  │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'         │                                                     │
│                                                 │ result will be a JSON object with a dbs key. This   │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ will be set to an array of database objects, each   │        │                                                     │                                                     │
│                                                 │ of which will contain the standard database         │        │                                                     │                                                     │
│                                                 │ attributes. Note: Database management is not        │        │                                                     │                                                     │
│                                                 │ supported for Redis clusters.                       │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ list_backups_for_a_database_cluster             │ To list all of the available backups of a           │ GET    │ curl -X GET -H 'Content-Type: application/json' -H  │ {}                                                  │
│                                                 │ PostgreSQL or MySQL database cluster, send a GET    │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'         │                                                     │
│                                                 │ request to /v2/databases/$DATABASE_ID/backups.      │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ Note: Backups are not supported for Redis clusters. │        │                                                     │                                                     │
│                                                 │ The result will be a JSON object with a backups     │        │                                                     │                                                     │
│                                                 │ key. This will be set to an array of backup         │        │                                                     │                                                     │
│                                                 │ objects, each of which will contain the size of the │        │                                                     │                                                     │
│                                                 │ backup and the timestamp at which it was created.   │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ list_connection_pools                           │ To list all of the connection pools available to a  │ GET    │ curl -X GET -H 'Content-Type: application/json' -H  │ {}                                                  │
│                                                 │ PostgreSQL database cluster, send a GET request to  │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'         │                                                     │
│                                                 │ /v2/databases/$DATABASE_ID/pools. The result will   │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ be a JSON object with a pools key. This will be set │        │                                                     │                                                     │
│                                                 │ to an array of connection pool objects.             │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ list_database_options                           │ To list all of the options available for the        │ GET    │ curl -X GET -H 'Content-Type: application/json' -H  │ {}                                                  │
│                                                 │ offered database engines, send a GET request to     │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'         │                                                     │
│                                                 │ /v2/databases/options. The result will be a JSON    │        │ 'https://api.digitalocean.com/v2/databases'         │                                                     │
│                                                 │ object with an options key.                         │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ list_database_users                             │ To list all of the users for your database cluster, │ GET    │ curl -X GET -H 'Content-Type: application/json' -H  │ {}                                                  │
│                                                 │ send a GET request to                               │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'         │                                                     │
│                                                 │ /v2/databases/$DATABASE_ID/users. Note: User        │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ management is not supported for Redis clusters. The │        │                                                     │                                                     │
│                                                 │ result will be a JSON object with a users key. This │        │                                                     │                                                     │
│                                                 │ will be set to an array of database user objects,   │        │                                                     │                                                     │
│                                                 │ each of which will contain the standard database    │        │                                                     │                                                     │
│                                                 │ user attributes. For MySQL clusters, additional     │        │                                                     │                                                     │
│                                                 │ options will be contained in the mysql_settings     │        │                                                     │                                                     │
│                                                 │ object.                                             │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ list_firewall_rules_for_a_database              │ To list all of a database cluster's firewall rules  │ GET    │ curl -X GET -H 'Content-Type: application/json' -H  │ {}                                                  │
│                                                 │ (known as trusted sources in the control panel),    │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'         │                                                     │
│                                                 │ send a GET request to                               │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ /v2/databases/$DATABASE_ID/firewall. The result     │        │                                                     │                                                     │
│                                                 │ will be a JSON object with a rules key.             │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ list_read_replicas                              │ To list all of the read-only replicas associated    │ GET    │ curl -X GET -H 'Content-Type: application/json' -H  │ {}                                                  │
│                                                 │ with a database cluster, send a GET request to      │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'         │                                                     │
│                                                 │ /v2/databases/$DATABASE_ID/replicas. Note:          │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ Read-only replicas are not supported for Redis      │        │                                                     │                                                     │
│                                                 │ clusters. The result will be a JSON object with a   │        │                                                     │                                                     │
│                                                 │ replicas key. This will be set to an array of       │        │                                                     │                                                     │
│                                                 │ database replica objects, each of which will        │        │                                                     │                                                     │
│                                                 │ contain the standard database replica attributes.   │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ migrate_a_database_cluster_to_a_new_region      │ To migrate a database cluster to a new region, send │ PUT    │ curl -X PUT -H 'Content-Type: application/json' -H  │ {'region': 'lon1'}                                  │
│                                                 │ a PUT request to                                    │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN' -d      │                                                     │
│                                                 │ /v2/databases/$DATABASE_ID/migrate. The body of the │        │ '$PAYLOAD'                                          │                                                     │
│                                                 │ request must specify a region attribute. A          │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ successful request will receive a 202 Accepted      │        │                                                     │                                                     │
│                                                 │ status code with no body in response. Querying the  │        │                                                     │                                                     │
│                                                 │ database cluster will show that its status          │        │                                                     │                                                     │
│                                                 │ attribute will now be set to migrating. This will   │        │                                                     │                                                     │
│                                                 │ transition back to online when the migration has    │        │                                                     │                                                     │
│                                                 │ completed.                                          │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ remove_database_user                            │ To remove a specific database user, send a DELETE   │ DEL    │ curl -X DELETE -H 'Content-Type: application/json'  │ {}                                                  │
│                                                 │ request to                                          │        │ -H 'Authorization: Bearer $DIGITALOCEAN_TOKEN'      │                                                     │
│                                                 │ /v2/databases/$DATABASE_ID/users/$USERNAME. A       │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ status of 204 will be given. This indicates that    │        │                                                     │                                                     │
│                                                 │ the request was processed successfully, but that no │        │                                                     │                                                     │
│                                                 │ response body is needed. Note: User management is   │        │                                                     │                                                     │
│                                                 │ not supported for Redis clusters.                   │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ reset_database_user                             │ To reset the password for a database user, send a   │ POST   │ curl -X POST -H 'Content-Type: application/json' -H │ {}                                                  │
│                                                 │ POST request to                                     │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'         │                                                     │
│                                                 │ /v2/databases/$DATABASE_ID/users/$USERNAME/reset_a… │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ For mysql databases, the authentication method can  │        │                                                     │                                                     │
│                                                 │ be specifying by including a key in the JSON body   │        │                                                     │                                                     │
│                                                 │ called mysql_settings with the auth_plugin value    │        │                                                     │                                                     │
│                                                 │ specified. The response will be a JSON object with  │        │                                                     │                                                     │
│                                                 │ a user key. This will be set to an object           │        │                                                     │                                                     │
│                                                 │ containing the standard database user attributes.   │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ resize_a_database_cluster                       │ To resize a database cluster, send a PUT request to │ PUT    │ curl -X PUT -H 'Content-Type: application/json' -H  │ {'size': 'db-s-4vcpu-8gb', 'num_nodes': 3}          │
│                                                 │ /v2/databases/$DATABASE_ID/resize. The body of the  │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN' -d      │                                                     │
│                                                 │ request must specify both the size and num_nodes    │        │ '$PAYLOAD'                                          │                                                     │
│                                                 │ attributes. A successful request will receive a 202 │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ Accepted status code with no body in response.      │        │                                                     │                                                     │
│                                                 │ Querying the database cluster will show that its    │        │                                                     │                                                     │
│                                                 │ status attribute will now be set to resizing. This  │        │                                                     │                                                     │
│                                                 │ will transition back to online when the resize      │        │                                                     │                                                     │
│                                                 │ operation has completed.                            │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ retrieve_an_existing_database_cluster           │ To show information about an existing database      │ GET    │ curl -X GET -H 'Content-Type: application/json' -H  │ {}                                                  │
│                                                 │ cluster, send a GET request to                      │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'         │                                                     │
│                                                 │ /v2/databases/$DATABASE_ID. The response will be a  │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ JSON object with a database key. This will be set   │        │                                                     │                                                     │
│                                                 │ to an object containing the standard database       │        │                                                     │                                                     │
│                                                 │ cluster attributes. The embedded connection and     │        │                                                     │                                                     │
│                                                 │ private_connection objects will contain the         │        │                                                     │                                                     │
│                                                 │ information needed to access the database cluster.  │        │                                                     │                                                     │
│                                                 │ The embedded maintenance_window object will contain │        │                                                     │                                                     │
│                                                 │ information about any scheduled maintenance for the │        │                                                     │                                                     │
│                                                 │ database cluster.                                   │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ retrieve_connection_pool                        │ To show information about an existing connection    │ GET    │ curl -X GET -H 'Content-Type: application/json' -H  │ {}                                                  │
│                                                 │ pool for a PostgreSQL database cluster, send a GET  │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'         │                                                     │
│                                                 │ request to                                          │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ /v2/databases/$DATABASE_ID/pools/$POOL_NAME. The    │        │                                                     │                                                     │
│                                                 │ response will be a JSON object with a pool key.     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ retrieve_database                               │ To show information about an existing database      │ GET    │ curl -X GET -H 'Content-Type: application/json' -H  │ {}                                                  │
│                                                 │ cluster, send a GET request to                      │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'         │                                                     │
│                                                 │ /v2/databases/$DATABASE_ID/dbs/$DB_NAME. Note:      │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ Database management is not supported for Redis      │        │                                                     │                                                     │
│                                                 │ clusters. The response will be a JSON object with a │        │                                                     │                                                     │
│                                                 │ db key. This will be set to an object containing    │        │                                                     │                                                     │
│                                                 │ the standard database attributes.                   │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ retrieve_database_cluster_configuration         │ Shows configuration parameters for an existing      │ GET    │ curl -X GET -H 'Content-Type: application/json' -H  │ {}                                                  │
│                                                 │ database cluster by sending a GET request to        │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'         │                                                     │
│                                                 │ /v2/databases/$DATABASE_ID/config. The response is  │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ a JSON object with a config key, which is set to an │        │                                                     │                                                     │
│                                                 │ object containing any database configuration        │        │                                                     │                                                     │
│                                                 │ parameters.                                         │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ retrieve_database_user                          │ To show information about an existing database      │ GET    │ curl -X GET -H 'Content-Type: application/json' -H  │ {}                                                  │
│                                                 │ user, send a GET request to                         │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'         │                                                     │
│                                                 │ /v2/databases/$DATABASE_ID/users/$USERNAME. Note:   │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ User management is not supported for Redis          │        │                                                     │                                                     │
│                                                 │ clusters. The response will be a JSON object with a │        │                                                     │                                                     │
│                                                 │ user key. This will be set to an object containing  │        │                                                     │                                                     │
│                                                 │ the standard database user attributes. For MySQL    │        │                                                     │                                                     │
│                                                 │ clusters, additional options will be contained in   │        │                                                     │                                                     │
│                                                 │ the mysql_settings object.                          │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ retrieve_read_replica                           │ To show information about an existing database      │        │ curl -X GET -H 'Content-Type: application/json' -H  │ {}                                                  │
│                                                 │ replica, send a GET request to                      │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'         │                                                     │
│                                                 │ /v2/databases/$DATABASE_ID/replicas/$REPLICA_NAME.  │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ Note: Read-only replicas are not supported for      │        │                                                     │                                                     │
│                                                 │ Redis clusters. The response will be a JSON object  │        │                                                     │                                                     │
│                                                 │ with a replica key. This will be set to an object   │        │                                                     │                                                     │
│                                                 │ containing the standard database replica            │        │                                                     │                                                     │
│                                                 │ attributes.                                         │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ retrieve_the_public_certificate                 │ To retrieve the public certificate used to secure   │ GET    │ curl -X GET -H 'Content-Type: application/json' -H  │ {}                                                  │
│                                                 │ the connection to the database cluster send a GET   │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN'         │                                                     │
│                                                 │ request to /v2/databases/$DATABASE_ID/ca. The       │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ response will be a JSON object with a ca key. This  │        │                                                     │                                                     │
│                                                 │ will be set to an object containing the base64      │        │                                                     │                                                     │
│                                                 │ encoding of the public key certificate.             │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ retrieve_the_status_of_an_online_migration      │ To retrieve the status of the most recent online    │ GET    │ curl -X PUT -H 'Content-Type: application/json' -H  │ {'source': {}, 'disable_ssl': False}                │
│                                                 │ migration, send a GET request to                    │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN' -d      │                                                     │
│                                                 │ /v2/databases/$DATABASE_ID/online-migration.        │        │ '$PAYLOAD'                                          │                                                     │
│                                                 │                                                     │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ start_an_online_migration                       │ To start an online migration, send a PUT request to │ PUT    │ curl -X PUT -H 'Content-Type: application/json' -H  │ {'source': {'host':                                 │
│                                                 │ /v2/databases/$DATABASE_ID/online-migration         │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN' -d      │ 'source-do-user-6607903-0.b.db.ondigitalocean.com', │
│                                                 │ endpoint. Migrating a cluster establishes a         │        │ '$PAYLOAD'                                          │ 'dbname': 'defaultdb', 'port': 25060, 'username':   │
│                                                 │ connection with an existing cluster and replicates  │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │ 'doadmin', 'password': 'paakjnfe10rsrsmf'},         │
│                                                 │ its contents to the target cluster. Online          │        │                                                     │ 'disable_ssl': False}                               │
│                                                 │ migration is only available for MySQL, PostgreSQL,  │        │                                                     │                                                     │
│                                                 │ and Redis clusters.                                 │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ stop_an_online_migration                        │ To stop an online migration, send a DELETE request  │ DEL    │ curl -X DELETE -H 'Content-Type: application/json'  │ {}                                                  │
│                                                 │ to                                                  │        │ -H 'Authorization: Bearer $DIGITALOCEAN_TOKEN'      │                                                     │
│                                                 │ /v2/databases/$DATABASE_ID/online-migration/$MIGRA… │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ A status of 204 will be given. This indicates that  │        │                                                     │                                                     │
│                                                 │ the request was processed successfully, but that no │        │                                                     │                                                     │
│                                                 │ response body is needed.                            │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│ update_database_cluster_configuration           │ To update the configuration for an existing         │ PATCH  │ curl -X PATCH -H 'Content-Type: application/json'   │ {'config': {'autovacuum_naptime': 60,               │
│                                                 │ database cluster, send a PATCH request to           │        │ -H 'Authorization: Bearer $DIGITALOCEAN_TOKEN' -d   │ 'autovacuum_vacuum_threshold': 50,                  │
│                                                 │ /v2/databases/$DATABASE_ID/config.                  │        │ '$PAYLOAD'                                          │ 'autovacuum_analyze_threshold': 50,                 │
│                                                 │                                                     │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │ 'autovacuum_vacuum_scale_factor': 0.2,              │
│                                                 │                                                     │        │                                                     │ 'autovacuum_analyze_scale_factor': 0.2,             │
│                                                 │                                                     │        │                                                     │ 'autovacuum_vacuum_cost_delay': 20,                 │
│                                                 │                                                     │        │                                                     │ 'autovacuum_vacuum_cost_limit': -1,                 │
│                                                 │                                                     │        │                                                     │ 'bgwriter_flush_after': 512,                        │
│                                                 │                                                     │        │                                                     │ 'bgwriter_lru_maxpages': 100,                       │
│                                                 │                                                     │        │                                                     │ 'bgwriter_lru_multiplier': 2,                       │
│                                                 │                                                     │        │                                                     │ 'idle_in_transaction_session_timeout': 0, 'jit':    │
│                                                 │                                                     │        │                                                     │ True, 'log_autovacuum_min_duration': -1,            │
│                                                 │                                                     │        │                                                     │ 'log_min_duration_statement': -1,                   │
│                                                 │                                                     │        │                                                     │ 'max_prepared_transactions': 0,                     │
│                                                 │                                                     │        │                                                     │ 'max_parallel_workers': 8,                          │
│                                                 │                                                     │        │                                                     │ 'max_parallel_workers_per_gather': 2,               │
│                                                 │                                                     │        │                                                     │ 'temp_file_limit': -1, 'wal_sender_timeout': 60000, │
│                                                 │                                                     │        │                                                     │ 'pgbouncer': {'server_reset_query_always': False,   │
│                                                 │                                                     │        │                                                     │ 'min_pool_size': 0, 'server_idle_timeout': 0,       │
│                                                 │                                                     │        │                                                     │ 'autodb_pool_size': 0, 'autodb_max_db_connections': │
│                                                 │                                                     │        │                                                     │ 0, 'autodb_idle_timeout': 0}, 'backup_hour': 21,    │
│                                                 │                                                     │        │                                                     │ 'backup_minute': 40, 'timescaledb': {},             │
│                                                 │                                                     │        │                                                     │ 'stat_monitor_enable': False}}                      │
│ update_firewall_rules_for_a_database            │ To update a database cluster's firewall rules       │ PUT    │ curl -X PUT -H 'Content-Type: application/json' -H  │ {'rules': []}                                       │
│                                                 │ (known as trusted sources in the control panel),    │        │ 'Authorization: Bearer $DIGITALOCEAN_TOKEN' -d      │                                                     │
│                                                 │ send a PUT request to                               │        │ '$PAYLOAD'                                          │                                                     │
│                                                 │ /v2/databases/$DATABASE_ID/firewall specifying      │        │ 'https://api.digitalocean.com/v2/databases/$DATABA… │                                                     │
│                                                 │ which resources should be able to open connections  │        │                                                     │                                                     │
│                                                 │ to the database. You may limit connections to       │        │                                                     │                                                     │
│                                                 │ specific Droplets, Kubernetes clusters, or IP       │        │                                                     │                                                     │
│                                                 │ addresses. When a tag is provided, any Droplet or   │        │                                                     │                                                     │
│                                                 │ Kubernetes node with that tag applied to it will    │        │                                                     │                                                     │
│                                                 │ have access. The firewall is limited to 100 rules   │        │                                                     │                                                     │
│                                                 │ (or trusted sources). When possible, we recommend   │        │                                                     │                                                     │
│                                                 │ placing your databases into a VPC network to limit  │        │                                                     │                                                     │
│                                                 │ access to them instead of using a firewall. A       │        │                                                     │                                                     │
│                                                 │ successful                                          │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
│                                                 │                                                     │        │                                                     │                                                     │
└─────────────────────────────────────────────────┴─────────────────────────────────────────────────────┴────────┴─────────────────────────────────────────────────────┴─────────────────────────────────────────────────────┘

```
And then you can run any of these commands in snake case (in the 'Route' column above); for example:
```
python3 cli.py --command api --route list_firewall_rules_for_a_database
```
Outputs pretty printed json:
```json
{
  "rules": [
    {
      "uuid": "41f1b3b4-a481-4ca7-8d92-f643a3606ac6",
      "cluster_uuid": "e4f7e56e-2c29-4de1-b937-965bd2e20e9d",
      "type": "ip_addr",
      "value": "115.206.82.140",
      "created_at": "2022-11-04T19:24:43Z"
    }
  ]
}
```

![](https://github.com/jim-schwoebel/dopg_cli/blob/main/assets/api.gif)

### doctl commands
You can also use [doctl](https://github.com/digitalocean/doctl)'s database commands directly - with a nicely formatted output for tables and other types of data. Note that doctl is the python command line interface for digitalocean.
```
python3 cli.py --command doctl
```

![](https://github.com/jim-schwoebel/dopg_cli/blob/main/assets/doctl.gif)

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

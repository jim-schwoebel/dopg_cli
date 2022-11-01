# dopg_cli
🦈 An unofficial python client for digitalocean postgres clusters (5+ integrations).

## setup 
```
brew install doctl, python3
doctl init
```
now install python dependencies within a virtual environment
```
git clone 
cd 
virtualenv env 
source env/bin/activate
pip3 install -r requirements.txt
```
now you can setup the cli (you will need your api key and must have already created a managed database postgres instance).
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
The DigitalOcean API is a great way to get json responses from common routes related to databases.

API database docs can be found [here](https://docs.digitalocean.com/reference/api/api-reference/#tag/Databases).
More on api docs here.

You can also get doctl docs using (pulls up doctl and api docs).
```
python3 cli.py --command docs
```

### pricing
You can get pricing of managed databases within digitalocean using public links:
```
python3 cli.py --command pricing
```

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

================================================ 
                 ABOUT                     
================================================ 

repository name: DOpg CLI
repository version: 1.0 
repository link: https://github.com/jim-schwoebel/dopg_cli
author: Jim Schwoebel 
role: Engineering manager
author contact: jschwoebel@digitalocean.com 
description: the DOpg CLI is a postgres command line interface for interacting with DigitalOcean's postgres managed db offering. 
license category: opensource 
license: Apache 2.0 license 
organization name: DigitalOcean 
location: Boston, MA 
website: https://digitalocean.com 
release date: 2022-10-27 

================================================ 
                LICENSE TERMS                      
================================================ 

Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at 

     http://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and 
limitations under the License. 
'''
import os, click, rich, json, datetime, time
from helpers import welcome, api_commands, get_settings

try:
    # load settings if they exist, assuming they work.
    settings = json.load(open('settings.json'))

except:
    # reload settings
    get_settings.reload()
    settings = json.load(open('settings.json'))

@click.command()
@click.option("--command", help="Command to operate on a database (see readme.md - e.g. ['query','api','doctl','docs','pricing'])")
@click.option("--route", help="Specify api route command here (for a list of routes, run: 'python3 cli.py --command api --route help')")
    
def api_init(command, route):
    # actual api response/description routes
    if command == 'init':
        get_settings.reload()
    else:
        api_commands.get_response(command, settings, route)

if __name__ == '__main__':
    api_init()

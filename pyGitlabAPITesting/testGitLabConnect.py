
import sys, os, urllib3, argparse, pdb
import gitlab



#bot authkey authkey = 'Uby43sz9x6qjRb1nSy8L'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://gitlab.com/rolando'
authkey = 'fkQ-bbsZzyNEzyxzAWcH'
project_name = 'Rolando Quintana/testGitAPI'

server = gitlab.Gitlab(url, authkey, api_version=4, ssl_verify=False)

project = server.projects.get(project_name)
print(project.attribute['name'])
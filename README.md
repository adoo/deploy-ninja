deploy-ninja
==========

##What is this?
Utility for deploying code to multiple environments.

##Usage:
Create a new file [deploy.py] for you project and include this 
module. In order to deploy, run your [deploy.py], with appropriate 
environment flag. You can define any number of environments.


###Config & run
Create a file [deploy.py]:

    #!/usr/bin/env python
    DeployNinja({
      "options": {
        "ignore":[".DS_Store", ".svn", ".git", "deploy.py", "deployninja.py", "deployninja.pyc"]
      },
      "environments": {
        "staging": {
          "target": {
            "host": "dummy-staging-server.com",
            "user": "ninja",
            "path": "/var/www/htdocs" # <- no ending slash
          },
          "source": {
            "path": "/Users/ninja/my_project" # <- no ending slash
          }
        },
        "production": {
          "confirm": "!!! You are about to deploy to production !!!",
          "target": {
            "host": "dummy-production-server.com",
            "user": "ninja",
            "path": "/var/www/htdocs" # <- no ending slash
          },
          "source": {
            "path": "/Users/ninja/my_project" # <- no ending slash
          }
        }
      }
    }).run()


###Deploying 
Run your file [deploy.py]:

    ./deploy.py -e staging
    ./deploy.py -e production


##More to come?

 * remote to remote
 * clean-slate
 * commands to run before & after

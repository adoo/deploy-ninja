#!/usr/bin/env python

"""
Example deploy configuraiton for DeployNinja.
Author: ado.b (echo@ado.io)
"""

from deployninja import DeployNinja

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


# basictest

7/15 trying to pass webhooks to jenkins (success)

7/15 execute shell "python -m unittest discover" (Success)

7/15 trying to pass build status to github (Success)
https://stackoverflow.com/questions/14274293/show-current-state-of-jenkins-build-on-github-repo/24269125#24269125

the status link cant be opened (it linked to 127.0.0.1:8080), need to change Jenkins IP configuration to http://140.115.53.39:8080
manage jenkins > configure system > Jenkins URL > http://140.115.53.39:8080/

7/16 trying to execute shell with pip install -r requirements.txt  (Success)

7/19 issue:
python3 -m pytest

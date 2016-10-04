from fabric.api import *

def cleanup_env(directory_path):      #deleting old deployment instance first
    sudo ('rm -rf %s' % directory_path)

# Base configurations, fabric uses python 2.6 but is compatible with python 3.x:
env.project_name = '$(project)'
env.database_password = '$(db_password)'
env.site_media_prefix = "site_media"
env.admin_media_prefix = "admin_media"
env.newsapps_media_prefix = "na_media"
env.path = '/home/newsapps/sites/%(project_name)s' % env
env.log_path = '/home/newsapps/logs/%(project_name)s' % env
env.env_path = '%(path)s/env' % env
env.repo_path = '%(path)s/repository' % env
env.apache_config_path = '/home/newsapps/sites/apache/%(project_name)s' % env
env.python = 'python2.6'

"""
def clone_repo():
    
    run('git clone https://github.com/mlisocialure/houndify_sdk' % env)

if we are pulling a file from github
"""

def test ():
    run('mocha test-server' % env)



def commit_repo():
    
    run('git add .' % env)
    run ('git commit -m 'commit message here' ' % env)
    run ('git push origin master' % env)
    
    
   

def deploy():
   
    #Deploy the latest version of the site to the server and restart Apache2. 

    require('settings', provided_by=[production, staging])
    require('branch', provided_by=[stable, master, branch])
    
    with settings(warn_only=True):
        maintenance_up()
        
    checkout_latest()
    gzip_assets()
    deploy_to_s3()
    refresh_widgets()
    maintenance_down()    
    


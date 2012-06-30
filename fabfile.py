from fabric.api import *

"""
Base configuration
"""
env.project_name = 'plan'
env.s3_bucket = 'plan.hacktyler.com'
    
"""
Commands - deployment
"""
def deploy():
    """
    Deploy the latest project site media to S3.
    """
    local(('s3cmd -P --guess-mime-type sync ./assets/ s3://%(s3_bucket)s/') % env)

"""
Deaths, destroyers of worlds
"""
def shiva_the_destroyer():
    """
    Remove all directories, databases, etc. associated with the application.
    """
    with settings(warn_only=True):
        run('s3cmd del --recursive s3://%(s3_bucket)s/' % env)


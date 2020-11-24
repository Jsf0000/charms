from charms.reactive import set_flag, when, when_not
from charmhelpers.core.hookenv import application_version_set, status_set
from charmhelpers.fetch import get_upstream_version
import subprocess as sp
from charmhelpers.core.templating import render


@when_not('mysql-example.installed')
def install_layer_example():
    set_flag('mysql-example.installed')
    
#Install mysql server
@when('apt.installed.mysql-server')
def set_message_mysql_server():
    application_version_set(get_upstream_version('mysql-server'))
   
    status_set('maintenance', 'Mysql Installed' )
    
    set_flag('mysql-server.version.set')
    

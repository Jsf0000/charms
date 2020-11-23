from charms.reactive import set_flag, when, when_not
from charmhelpers.core.hookenv import application_version_set, status_set
from charmhelpers.fetch import get_upstream_version
import subprocess as sp
from charmhelpers.core.templating import render


@when_not('mysql-example.installed')
def install_layer_example():
    set_flag('mysql-example.installed')
    
@when('apt.installed.hello')
def set_message_hello():
    application_version_set(get_upstream_version('hello'))
    
    message = sp.check_output('hello', stderr=sp.STDOUT)

    status_set('maintenance', message )
    
    set_flag('hello.version.set')
    
@when('database.available')
def write_text_file(mysql):
    render(source='text-file.tmpl',
           target='/root/text-file.txt',
           owner='root',
           perms=0o775,
           context={
               'my_database': mysql,
           })
    status_set('active', 'Ready: File rendered.')

@when_not('database.connected')
def missing_mysql():
    status_set('blocked', 'Please add relation to MySQL')

@when('database.connected')
@when_not('database.available')
def waiting_mysql(mysql):
    status_set('waiting', 'Waiting for MySQL')
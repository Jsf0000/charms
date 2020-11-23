from charms.reactive import set_flag, when, when_not
from charmhelpers.core.hookenv import application_version_set, status_set
from charmhelpers.fetch import get_upstream_version
import subprocess as sp

@when_not('example-jason.installed')
def install_example():
    set_flag('example-jason.installed')

@when('apt.installed.hello')
def set_message_hello():
    # Set the upstream version of hello for juju status.
    application_version_set(get_upstream_version('hello'))

    # Run hello and get the message
    message = sp.check_output('hello', stderr=sp.STDOUT)

    # Set the active status with the message
    status_set('active', message )

    # Signal that we know the version of hello
    set_flag('hello.version.set')

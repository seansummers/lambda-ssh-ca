import collections
import os
import subprocess


DEFAULT_EVENT = {
    'signing_key': 'server_ca',
    'key_identifier': 'host_auth_server',
    'principal_name': 'auth.example.com',
    'age': '+52w',
    'key_to_sign': 'server_ca.pub',
    'is_host': 'true',
}

with open('/etc/system-release', 'r') as release_check:
    if 'Amazon Linux AMI release 2016.03' not in release_check.read():
        print('WARNING: Lambda AMI has changed, update libfipscheck!')

PATH = '.'

cwd = os.path.abspath(PATH)
ssh_keygen = os.path.join(cwd, 'ssh-keygen')
env = os.environ.copy()

ld_library_path = (_ for _ in (env.get('LD_LIBRARY_PATH', ''), cwd) if _)
env.update(LD_LIBRARY_PATH=':'.join(ld_library_path))


def call(command, cwd, env):
    returncode = subprocess.call(command, cwd=cwd, env=env)
    if returncode != 0:
        raise Exception(returncode)


def handler(event=None, context=None):
    event = event or DEFAULT_EVENT
    signing_key = event.get('signing_key')
    key_identifier = event.get('key_identifier')
    principal_name = event.get('principal_name')
    age = event.get('age')
    key_to_sign = event.get('key_to_sign')
    is_host = event.get('is_host')
    command = [ssh_keygen]
    if is_host:
        command.append('-h')
    command.extend([
        '-s', signing_key,
        '-I', key_identifier,
        '-n', principal_name,
        '-V', age,
        key_to_sign
    ])
    call(command, cwd, env)


if __name__ == '__main__':
    handler()
    user_event = {
        'signing_key': 'users_ca',
        'key_identifier': 'host_auth_server',
        'principal_name': 'user username',
        'age': '+52w',
        'key_to_sign': 'users_ca.pub',
    }
    handler(user_event)

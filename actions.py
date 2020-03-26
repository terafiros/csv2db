import argparse, getpass
from sgbds import SQLServer, MySQL, PostgreSQL

class PasswordAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs='?', **kwargs):
        super(PasswordAction, self).__init__(option_strings, dest, nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        password = getpass.getpass()
        setattr(namespace, self.dest, password)


class SGBDAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs='?', **kwargs):
        super(SGBDAction, self).__init__(option_strings, dest, nargs, **kwargs)
        self.sgbds = {'sqlserver': SQLServer(),
                      'mysql': MySQL(),
                      'postgresql':PostgreSQL()
                      }

    def __call__(self, parser, namespace, values, option_string=None):
        sgbd = self.sgbds[values]
        connection_string = sgbd.get_data_for_connection()
        connection = sgbd.make_connection()
        setattr(namespace, 'connection_string', connection_string)
        setattr(namespace, 'connection', connection)
        setattr(namespace, 'sgbd', sgbd)

from contextlib import contextmanager
from dataclasses import dataclass
import dbt.exceptions
from dbt.adapters.base import Credentials
from dbt.adapters.{{cookiecutter.adapter_src}} import {{cookiecutter.connection_cls}}
from dbt.logger import GLOBAL_LOGGER as logger


@dataclass
class {{cookiecutter.adapter_title}}Credentials(Credentials):
    # Add credentials members here, like:
    # host: str
    # port: int
    # username: str
    # password: str

    _ALIASES = {
        'dbname':'database',
        'pass':'password',
        'user':'username'
    }

    @property
    def type(self):
        return '{{cookiecutter.adapter}}'

    @property
    def unique_field(self):
        return self.host

    def _connection_keys(self):
        return ('host','port','username','user')

# add kwargs propperly to the correct spots from create.py ex connection_cls = SQLConnectionManager
class {{cookiecutter.adapter_title}}ConnectionManager({{cookiecutter.connection_cls}}):
    TYPE = '{{cookiecutter.adapter}}'

    @contextmanager
    def exception_handler(self,sql: str):
        try:
            yield
        except:
            pass
        except:
             pass

    @classmethod
    def open(cls,connection):
        if connection.state == 'open':
            logger.debug('connection is already open, skipping open.')
            return connection
        
        credentials = connection.credentials

        try:
            handle = {{cookiecutter.adapter}}_library(
                host=credentials.host,
                port=credentials.port,
                username=credentials.username,
                password=credentials.password,
            )
            connection.state = 'open'
            connection.handle = handle
        except {{cookiecutter.adapter}}_library.Error as e:
            logger.debug('Got an error when attempting to open {{cookiecutter.adapter}}')
            connection.handle = None
            connection.state = 'fail'
            
        return connection

    @classmethod
    def get_response(cls,cursor):
        return cursor.status_message
    

    def cancel(self, connection):
        pass


   
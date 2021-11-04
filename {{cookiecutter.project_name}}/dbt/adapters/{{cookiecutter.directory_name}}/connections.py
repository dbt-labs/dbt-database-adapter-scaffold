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

class {{cookiecutter.adapter_title}}ConnectionManager({{cookiecutter.connection_cls}}):
    TYPE = '{{cookiecutter.adapter}}'

    @contextmanager
    def exception_handler(self, sql: str):
        # ## Example ##
        # try:
        #     yield
        # except myadapter_library.DatabaseError as exc:
        #     self.release(connection_name)

        #     logger.debug('myadapter error: {}'.format(str(e)))
        #     raise dbt.exceptions.DatabaseException(str(exc))
        # except Exception as exc:
        #     logger.debug("Error running SQL: {}".format(sql))
        #     logger.debug("Rolling back transaction.")
        #     self.release(connection_name)
        #     raise dbt.exceptions.RuntimeException(str(exc))
        pass

    @classmethod
    def open(cls, connection):
        # ## Example ##
        # if connection.state == 'open':
        #     logger.debug('Connection is already open, skipping open.')
        #     return connection

        # credentials = connection.credentials

        # try:
        #     handle = myadapter_library.connect(
        #         host=credentials.host,
        #         port=credentials.port,
        #         username=credentials.username,
        #         password=credentials.password,
        #         catalog=credentials.database
        #     )
        #     connection.state = 'open'
        #     connection.handle = handle
        # return connection
        pass

    @classmethod
    def get_response(cls,cursor):
        # ## Example ##
        # return cursor.status_message
        pass
    
    def cancel(self, connection):
        # ## Example ##
        # tid = connection.handle.transaction_id()
        # sql = 'select cancel_transaction({})'.format(tid)
        # logger.debug("Cancelling query '{}' ({})".format(connection_name, pid))
        # _, cursor = self.add_query(sql, 'master')
        # res = cursor.fetchone()
        # logger.debug("Canceled query '{}': {}".format(connection_name, res))
        pass


   
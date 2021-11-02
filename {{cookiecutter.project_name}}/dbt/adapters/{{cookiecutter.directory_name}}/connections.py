from dataclasses import dataclass
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

    @property
    def type(self):
        return {{cookiecutter.adapter}}

    @property
    def unique_field(self):
        return self.host

    def _connection_keys(self):
        # return an iterator of keys to pretty-print in 'dbt debug'.
        # Omit fields like 'password'!
        raise NotImplementedError

# add kwargs propperly to the correct spots from create.py ex connection_cls = SQLConnectionManager
class {{cookiecutter.adapter_title}}ConnectionManager({{cookiecutter.connection_cls}}):
    TYPE = '{{cookiecutter.adapter}}'


   
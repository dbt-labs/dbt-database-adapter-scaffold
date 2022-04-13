{% if cookiecutter.is_sql_adapter == "true" %}
from dbt.adapters.sql import SQLAdapter as adapter_cls
{% else %}
from dbt.adapters.base import BaseAdapter as adapter_cls
{% endif %}
from dbt.adapters.{{cookiecutter.directory_name}} import {{cookiecutter.adapter_title}}ConnectionManager



class {{cookiecutter.adapter_title}}Adapter(adapter_cls):
    '''
    Controls actual implmentation of adapter, and ability to override certain methods.
    '''

    ConnectionManager = {{cookiecutter.adapter_title}}ConnectionManager

    @classmethod
    def date_function(cls):
        '''
        Returns canonical date func
        '''
        return 'datenow()'

 # may require more build out to make more user friendly to confer with team and community.

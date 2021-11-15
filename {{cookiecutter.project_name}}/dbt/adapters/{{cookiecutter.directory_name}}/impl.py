# adapter_src, and adapter_cls comes from kwargs in create.py
from dbt.adapters.{{cookiecutter.adapter_src}} import {{cookiecutter.adapter_cls}}
from dbt.adapters.{{cookiecutter.adapter}} import {{cookiecutter.adapter_title}}ConnectionManager



class {{cookiecutter.adapter_title}}Adapter({{cookiecutter.adapter_cls}}):
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

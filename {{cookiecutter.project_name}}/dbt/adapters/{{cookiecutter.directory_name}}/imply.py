# adapter_src, and adapter_cls comes from kwargs in create.py
from dbt.adapters.{{cookiecutter.adapter_src}} import {{cookiecutter.adapter_cls}}
from dbt.adapters.{{cookiecutter.adapter}} import {{cookiecutter.adapter_title}}ConnectionManager



class {{cookiecutter.adapter_title}}Adapter({{cookiecutter.adapter_cls}}):
    ConnectionManager = {{cookiecutter.adapter_title}}ConnectionManager

    @classmethod
    def date_function(cls):
        return 'datenow()'

 # may require more build out to make more user friendly to confer with team and community.


#  "adapter_cls":["SQLAdapter","BaseAdapter"],
#  "connection_cls":["SQLConnectionManager","BaseConnectionManager"],
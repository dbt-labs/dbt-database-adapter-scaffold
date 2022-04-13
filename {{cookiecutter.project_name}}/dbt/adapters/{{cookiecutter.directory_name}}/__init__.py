from dbt.adapters.{{cookiecutter.directory_name}}.connections import {{cookiecutter.adapter_title}}ConnectionManager # noqa
from dbt.adapters.{{cookiecutter.directory_name}}.connections import {{cookiecutter.adapter_title}}Credentials
from dbt.adapters.{{cookiecutter.directory_name}}.impl import {{cookiecutter.adapter_title}}Adapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import {{cookiecutter.directory_name}}


Plugin = AdapterPlugin(
    adapter={{cookiecutter.adapter_title}}Adapter,
    credentials={{cookiecutter.adapter_title}}Credentials,
    include_path={{cookiecutter.directory_name}}.PACKAGE_PATH)
from dbt.adapters.{{cookiecutter.adapter}}.connections import {{cookiecutter.adapter_title}}ConnectionManager
from dbt.adapters.{{cookiecutter.adapter}}.connections import {{cookiecutter.adapter_title}}Credentials
from dbt.adapters.{{cookiecutter.adapter}}.impl import {{cookiecutter.adapter_title}}Adapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import {{cookiecutter.adapter}}


Plugin = AdapterPlugin(
    adapter={{cookiecutter.adapter_title}}Adapter,
    credentials={{cookiecutter.adapter_title}}Credentials,
    include_path={{cookiecutter.adapter}}.PACKAGE_PATH)
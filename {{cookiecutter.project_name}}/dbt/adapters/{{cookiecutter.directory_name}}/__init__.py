from dbt.adapters.{{ cookiecutter.directory_name }}.connections import {{ cookiecutter.adapter_name }}ConnectionManager # noqa
from dbt.adapters.{{ cookiecutter.directory_name }}.connections import {{ cookiecutter.adapter_name }}Credentials
from dbt.adapters.{{ cookiecutter.directory_name }}.impl import {{ cookiecutter.adapter_name }}Adapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import {{ cookiecutter.directory_name }}


Plugin = AdapterPlugin(
    adapter={{ cookiecutter.adapter_name }}Adapter,
    credentials={{ cookiecutter.adapter_name }}Credentials,
    include_path={{ cookiecutter.directory_name }}.PACKAGE_PATH
    )

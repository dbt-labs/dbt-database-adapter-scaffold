/* For examples of how to fill out the macros please refer to the postgres adapter and docs
postgres adapter macros: https://github.com/dbt-labs/dbt-core/blob/main/plugins/postgres/dbt/include/postgres/macros/adapters.sql
dbt docs: https://docs.getdbt.com/docs/contributing/building-a-new-adapter
*/


{{'{%'}} macro {{cookiecutter.adapter}}__alter_column_type(relation,column_name,new_column_type) {{ '-%}' }}
{{'{%'}} endmacro {{ '%}' }}

{{'{%'}} macro {{cookiecutter.adapter}}__check_schema_exists(information_schema,schema) {{ '-%}' }}
{{'{%'}} endmacro {{ '%}' }}

{{'{%'}} macro {{cookiecutter.adapter}}__create_schema(relation) {{ '-%}' }}
{{'{%'}} endmacro {{ '%}' }}

{{'{%'}} macro {{cookiecutter.adapter}}__drop_relation(relation) {{ '-%}' }}
{{'{%'}} endmacro {{ '%}' }}

{{'{%'}} macro {{cookiecutter.adapter}}__drop_schema(relation) {{ '-%}' }}
{{'{%'}} endmacro {{ '%}' }}

{{'{%'}} macro {{cookiecutter.adapter}}__get_columns_in_relation(relation) {{ '-%}' }}
{{'{%'}} endmacro {{ '%}' }}

{{'{%'}} macro {{cookiecutter.adapter}}__list_relations_without_caching(schema_relation) {{ '-%}' }}
{{'{%'}} endmacro {{ '%}' }}

{{'{%'}} macro {{cookiecutter.adapter}}__list_schemas(database) {{ '-%}' }}
{{'{%'}} endmacro {{ '%}' }}

{{'{%'}} macro {{cookiecutter.adapter}}__rename_relation(from_relation, to_relation) {{ '-%}' }}
{{'{%'}} endmacro {{ '%}' }}

{{'{%'}} macro {{cookiecutter.adapter}}__truncate_relation(relation) {{ '-%}' }}
{{'{%'}} endmacro {{ '%}' }}

{{'{%'}} macro {{cookiecutter.adapter}}__current_timestamp() {{ '-%}' }}
{{'{#'}} docs show not to be implemented currently. {{'#}'}}
{{'{%'}} endmacro {{ '%}' }}
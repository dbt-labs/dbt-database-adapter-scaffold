/* For examples of how to fill out the macros please refer to the postgres adapter and docs
postgres adapter macros: https://github.com/dbt-labs/dbt-core/blob/main/plugins/postgres/dbt/include/postgres/macros/adapters.sql
dbt docs: https://docs.getdbt.com/docs/contributing/building-a-new-adapter
*/

{{'{%'}} macro {{cookiecutter.adapter}}__alter_column_type(relation,column_name,new_column_type) {{ '-%}' }}
{{'{%'}} endmacro {{ '%}' }}

{{'{%'}} macro {{cookiecutter.adapter}}__check_schema_exists(information_schema,schema) {{ '-%}' }}
{{'{%'}} endmacro {{ '%}' }}

--  Example from postgres adapter in dbt-core 
--  Notice how you can build out other methods than the designated ones for the impl.py file,
--  to make a more robust adapter. ex. (verify_database)

/*
{% raw %}
 {% macro postgres__create_schema(relation) -%}
   {% if relation.database -%}
    {{ adapter.verify_database(relation.database) }}
  {%- endif -%}   {%- call statement('create_schema') -%}
     create schema if not exists {{ relation.without_identifier().include(database=False) }}
   {%- endcall -%}
 {% endmacro %}
 {% endraw %}
*/

{{'{%'}} macro {{cookiecutter.adapter}}__create_schema(relation) {{ '-%}' }}
{{'{%'}} endmacro {{ '%}' }}

-- {% raw %}
-- {% macro postgres__drop_schema(relation) -%}
--   {% if relation.database -%}
--     {{ adapter.verify_database(relation.database) }}
--   {%- endif -%}
--   {%- call statement('drop_schema') -%}
--     drop schema if exists {{ relation.without_identifier().include(database=False) }} cascade
--   {%- endcall -%}
-- {% endmacro %}
-- {% endraw %}

{{'{%'}} macro {{cookiecutter.adapter}}__drop_relation(relation) {{ '-%}' }}
{{'{%'}} endmacro {{ '%}' }}

{{'{%'}} macro {{cookiecutter.adapter}}__drop_schema(relation) {{ '-%}' }}
{{'{%'}} endmacro {{ '%}' }}

-- {% raw %}
--  Example of 1 of 3 required macros that does not have a default implementation
-- {% macro postgres__get_columns_in_relation(relation) -%}
--   {% call statement('get_columns_in_relation', fetch_result=True) %}
--       select
--           column_name,
--           data_type,
--           character_maximum_length,
--           numeric_precision,
--           numeric_scale

--       from {{ relation.information_schema('columns') }}
--       where table_name = '{{ relation.identifier }}'
--         {% if relation.schema %}
--         and table_schema = '{{ relation.schema }}'
--         {% endif %}
--       order by ordinal_position

--   {% endcall %}
--   {% set table = load_result('get_columns_in_relation').table %}
--   {{ return(sql_convert_columns_in_relation(table)) }}
-- {% endmacro %}
-- {% endraw %}

{{'{%'}} macro {{cookiecutter.adapter}}__get_columns_in_relation(relation) {{ '-%}' }}
{{'{%'}} endmacro {{ '%}' }}

--  Example of 2 of 3 required macros that do not come with a default implementation

-- {% raw %}
-- {% macro postgres__list_relations_without_caching(schema_relation) %}
--   {% call statement('list_relations_without_caching', fetch_result=True) -%}
--     select
--       '{{ schema_relation.database }}' as database,
--       tablename as name,
--       schemaname as schema,
--       'table' as type
--     from pg_tables
--     where schemaname ilike '{{ schema_relation.schema }}'
--     union all
--     select
--       '{{ schema_relation.database }}' as database,
--       viewname as name,
--       schemaname as schema,
--       'view' as type
--     from pg_views
--     where schemaname ilike '{{ schema_relation.schema }}'
--   {% endcall %}
--   {{ return(load_result('list_relations_without_caching').table) }}
-- {% endmacro %}
-- {% endraw %}

{{'{%'}} macro {{cookiecutter.adapter}}__list_relations_without_caching(schema_relation) {{ '-%}' }}
{{'{%'}} endmacro {{ '%}' }}

{{'{%'}} macro {{cookiecutter.adapter}}__list_schemas(database) {{ '-%}' }}
{{'{%'}} endmacro {{ '%}' }}

{{'{%'}} macro {{cookiecutter.adapter}}__rename_relation(from_relation, to_relation) {{ '-%}' }}
{{'{%'}} endmacro {{ '%}' }}

{{'{%'}} macro {{cookiecutter.adapter}}__truncate_relation(relation) {{ '-%}' }}
{{'{%'}} endmacro {{ '%}' }}

-- {% raw %}
-- Example 3 of 3 of required macros that does not have a default implementation.
--  ** Good example of building out small methods ** please refer to impl.py for implementation of now() in postgres plugin
-- {% macro postgres__current_timestamp() -%}
--   now()
-- {%- endmacro %}
-- {% endraw %}

{{'{%'}} macro {{cookiecutter.adapter}}__current_timestamp() {{ '-%}' }}
{{'{#'}} docs show not to be implemented currently. {{'#}'}}
{{'{%'}} endmacro {{ '%}' }}
 {{'{{%'}} macro {{cookiecutter.adapter}}__get_catalog(information_schema, schemas){{ '-%}}' }}

   {{'{{%'}}set msg {{ '-%}}' }}
    get_catalog not implemented for {{cookiecutter.adapter}}
   {{ '-%}}' }} endset {{'{{%'}}

  {{ '{{{{ exceptions.raise_compiler_error(msg) }}}}' }}
 {{'{{%'}} endmacro {{'{{%'}}
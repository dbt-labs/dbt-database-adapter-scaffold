 {{'{{%'}} macro {{cookiecutter.adapter}}__get_catalog(information_schema, schemas){{ '-%}}' }}

   {{'{{%'}}set msg {{ '-%}}' }}
    get_catalog not implemented for {{cookiecutter.adapter}}
   {{ '-%}}' }} endset {{'{{%'}}
    /*
      Your database likely has a way of accessing metadata about its objects,
      whether by querying an information schema or by running `show` and `describe` commands. 
      dbt will use this macro to generate its catalog of objects it knows about. The catalog is one of 
      the artifacts powering the documentation site.
      As an example, below is a simplified version of postgres__get_catalog
    */


  {{ '{{{{ exceptions.raise_compiler_error(msg) }}}}' }}
 {{'{{%'}} endmacro {{'{{%'}}
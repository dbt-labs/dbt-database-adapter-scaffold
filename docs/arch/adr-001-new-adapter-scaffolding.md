# New Adapter Scaffold

## Context

Currently we offer the ability for users and datawarehouses to build vendor/community supported adapter plugins via the [`create_adapter_plugins.py`](https://github.com/dbt-labs/dbt/blob/47033c459f2c835d81cc845d49ef23e7d19736b6/core/scripts/create_adapter_plugins.py) file. While this file is able to produce a usable adapter plugin, it is not the most user friendly experience as we have noted over time and needed to be updated.

### known issues or possible improvements to be made

- Updating the script to generate a new adapter plugin is tricky. You must edit numerous template strings in python code, which makes it difficult to test and search for all instances that need to be updated. ex. `$ python create_adapter_plugins.py --sql --title-case=MyAdapter ./ myadapter`
- Not an interactive experience, must know and pass all required arguments to the .py file 
- stuck with defaults, or missing dbt suggested default dependencies
  - Options to set up Github Actions
  - flake8 by default for linting to match other adapters
  - mypy by default or optional for static type checking
  - tox by default 
  - Ability to make a docker image by default
- Lack of docstrings, examples, comments to help users undestand what needs to be built out.
- Lack of pointers to what offical documentation we do have.

## Options

- Pull out current script, and move it to a new repo by itself
  - lots of template strings difficult to parse
- use Scaffolding tool
  - easier to maintain
  - interactive
  - possibly more easily testable
  - potential scaffolding tools
      - [`cookiecutter`](https://cookiecutter.readthedocs.io/en/1.7.2/overview.html)
        - Uses a json file to trigger commandline interactive session and passes variables user defines or chooses between potential defaults to fill out jinja templated variables and produce a new repo
        - allows for manipulation of json behind scense to keep interactive session from being to long
        - provides various ways to run program, either from fork/cloning, from a recognized cookiecutter command without cloning, or from within `dbt-core` able to take advantage of bumpversioning.
      - [`pyscaffold`](https://cookiecutter.readthedocs.io/en/1.7.2/overview.html)
        - creates a simple scaffold of project not as flexible as cookiecutter
      - [`yehua`](https://yehua.readthedocs.io/en/latest/)
        - Seems to of had similar functionality to cookiecutter but hasn't been suppoted in quite some time therefore no longer works with pip install, (unusable)

## Decision

Firstly after looking at available tooling, we landed on using `cookiecutter` to aid in creating a interactive scaffolding session for users quickily generate a starting point to build out their adapter plugin by quickly building out variable names, giving choice selections for things like `adapter_src` which is how we let the program know which connection methods to pull in from `dbt-core`. This also meant we could keep much of the structure for the files the same from previous adapter generator by having the files exist in the starting state and just passing the user passed parameters on generation. 

Secondly we looked at our current `dbt-docs` to see what things we specifically require users to build out for adapters to work ex. (class methods for connection, macros.) and added starting stubs to the files along with docstrings declaring their purpose, examples from other adapters, pointers in comments to documentation.


## Status

proposed

## Consequences

We now have a adapter plugin that takes what our original process did and improves upon it by trying to be more explicit in what needs to be done, and offering helpful tips or references. we have given users the suggested tools we at `dbt` use ourselves, and can refocus towards other more deep dive areas around testing these adapters and making that a more clear process.
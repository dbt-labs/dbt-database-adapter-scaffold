# New Adapter Scaffold

## Context
Currently we offer the ability for users and datawarehouses to build vendor/community supported adapter plugins via the [`create_adapter_plugins.py`](https://github.com/dbt-labs/dbt/blob/47033c459f2c835d81cc845d49ef23e7d19736b6/core/scripts/create_adapter_plugins.py) file. While this file is able to produce a usable adapter plugin, it is not the most user friendly experience as we have noted over time and needed to be updated.

### known issues or possible improvements to be made
- Updating script to generate a new adapter plugin is tricky, must edit numerous template strings in python code, difficult to test and search for all areas changes are needed.
- Not an interactive experience, must know and pass all required arguments to the .py file `$ python create_adapter_plugins.py --sql --title-case=MyAdapter ./ myadapter`
- stuck with defaults, or missing dbt suggested default dependencies
  - Options to set up Github Actions
  - flake8 by default for linting to match other adapters
  - mypy by default or optional for stati type checking
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
        - provides various ways to run program, either from fork/cloning, from a reconized cookiecutter command without cloning, or from within `dbt-core` able to take advantace of bumpversioning.
      - [`pyscaffold`](https://cookiecutter.readthedocs.io/en/1.7.2/overview.html)
        - creates a simple scaffold of project not as flexible as cookiecutter
      - [`yehua`](https://yehua.readthedocs.io/en/latest/)
        - Seems to of had similar functionality to cookiecutter but hasn't been suppoted in quite some time therefore no longer works with pip install, (unusable)

## Decision
After looking at available tooling, we have decided to use `cookiecutter` parsed through .py and generated "adapter" base file from current process and pulled out any information we would need to keep, built out the `cookiecutter.json` based variables that were built by running the .py variables and put them in way to augment things like adapter name to fit into correct place, assign correct ConnectionManager classes based on certain choices, applied file sturcture and dependency list for things dbt wants to suggest be used (ex. tox, flake8,etc.), once base file structure was built out I grabbed examples of the macros that do not have a default version and provided them as a context to be looked at, built out base steps of what all other macros do in general terms to help users make any changes to default action needed, created general docstrings for classes based on offical documentation and implementation.


## Status
proposed

## Consequences

We now have a adapter plugin that takes what our original process did and improves upon it by trying to be more explicit in what needs to be done, and offering helpful tips or references. we have given users the suggested tools we at `dbt` use ourselves, and can refocus towards other more deep dive areas around testing these adapters and making that a more clear process.
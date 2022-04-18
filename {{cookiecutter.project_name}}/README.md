<p align="center">
  <img src="https://raw.githubusercontent.com/dbt-labs/dbt/ec7dee39f793aa4f7dd3dae37282cc87664813e4/etc/dbt-logo-full.svg" alt="dbt logo" width="500"/>
</p>

**[dbt](https://www.getdbt.com/)** enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

dbt is the T in ELT. Organize, cleanse, denormalize, filter, rename, and pre-aggregate the raw data in your warehouse so that it's ready for analysis.

## {{ cookiecutter.project_name }}
This repo contains the base code to help you start to build out your {{ cookiecutter.project_name }} adapter plugin, for more information on how to build out the adapter please follow the [docs](https://docs.getdbt.com/docs/contributing/building-a-new-adapter)

 ** Note ** this `README` is meant to be replaced with what information would be required to use your adpater once your at a point todo so.

 ## Getting Started

 #### Setting up Locally
- run `pip install dev_requirements.txt`.
- cd directory into the `dbt-core` you'd like to be testing against and run `make dev`.

 #### Connect to Github
- run `git init`.
- Connect your lcoal code to a Github repo.

 ## Testing
Testing for adapter connection capablilities
- Once you have your plugin connecting to a database, you can test basic dbt functionality against the by running
```
 python -m pytest tests/functional/adapter/test_basic.py
```

Once your adapter is built out a few options.
- you can use `dbt debug` to troubleshoot issues with macros
- [Jaffle_shop](https://docs.getdbt.com/tutorial/setting-up) is a frinedly beginner project to test adapter compatiablity with dbt functionality.

## Join the dbt Community

- Be part of the conversation in the [dbt Community Slack](http://community.getdbt.com/)
- Read more on the [dbt Community Discourse](https://discourse.getdbt.com)

## Reporting bugs and contributing code

- Want to report a bug or request a feature? Let us know on [Slack](http://community.getdbt.com/), or open [an issue](https://github.com/dbt-labs/dbt-redshift/issues/new)
- Want to help us build dbt? Check out the [Contributing Guide](https://github.com/dbt-labs/dbt/blob/HEAD/CONTRIBUTING.md)

## Code of Conduct

Everyone interacting in the dbt project's codebases, issue trackers, chat rooms, and mailing lists is expected to follow the [dbt Code of Conduct](https://community.getdbt.com/code-of-conduct).
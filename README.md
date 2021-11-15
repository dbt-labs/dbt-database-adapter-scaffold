<p align="center">
  <img src="https://raw.githubusercontent.com/dbt-labs/dbt/ec7dee39f793aa4f7dd3dae37282cc87664813e4/etc/dbt-logo-full.svg" alt="dbt logo" width="500"/>
</p>

**[dbt](https://www.getdbt.com/)** enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

dbt is the T in ELT. Organize, cleanse, denormalize, filter, rename, and pre-aggregate the raw data in your warehouse so that it's ready for analysis.

## dbt-database-adapter-scaffold
The `dbt-database-adapter-scaffold` package is a user-friendly interactive way to build out a new adapter.

## Getting started

#### Running from Github
- [Install cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)
- run `cookiecutter gh:dbt-labs/dbt-database-adapter-scaffold` in console

#### Running Locally
- [Install cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)
- Fork and clone this repo
- Once cloned run cookiecutter path_to_this_file/..

#### Generally
- read the [docs](https://docs.getdbt.com/docs/contributing/building-a-new-adapter) around building a new adapter and follow helpful tips within generated project to build out your new adapter.

## Testing
Testing for adapter connection capablilities
- Please use the `dbt-adapter-tests` these are best for troubleshootting connection and common functionality. 

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
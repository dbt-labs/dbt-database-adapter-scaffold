<p align="center">
  <img src="https://raw.githubusercontent.com/dbt-labs/dbt/ec7dee39f793aa4f7dd3dae37282cc87664813e4/etc/dbt-logo-full.svg" alt="dbt logo" width="500"/>
</p>

**[dbt](https://www.getdbt.com/)** enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

dbt is the T in ELT. Organize, cleanse, denormalize, filter, rename, and pre-aggregate the raw data in your warehouse so that it's ready for analysis.

# dbt-database-adapter-scaffold
The `dbt-database-adapter-scaffold` package is a user-friendly interactive way to build out a new adapter.

> ### :warning: Versioning
> `dbt-core` use semver to denote compatibility and intends to maintain compatibility for database adapters of the same major and minor version. (i.e. any patch version for a given major and minor version) This is a convention used by existing plugins that database adapter plugin developers can opt into during project setup. When generating a scaffold, the project version will include the same major and minor version of the latest stable version of `dbt-core`.

## Getting started

### Local environment setup
- `cd` to where you'd like your adapter to live. the scaffold will create a new folder for your adapter, e.g. `dbt-{myadapter}`. This will be the folder to make into a Git repository
- setup a virtual env
    ```
    python3 -m venv env
    ```
- choose how you would like to run the `dbt-database-adapter-scaffold`
      - [Running from Github](#running-from-github) (recommended)
      - [Running Locally](#running-locally)
- Once you have generated your adapter please continue by using the [`README`]({{cookiecutter.project_name}}/README.md) located within the repo.

#### Running from Github
- Install [cookiecutter](https://cookiecutter.readthedocs.io/) with `pip install cookiecutter` ([guide for alt install methods](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html))
- run `cookiecutter gh:dbt-labs/dbt-database-adapter-scaffold` in console

#### Running Locally
- [Install cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)
- Fork and clone this repo
- Once cloned run cookiecutter `path_to_this_repo/.`

## Join the dbt Community

- Be part of the conversation in the [dbt Community Slack](http://community.getdbt.com/)
- Read more on the [dbt Community Discourse](https://discourse.getdbt.com)

## Reporting bugs and contributing code

- Want to report a bug or request a feature? Let us know on [Slack](http://community.getdbt.com/), or open [an issue](https://github.com/dbt-labs/dbt-redshift/issues/new)
- Want to help us build dbt? Check out the [Contributing Guide](https://github.com/dbt-labs/dbt/blob/HEAD/CONTRIBUTING.md)

## Code of Conduct

Everyone interacting in the dbt project's codebases, issue trackers, chat rooms, and mailing lists is expected to follow the [dbt Code of Conduct](https://community.getdbt.com/code-of-conduct).

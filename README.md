<p align="center">
  <img src="https://raw.githubusercontent.com/dbt-labs/dbt/ec7dee39f793aa4f7dd3dae37282cc87664813e4/etc/dbt-logo-full.svg" alt="dbt logo" width="500"/>
</p>

**[dbt](https://www.getdbt.com/)** enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

dbt is the T in ELT. Organize, cleanse, denormalize, filter, rename, and pre-aggregate the raw data in your warehouse so that it's ready for analysis.

## dbt-database-adapter-scaffold
The `dbt-database-adapter-scaffold` package is a user-friendly interactive way to build out a new adapter.

## Getting started

### Local environment setup
- cd to where you'd like your adapter to live
- setup a virtual env
```
python3 -m venv env
```
- choose how you would like to run the `dbt-database-adapter-scaffold`
      - Running from Github (recommended)
      - Running Locally
- Once you have generated your adapter please continue by using the `README` located within the repo.

#### Running from Github
- [Install cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)
- run `cookiecutter gh:dbt-labs/dbt-database-adapter-scaffold` in console

#### Running Locally
- [Install cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)
- Fork and clone this repo
- Once cloned run cookiecutter path_to_this_file/..

 ### Testing
A suggested process for testing while building out your new adapter might be something like.
- Firstly focus on getting the connection methods and credentials setup correctly and test basic connection with `dbt debug`
- Creating a small project to slowly run and test against locally as you build (will really help once you get to building out unit/integration test implementations) ex. [jaffle_shop](https://github.com/dbt-labs/jaffle_shop) is one we have various instructions and tutorials for (Tutorial)(https://docs.getdbt.com/tutorial/setting-up)
- Work on building up higher-level macros/methods using your small project from step before to test basic adapter functionality by running things like `dbt run` against building views, tables, `dbt test` till you have basic functionality.
- Start incorporating new more `pytest` testing to check against your basic adapter functionality. At this point your adapter will be feature-complete at baseline level.
- Share your adapter to get feedback.
- Continue developing additional features standard to other dbt adapters and adding in more feature based `unit` and `functional` tests or building out adapter specific test functionality/tests.


#### Generally
- read the [docs](https://docs.getdbt.com/docs/contributing/building-a-new-adapter) around building a new adapter and follow helpful tips within generated project to build out your new adapter.

## Join the dbt Community

- Be part of the conversation in the [dbt Community Slack](http://community.getdbt.com/)
- Read more on the [dbt Community Discourse](https://discourse.getdbt.com)

## Reporting bugs and contributing code

- Want to report a bug or request a feature? Let us know on [Slack](http://community.getdbt.com/), or open [an issue](https://github.com/dbt-labs/dbt-redshift/issues/new)
- Want to help us build dbt? Check out the [Contributing Guide](https://github.com/dbt-labs/dbt/blob/HEAD/CONTRIBUTING.md)

## Code of Conduct

Everyone interacting in the dbt project's codebases, issue trackers, chat rooms, and mailing lists is expected to follow the [dbt Code of Conduct](https://community.getdbt.com/code-of-conduct).

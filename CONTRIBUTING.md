# Contributing to `dbt-database-adapter-scaffold`

`dbt-database-adapter-scaffold` is open source software. It is what it is today because community members have opened issues, provided feedback, and [contributed to the knowledge loop](https://www.getdbt.com/dbt-labs/values/). Whether you are a seasoned open source contributor or a first-time committer, we welcome and encourage you to contribute code, documentation, ideas, or problem statements to this project.

1. [About this document](#about-this-document)
2. [Getting the code](#getting-the-code)
3. [Setting up an environment](#setting-up-an-environment)
4. [Running dbt-core in development](#running-dbt-core-in-development)
5. [Testing dbt-core](#testing)
6. [Debugging](#debugging)
7. [Adding or modifying a changelog entry](#adding-or-modifying-a-changelog-entry)
8. [Submitting a Pull Request](#submitting-a-pull-request)

## About this document

There are many ways to contribute to the ongoing development of `dbt-database-adapter-scaffold`, such as by participating in discussions and issues. We encourage you to first read our higher-level document: ["Expectations for Open Source Contributors"](https://docs.getdbt.com/docs/contributing/oss-expectations).

The rest of this document serves as a more granular guide for contributing code changes to `dbt-database-adapter-scaffold` (this repository). It is not intended as a guide for using `dbt-database-adapter-scaffold`, and some pieces assume a level of familiarity with Python development (virtualenvs, `pip`, etc). Specific code snippets in this guide assume you are using macOS or Linux and are comfortable with the command line.

If you get stuck, we're happy to help! Drop us a line in the `#adapter-ecosystem` channel in the [dbt Community Slack](https://community.getdbt.com).

### Notes

- **CLA:** Please note anyone contributing code to `dbt-database-adapter-scaffold` must sign the [Contributor License Agreement](https://docs.getdbt.com/docs/contributor-license-agreements). If you are unable to sign the CLA, the `dbt-database-adapter-scaffold` maintainers will unfortunately be unable to merge any of your Pull Requests. We welcome you to participate in discussions, open issues, and comment on existing ones.

## Getting the code

### Installing git

You will need `git` in order to download and modify the `dbt-core` source code. On macOS, the best way to download git is to just install [Xcode](https://developer.apple.com/support/xcode/).

### External contributors

If you are not a member of the `dbt-labs` GitHub organization, you can contribute to `dbt-database-adapter-scaffold` by forking the `dbt-database-adapter-scaffold` repository. For a detailed overview on forking, check out the [GitHub docs on forking](https://help.github.com/en/articles/fork-a-repo). In short, you will need to:

1. Fork the `dbt-database-adapter-scaffold` repository
2. Clone your fork locally
3. Check out a new branch for your proposed changes
4. Push changes to your fork
5. Open a pull request against `dbt-labs/dbt-database-adapter-scaffold` from your forked repository

### dbt Labs contributors

If you are a member of the `dbt-labs` GitHub organization, you will have push access to the `dbt-database-adapter-scaffold` repo. Rather than forking `dbt-database-adapter-scaffold` to make your changes, just clone the repository, check out a new branch, and push directly to that branch.

## Setting up an environment

There are some tools that will be helpful to you in developing locally. While this is the list relevant for `dbt-database-adapter-scaffold` development, many of these tools are used commonly across open-source python projects.

### Tools

These are the tools used in `dbt-database-adapter-scaffold` development and testing:

- [`pytest`](https://docs.pytest.org/en/latest/) to define, discover, and run tests
- [GitHub Actions](https://github.com/features/actions) for automating tests and checks, once a PR is pushed to the `dbt-database-adapter-scaffold` repository

A deep understanding of these tools in not required to effectively contribute to `dbt-database-adapter-scaffold`, but we recommend checking out the attached documentation if you're interested in learning more about each one.

#### Virtual environments

We strongly recommend using virtual environments when developing code in `dbt-database-adapter-scaffold`. We recommend creating this virtualenv
in the root of the `dbt-database-adapter-scaffold` repository. To create a new virtualenv, run:
```sh
python3 -m venv env
source env/bin/activate
```

This will create and activate a new Python virtual environment.

## Testing

Once you're able to manually test that your code change is working as expected, it's important to run existing automated tests, as well as adding some new ones. These tests will ensure that:
- Your code changes do not unexpectedly break other established functionality
- Your code changes can handle all known edge cases
- The functionality you're adding will _keep_ working in the future

### Test commands

With a virtualenv active and dev dependencies installed you can do things like:

```sh
# run all unit tests in a file
python3 -m pytest tests/template_test.py
# run a specific unit test
python3 -m pytest tests/template_test.py::bake_in_temp_dir
```

> See [pytest usage docs](https://docs.pytest.org/en/6.2.x/usage.html) for an overview of useful command-line options.

## Submitting a Pull Request

Code can be merged into the current development branch `main` by opening a pull request. A `dbt-database-adapter-scaffold` maintainer will review your PR. They may suggest code revision for style or clarity, or request that you add unit or integration test(s). These are good things! We believe that, with a little bit of help, anyone can contribute high-quality code.

Automated tests run via GitHub Actions. If you're a first-time contributor, all tests (including code checks and unit tests) will require a maintainer to approve.

Once all tests are passing and your PR has been approved, a `dbt-database-adapter-scaffold` maintainer will merge your changes into the active development branch. And that's it! Happy developing :tada:

Sometimes, the content license agreement auto-check bot doesn't find a user's entry in its roster. If you need to force a rerun, add `@cla-bot check` in a comment on the pull request.

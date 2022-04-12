# Un comment and create your fixture for python test

# import pytest
# import os
# import json

# # Import the fuctional fixtures as a plugin
# # Note: fixtures with session scope need to be local

# pytest_plugins = ["dbt.tests.fixtures.project"]

# # The profile dictionary, used to write out profiles.yml
# @pytest.fixture(scope="class")
# def dbt_profile_target():
#     pass

#     '''
#     example of what return object might look like

#     {
#       type: {{cookiecutter.adapter_name}}
#       user:
#       database:
#       etc..
#     }
#     '''
from contextlib import contextmanager
import pytest
from cookiecutter.utils import rmtree

# @contextmanager
# def bake_in_temp_dir(cookies, *args, **kwargs):
#     extra_context = kwargs.setdefault('extra_context',{})
#     extra_context.setdefault('project_name','myproject')
#     result = cookies.bake(*args, **kwargs)
#     try:
#         yield result
#     finally: 
#         rmtree(str(result.project))

def test_bake_project(cookies):
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "dbt-myadapter"
    assert result.project_path.is_dir()

    # The `project` attribute is deprecated
    assert result.project.basename == "dbt-myadapter"
    assert result.project.isdir()


def test_bake_project_fail(cookies):
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name != "hello_world"
    assert result.project_path.is_dir()

    # The `project` attribute is deprecated
    assert result.project.basename != "hello_world"
    assert result.project.isdir()



    



import json
import pytest
from contextlib import contextmanager
from cookiecutter.utils import rmtree

@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    extra_context = kwargs.setdefault('extra_context', {})
    extra_context.setdefault('adapter_name', 'my project')
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project_path))

def test_bake_project_default(cookies):
    """bake and test against default values of cookiecutter.json"""
    result = cookies.bake()
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "dbt-myadapter"
    assert result.project_path.is_dir()
    # looks for files in generated project
    found_toplevel_files = [f.name for f in result.project_path.glob('*')]
    assert  'dbt' in found_toplevel_files
    assert 'setup.py' in found_toplevel_files
    assert 'tox.ini' in found_toplevel_files
    assert 'test' in found_toplevel_files
    

def test_bake_project_fail(cookies):
    """bake and test against new words, if passes means its changing values in template"""
    result = cookies.bake()
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name != "hello_world"
    assert result.project_path.is_dir()
    # looks for files in generated project
    found_toplevel_files = [f.name for f in result.project_path.glob('*')]
    assert  'dbt' in found_toplevel_files
    assert 'setup.py' in found_toplevel_files
    assert 'tox.ini' in found_toplevel_files
    assert 'test' in found_toplevel_files

def test_without_internationalization(cookies):
    with bake_in_temp_dir(
        cookies,
        extra_context={'use_i18n': 'No'}
    ) as result:
        assert result.project_path.joinpath('dbt/adapters').is_dir()




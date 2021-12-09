from contextlib import contextmanager
import pytest
from cookiecutter.utils import rmtree

@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    extra_context = kwargs.setdefault('extra_context',{})
    extra_context.setdefault('project_name','myproject')
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally: 
        rmtree(str(result.project))

def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.exit_code == 0
        assert result.exception is None
        assert result.project.isdir()
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'test' in found_toplevel_files
        assert 'setup.py'in found_toplevel_files



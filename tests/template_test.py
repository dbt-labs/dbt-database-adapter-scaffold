import re
from contextlib import contextmanager
from cookiecutter.utils import rmtree

@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project_path)) 

def test_bake_project_default_adapter_name(cookies):
    """bake and test against default values of cookiecutter.json, adapter_name, and top level files created"""
    with bake_in_temp_dir(cookies) as result:
        assert result.exit_code == 0
        assert result.exception is None
        assert result.context['adapter_name'] == "My Adapter"
        assert result.context['adapter_name'] != '123444'
        assert result.project_path.is_dir()
        # looks for files in generated project
        found_toplevel_files = [f.name for f in result.project_path.glob('*')]
        print(found_toplevel_files)
        assert '.github' in found_toplevel_files
        assert  'dbt' in found_toplevel_files
        assert 'setup.py' in found_toplevel_files
        assert 'tox.ini' in found_toplevel_files
        assert 'test' in found_toplevel_files
    
def test_bake_direcotry_name(cookies):
    """bake and test against new words, if passes means its changing values in template"""
    with bake_in_temp_dir(cookies) as result:
        assert result.exit_code == 0
        assert result.exception is None
        assert result.context['directory_name'] == 'myadapter'
        assert result.context['directory_name'] != "hello_world"
       
def test_bake_deafult_adapter_src(cookies):
    '''bake and test default version of adapter_src is sql'''
    with bake_in_temp_dir(cookies) as result:
        assert result.exit_code == 0
        assert result.exception is None
        assert result.context['adapter_src'] =='sql'
        assert result.context['adapter_src'] != 'base'
        assert result.context['adapter_src'] != '1'
        assert result.context['adapter_src'] != '2'

def test_bake_adapter_src_base(cookies):
    '''bake and test adapter_src can register change from sql to base'''
    with bake_in_temp_dir(cookies,extra_context={'adapter_src': 'base'}) as result:
        assert result.exit_code == 0
        assert result.exception is None
        assert result.context['adapter_src'] == 'base'
        assert result.context['adapter_src'] != 'sql'

def test_bake_author_default(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.context['author'] == "<INSERT AUTHOR HERE>"

def test_bake_author_change(cookies):
    with bake_in_temp_dir(cookies,extra_context={'author':'John Doe'}) as result:
        assert result.context['author'] == 'John Doe'
        assert result.context['author'] != 'JOhn Dooe'

def test_bake_email_default(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.context['author_email'] == "<INSERT EMAIL HERE>"

def test_bake_email_change(cookies):
    with bake_in_temp_dir(cookies,extra_context={'author_email':'John.D@test.com'}) as result:
        assert result.context['author_email'] == 'John.D@test.com'
        assert result.context['author_email'] != 'J@hn.d@test.com'
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        assert re.fullmatch(regex,result.context['author_email'])

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

def test_bake_project_adapter_name(cookies):
    """bake and test against default values of cookiecutter.json, adapter_name, and top level files created"""
    with bake_in_temp_dir(cookies, extra_context={ "adapter_name": "MyAdapter" }) as result:
        assert result.exit_code == 0
        assert result.exception is None
        assert result.context["adapter_name"] == "MyAdapter"
        assert result.project_path.is_dir()
        # looks for files in generated project
        found_toplevel_files = [f.name for f in result.project_path.glob('*')]
        assert ".github" in found_toplevel_files
        assert  "dbt" in found_toplevel_files
        assert "setup.py" in found_toplevel_files
        assert "tox.ini" in found_toplevel_files
        assert "tests" in found_toplevel_files

def test_bake_project_name(cookies):
    """bake and test against new words, if passes means its changing values in template"""
    with bake_in_temp_dir(cookies, extra_context={ "adapter_name":"MyAdapter" }) as result:
        assert result.exit_code == 0
        assert result.exception is None
        assert result.context["project_name"] == "dbt-myadapter"

def test_bake_deafult_is_sql_adapter(cookies):
    """bake and test default version of is_sql_adapter is true"""
    with bake_in_temp_dir(cookies) as result:
        assert result.exit_code == 0
        assert result.exception is None
        assert result.context["is_sql_adapter"] =="true"

def test_bake_is_sql_adapter_base(cookies):
    """bake and test is_sql_adapter can register change from true to false"""
    with bake_in_temp_dir(cookies, extra_context={ "is_sql_adapter":"false" }) as result:
        assert result.exit_code == 0
        assert result.exception is None
        assert result.context["is_sql_adapter"] == "false"

def test_bake_author_default(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.context["author"] == "<INSERT AUTHOR HERE>"

def test_bake_author_change(cookies):
    with bake_in_temp_dir(cookies, extra_context={ "author":"John Doe" }) as result:
        assert result.context["author"] == "John Doe"


def test_bake_email_default(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.context["author_email"] == "<INSERT EMAIL HERE>"

def test_bake_email_change(cookies):
    with bake_in_temp_dir(cookies, extra_context={ "author_email":"John.D@test.com" }) as result:
        assert result.context["author_email"] == "John.D@test.com"
        assert result.context["author_email"] != "J@hn.d@test.com"
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        assert re.fullmatch(regex,result.context["author_email"])

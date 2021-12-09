import json
import pytest




def test_bake_project_default(cookies):
    result = cookies.bake()
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "dbt-myadapter"
    assert result.project_path.is_dir()


def test_bake_project_fail(cookies):
    result = cookies.bake()
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name != "hello_world"
    assert result.project_path.is_dir()






    



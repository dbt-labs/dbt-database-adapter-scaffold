import pytest

from dbt.tests.adapter.basic.test_base import BaseSimpleMaterializations
from dbt.tests.adapter.basic.test_singular_tests import BaseSingularTests
from dbt.tests.adapter.basic.test_singular_tests_ephemeral import (
    BaseSingularTestsEphemeral
)
from dbt.tests.adapter.basic.test_empty import BaseEmpty
from dbt.tests.adapter.basic.test_ephemeral import BaseEphemeral
from dbt.tests.adapter.basic.test_incremental import BaseIncremental
from dbt.tests.adapter.basic.test_generic_tests import BaseGenericTests
from dbt.tests.adapter.basic.test_snapshot_check_cols import BaseSnapshotCheckCols
from dbt.tests.adapter.basic.test_snapshot_timestamp import BaseSnapshotTimestamp
from dbt.tests.adapter.basic.test_adapter_methods import BaseAdapterMethod


class TestSimpleMaterializations{{ cookiecutter.adapter_name }}(BaseSimpleMaterializations):
    pass


class TestSingularTests{{ cookiecutter.adapter_name }}(BaseSingularTests):
    pass


class TestSingularTestsEphemeral{{ cookiecutter.adapter_name }}(BaseSingularTestsEphemeral):
    pass


class TestEmpty{{ cookiecutter.adapter_name }}(BaseEmpty):
    pass


class TestEphemeral{{ cookiecutter.adapter_name }}(BaseEphemeral):
    pass


class TestIncremental{{ cookiecutter.adapter_name }}(BaseIncremental):
    pass


class TestGenericTests{{ cookiecutter.adapter_name }}(BaseGenericTests):
    pass


class TestSnapshotCheckCols{{ cookiecutter.adapter_name }}(BaseSnapshotCheckCols):
    pass


class TestSnapshotTimestamp{{ cookiecutter.adapter_name }}(BaseSnapshotTimestamp):
    pass


class TestBaseAdapterMethod{{ cookiecutter.adapter_name }}(BaseAdapterMethod):
    pass

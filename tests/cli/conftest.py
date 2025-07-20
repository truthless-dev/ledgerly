from click.testing import CliRunner
from pytest import fixture


@fixture
def runner():
    return CliRunner()

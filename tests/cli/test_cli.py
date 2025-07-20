from ledgerly.cli.main import cli


class TestCli:

    def test_can_show_main_help(self, runner):
        result = runner.invoke(cli, "-h")
        assert result.exit_code == 0

    def test_can_show_version_info(self, runner):
        result = runner.invoke(cli, "--version")
        assert result.exit_code == 0

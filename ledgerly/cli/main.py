import click


context_settings = {
    "help_option_names": ["-h", "--help"],
}


@click.group(
    context_settings=context_settings,
)
@click.version_option(
    prog_name="Ledgerly",
    message="%(prog)s v%(version)s",
)
@click.pass_context
def cli(ctx):
    """A personal finance application"""
    pass


if __name__ == "__main__":
    cli()

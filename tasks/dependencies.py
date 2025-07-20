from invoke import task


@task(
    name="install",
    aliases=("inst",),
)
def install_all(c):
    """Install the project along with all its dependencies"""
    c.run("poetry install && pre-commit install")

from pathlib import Path

from invoke import task


DIR_ROOT = Path(__file__).parent.parent


@task(default=True)
def all(c):
    """Run all tests"""
    c.run(f'pytest "{DIR_ROOT}"')

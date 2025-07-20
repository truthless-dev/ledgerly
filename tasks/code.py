from pathlib import Path

from invoke import task


DIR_ROOT = Path(__file__).parent.parent

TOOLS = [
    {
        "name": "Flake8",
        "check_command": f'flake8 "{DIR_ROOT}"',
    },
    {
        "name": "Black",
        "check_command": f'black --check "{DIR_ROOT}"',
        "format_command": f'black "{DIR_ROOT}"',
    },
    {
        "name": "Isort",
        "check_command": f'isort --check "{DIR_ROOT}"',
        "format_command": f'isort "{DIR_ROOT}"',
    },
]


def _pre(c, tool):
    c.run(f"echo -n \"{tool['name']}... \"")


def _check(c, tool):
    return c.run(tool["check_command"], hide=True, warn=True)


def _format(c, tool):
    return c.run(tool["format_command"], hide=True, warn=True)


def _post(c, result):
    if result.ok:
        c.run("echo pass.")
        return
    c.run("echo fail.")
    if len(result.stdout) > 0:
        c.run(f'echo -n "{result.stdout}"')
    if len(result.stderr) > 0:
        c.run(f'echo -n "{result.stderr}"')
    c.run("echo")


@task
def check(c):
    """Check formatting without modifying files"""
    for tool in TOOLS:
        _pre(c, tool)
        result = _check(c, tool)
        _post(c, result)


@task(
    default=True,
)
def format(c):
    """Format all code"""
    for tool in TOOLS:
        if "format_command" not in tool:
            continue
        _pre(c, tool)
        result = _format(c, tool)
        _post(c, result)

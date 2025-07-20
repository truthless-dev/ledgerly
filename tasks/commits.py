from invoke import task


@task
def check(c, rev_range: str | None = None):
    """Validate commit messages"""
    if rev_range is None:
        rev_range = "HEAD"
    c.run(f"cz check --rev-range {rev_range}")


@task(default=True)
def commit(c, all: bool = False):
    """Commit changes"""
    cmd = "cz commit" if not all else "cz commit --all"
    c.run(cmd)

from pathlib import Path

from invoke import task


DIR_ROOT = Path(__file__).parent.parent
DIR_DOCS = DIR_ROOT / "docs"
DIR_DOCS_SOURCE = DIR_DOCS
DIR_DOCS_BUILD = DIR_DOCS / "_build"


@task
def clean(c):
    """Remove previous docs builds"""
    c.run(f"sphinx-build -M clean {DIR_DOCS_SOURCE} {DIR_DOCS_BUILD}")


@task(
    name="html",
    pre=(clean,),
    default=True,
)
def build_html(c):
    """Build HTML docs"""
    c.run(f"sphinx-build -M html {DIR_DOCS_SOURCE} {DIR_DOCS_BUILD}")

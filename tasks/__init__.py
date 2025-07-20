from invoke import Collection

from . import (
    code,
    commits,
    dependencies,
    documentation,
    tests,
)


ns = Collection()
ns.add_collection(code)
ns.add_collection(commits, name="c")
ns.add_collection(documentation, name="doc")
ns.add_collection(tests, name="test")
ns.add_task(dependencies.install_all, default=True)

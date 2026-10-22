# Python port template

**The R ecosystem, reimagined for Python.**

A small starting point for future PyRverse packages: typed Python, modern
packaging, reference-test conventions, and automated checks.

**Status: infrastructure.** This repository does not port an R package, establish
scientific parity, or provide a production scientific method. Its `center`
function is a teaching example; its reference values were calculated by hand.

## Start developing

Python 3.11 or newer is required. Create and activate an isolated environment:

```sh
python -m venv .venv
# macOS / Linux:
source .venv/bin/activate
# Windows PowerShell instead:
# .venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m pytest
python -m ruff check .
python -m ruff format --check .
python -m mypy
python -m build
```

Run the small example with `python examples/basic_usage.py`:

```python
from pyrverse_port import center

center([1.0, 2.0, 6.0])  # (-2.0, -1.0, 3.0)
```

Development dependency ranges live in `pyproject.toml`. For a reproducible
experiment, record the exact environment with `python -m pip freeze` and retain
the Python version, operating system, input checksums, and run command. Version
ranges alone are not an immutable environment lock.

## Make it your own

1. Create a repository from this template or copy the scaffold into a new project.
2. Rename the distribution in `pyproject.toml` and the `src/pyrverse_port` import
   package; update imports, URLs, CI wheel-install name, and documentation.
3. Describe one scientifically useful scope and complete
   [PROVENANCE.md](PROVENANCE.md) before importing or translating upstream code.
4. Review licensing for that specific port. The scaffold's MIT license does not
   determine the license of future translated code, data, or documentation.
5. Replace the teaching example with an API specification, implementation,
   reproducible reference generator, and tests with justified tolerances.
6. Publish a package only after scientific and engineering review. There is no
   automatic package publishing workflow here.

## Repository map

| Path | Purpose |
| --- | --- |
| `src/` | Typed installable package and `py.typed` marker |
| `tests/` | Behavioral tests and a reference comparison pattern |
| `examples/` | A runnable usage example |
| `benchmarks/` | An optional, local timing exercise |
| `docs/` | API, validation, licensing, and release guidance |
| `.github/` | Small CI matrix and monthly dependency update checks |

See the [documentation](docs/README.md) and
[contribution guide](CONTRIBUTING.md). CI covers Python 3.11–3.14, linting,
formatting, type checking, source/wheel builds, and tests against the built wheel.
Passing these checks validates the scaffold, not any scientific method.

## Attribution and license

Original scaffold code is provided under the [MIT license](LICENSE).
No upstream R source code or datasets are included. Preserve required notices
when reusing this scaffold and assess additional material independently.

PyRverse is an independent community effort and has no implied affiliation
with upstream authors or scientific software organizations.

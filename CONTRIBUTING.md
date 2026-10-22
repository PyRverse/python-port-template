# Contributing

Improvements to packaging, documentation, test patterns, and reproducibility are
welcome. Open an issue describing the problem and a minimal example, or send a
small pull request with a clear explanation and relevant tests. Do not include
private datasets, credentials, or identifiable research data.

Follow the [development commands](README.md#start-developing), keep new APIs typed,
and explain user-visible changes. Review should check correctness, edge cases,
documentation, attribution, and the scope of any validation claim. A passing test
suite alone does not establish a method's scientific validity.

Before starting a port, evaluate existing Python implementations, read the
upstream documentation and literature, identify original authors, and agree on
the supported statistical behavior. Complete [PROVENANCE.md](PROVENANCE.md) and
the [licensing review](docs/licensing.md). Generate small reference outputs using
a pinned upstream environment, with dataset permission and documented random
seeds. Choose tolerances from numerical and scientific reasoning; do not relax
them merely to obtain a passing test. See [validation](docs/validation.md).

Keep benchmark work optional and lightweight. Documentation contributions need
not add tests unless they change runnable examples. Include the exact commands
and results used to verify a code change in the pull request.

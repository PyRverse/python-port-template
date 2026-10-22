# Documentation

- [Example API](api.md)
- [Reference validation](validation.md)
- [Licensing and attribution](licensing.md)
- [Release checklist](release-checklist.md)
- [Provenance worksheet](../PROVENANCE.md)

The template intentionally uses plain Markdown and a small runtime dependency
surface. Add a documentation generator when a real package needs one.

The CI action majors were checked against the official
[checkout](https://github.com/actions/checkout) and
[setup-python](https://github.com/actions/setup-python) documentation on
2026-10-22. Dependabot checks both pip dependencies and GitHub Actions monthly;
its configuration follows GitHub's
[options reference](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference).
Review dependency updates before merging them.

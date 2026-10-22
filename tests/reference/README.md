# Reference fixtures

`center.json` is a hand-calculated teaching fixture, not an R-generated result.
The zero tolerances apply only to these exactly representable values.

For a real method, replace or supplement it with small reference fixtures and
record upstream package version and source revision, R version, dependencies,
platform and numerical libraries, RNG kind and seed, generator command, data
license, input/output checksums, and the reason for each tolerance. Commit the
generator script alongside its outputs. Never silently replace expected results
to make tests pass. See [validation](../../docs/validation.md).

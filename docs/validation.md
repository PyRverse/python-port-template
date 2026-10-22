# Reference validation

Use a reproducible reference environment, not a plausible-looking answer, as
evidence for a real port. The supplied fixture is explicitly hand-calculated and
only demonstrates loading expected values and setting comparison tolerances.

For each supported behavior:

1. Record upstream package, version, revision, authors, citation, and relevant
   algorithm options. Preserve the generator and full session information.
2. Document dataset provenance, license, transformations, and checksums. Prefer
   small synthetic inputs where scientifically meaningful.
3. Store outputs with stable row/column identifiers and adequate numeric
   precision. Record missing-value and nonfinite-value conventions.
4. Explain absolute and relative tolerances per output. Include zero, very small,
   and large magnitudes; distinguish rounding from substantive disagreement.
5. Test statistical behavior as well as arrays: convergence, warnings, effect
   estimates, p-values, multiple-testing decisions, and model assumptions where
   relevant. Include singular, sparse, constant, and otherwise degenerate inputs.
6. Report failures and limitations. Scope claims to the tested versions, inputs,
   platforms, and settings; do not advertise exact parity without evidence.

For stochastic methods, document random-number generators and seeds; matching
seeds across languages does not ensure identical random streams. Consider
distributional or invariant checks when pointwise identity is inappropriate.

Reference execution may require R during validation. A native Python runtime
package should keep that requirement separate from normal installation.

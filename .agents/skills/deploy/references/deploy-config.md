# Deployment contract

Customize this file before using `$deploy` to mutate an environment.

## Environments

| Environment | Deployment command or tool | Approval owner | Health signal |
| --- | --- | --- | --- |
| Development | Define for this project | Project team | Define for this project |
| Staging | Define for this project | Project team | Define for this project |
| Production | Define for this project | Service owner | Define for this project |

## Required checks

For each target, replace the example cells above with the exact account, region or namespace and its accountable team. Record the working directory, command or pipeline identifier, prerequisites and a read-only check that confirms the selected destination. State where operators obtain credentials by reference.

Identify the deployable unit and immutable identifier. This may be a package digest, dataset snapshot, static asset manifest or configuration revision. Record the source revision, builder and verification method. When a team adopts a supply-chain assurance level, specify its track, level and supporting evidence using [SLSA 1.2](https://slsa.dev/spec/v1.2/).

- Define the build, test, security, and migration checks required for each environment.
- For production, link the applicable security and privacy checks and approved exceptions from the [adoption standard](../../../../docs/standards/security-privacy.md#review-changes-and-releases).
- Define the deployable artifact or revision identifier and how it is verified.
- Define whether migrations are backward-compatible and how they are ordered relative to application rollout.

## Rollback

Describe the rollout stages, initial population, and observation window. For each stage, specify the query or user journey, acceptable range, minimum sample and action on missing evidence. For a data pipeline, compare record counts and freshness at the same checkpoint. For an interactive workflow, verify completion through the released entry point. Link the service's recovery objectives and exercise results using the [operational readiness guide](../../../../docs/standards/operational-readiness.md).

Identify any point after which restoring an earlier artifact would misread new state. Document the compatible roll-forward artifact or data recovery procedure, the owner who can run it, and the reconciliation check for writes received during the transition.

- Define the rollback command or platform procedure.
- Define the last known-good artifact source.
- Define the signals and thresholds that trigger rollback.

## Secrets

List environment variable or secret-manager key names only. Never store secret values in this file.

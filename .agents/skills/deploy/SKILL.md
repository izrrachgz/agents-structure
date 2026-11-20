---
name: deploy
description: Prepare, validate, execute, or verify a deployment using this repository's environment contract. Use for releases and deployments; require explicit approval before production mutations.
---

# Deploy

Use the release request to identify its intended outcome. A readiness assessment should produce a decision with evidence. An execution request should also identify the target, immutable revision and authorized scope.

1. Resolve the destination using the contract's read-only target check. Match the candidate's identifier to the revision that passed verification. Include independent units such as configuration, schema or assets when they ship on different schedules.
2. Check whether old and new consumers can coexist during rollout. For persisted state, identify the last reversible step and how writes made after that step would be recovered.
3. Apply the contract's stage criteria. If a release command times out, inspect the platform's recorded revision and rollout status before deciding whether a retry is safe.
4. Return a release record with the intended and observed revisions, stage reached, health measurements and observation window. Record whether the outcome is verified, still progressing, rolled back or requires operator action.

Read [references/deploy-config.md](references/deploy-config.md) before planning or executing a deployment.

Determine the target environment, artifact or revision, required checks, rollback path, and expected health signals. Stop if required deployment configuration is still unspecified.

Preparation and read-only validation may proceed within the user's requested scope. Obtain explicit approval immediately before a production mutation, traffic shift, destructive migration, or irreversible release action.

After execution, verify the declared health signals and report the deployed revision, environment, validation evidence, and rollback status. Never print secrets or copy them into repository files.

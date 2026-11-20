# Operating and recovering a component

Use this guide for components with an operator, a production dependency or persistent state. Keep the resulting values in the team's existing runbook. Link that runbook from the deployment contract. The team that can act on a signal should own its definition.

## Define a signal that reflects user impact

Name the operation, the population measured, the source of measurements and the action an operator will take. For a UI, a successful page load may still leave users unable to submit a form. For a batch pipeline, a healthy process can still publish yesterday's data. Measure successful task completion or the age of the last reconciled publication as appropriate.

For each service objective, specify the numerator and denominator or measured distribution, the target, the time window, exclusions and expected reporting delay. Define how an operator distinguishes no traffic from missing telemetry. Record the dashboard or query, the escalation route, and the first read-only diagnostic check. For logs, identify fields safe to retain, correlation identifiers, retention period and authorized readers.

## Model failure and recovery

| Situation | What the runbook should establish | Evidence to retain |
| --- | --- | --- |
| A dependency slows or fails | Deadline, degraded user experience, retry owner, load limit and signal to restore normal operation | A bounded failure exercise showing downstream recovery and queue drainage |
| A stateful component becomes unavailable | Recovery time objective (maximum acceptable outage), recovery point objective (maximum acceptable data loss), backup scope and restore owner | Date and duration of an isolated restore, recovered checkpoint and reconciled business records |
| Processing stops halfway | Commit boundary, durable checkpoint, duplicate handling and procedure for resuming outstanding work | A replay or reconciliation result showing which items completed exactly as intended |
| A schema or configuration change interrupts service | Compatible application versions, last reversible step, and conditions for roll-forward or rollback | Rehearsal with representative state and a recorded decision point |

## Handoff after a recovery exercise

Record the scenario, revision, elapsed recovery time, observed data gap and unresolved customer impact. Compare actual results with the team's objectives. Assign a follow-up owner and verification date for any missed objective. Keep sensitive incident evidence in the access-controlled system referenced by the runbook.

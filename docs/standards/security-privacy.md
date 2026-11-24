# Security and privacy adoption standard

Projects adopting this scaffold must design, build, operate, and retire their software in accordance with the applicable requirements of ISO/IEC 27001:2022, including Amendment 1:2024, and ISO/IEC 27701:2025. Implement and verify the applicable controls to the fullest extent possible. Record unmet requirements and work through the gap and release process below. Use the published editions to determine applicability and assess conformity. [ISO/IEC 27001:2022](https://www.iso.org/standard/27001) · [2024 amendment](https://www.iso.org/standard/88435.html) · [ISO/IEC 27701:2025](https://www.iso.org/standard/27701)

## Establish scope and ownership

- Identify the adopting organization's information security management system (ISMS) and privacy information management system (PIMS) owners. Link the approved scopes, policies, measurable objectives, and responsible teams from the project runbook. Identify the security program and controls that protect personal information within the PIMS scope. If a management system has yet to be established, assign an owner and track its establishment as a gap.
- Record which components, environments, development and build systems, operators, data, and suppliers are in scope. Identify controls provided by a shared platform or supplier and who verifies that coverage applies to this software. Record the boundaries and rationale for each scope.
- Identify stakeholder needs and applicable legal, regulatory, and contractual obligations. Record whether climate change is relevant to the ISMS and identify any related stakeholder requirements. For the PIMS, assess where the organization acts as a personally identifiable information (PII) controller or processor. Document the basis for any scope without PII processing. [ISO/IEC 27001 amendment](https://www.iso.org/standard/88435.html) · [ISO/IEC 27701:2025](https://www.iso.org/standard/27701)

## Assess risks and choose controls

- Assess information security risks to confidentiality, integrity, and availability, and privacy risks to the people whose information is processed. Record the scenario, affected assets or people, likelihood, impact, risk owner, treatment, residual risk, and approval. Reassess when scope, processing, supplier responsibilities, or material risks change.
- Maintain or link each management system's Statement of Applicability and risk treatment plan. Compare necessary controls with the reference controls in the relevant edition, including Annex A, and account for the project's PII processing roles. Record necessary controls, their inclusion rationale and implementation status, and the reason for exclusions. Include any additional controls needed to treat the identified risks. [ISO/IEC 27001 Statement of Applicability guidance](https://committee.iso.org/files/live/sites/jtc1sc27/files/resources/ISO-IECJTC1-SC27-WG1_N3298_Auditing%20Practices%20Note%20-%20SoA.pdf) · [ISO/IEC 27701:2025](https://www.iso.org/standard/27701)
- Maintain a traceable record for each applicable software control. Record its standard and control reference, affected component, accountable owner, implementation or inherited control, verification method and evidence, and current status. Link existing records when they provide the same information.

## Implement and verify the software controls

Use the risks and Statements of Applicability to select the checks for the software. Assign an owner and retain evidence proportionate to the risk. Use the existing test and operations practices to define observable results. [Testing standard](testing.md) · [Operational readiness guide](operational-readiness.md)

| Area | What to implement where applicable | Example evidence |
| --- | --- | --- |
| Identity and access | Limit human and service access to authorized roles. Manage privileged access and secrets, and enforce authorization at resource boundaries. | An authorization test that denies cross-tenant access, a privileged role review, and a recorded credential rotation. |
| Secure development and supply chain | Review security-relevant designs and changes. Verify builds and releases, track vulnerable dependencies, and assign supplier and remediation responsibilities. | A reviewed threat model, a dependency finding with remediation evidence, and an artifact linked to its verified source revision. |
| Data and telemetry protection | Classify data and protect it in storage, in transit, and in derived copies. Limit PII in telemetry and test data. Restrict access to audit records and manage their retention. | Encryption and key access evidence, and a test showing sensitive fields are absent from logs. |
| PII processing and lifecycle | Inventory processing purposes, PII categories, recipients, locations, transfers, and retention. Document the lawful basis and transfer safeguards where required. Apply minimization, deletion, and applicable notices, choices, and individual rights. Where acting as a processor, follow documented controller instructions and account for authorized subprocessors and support obligations. | A reviewed data-flow record, a privacy impact assessment when applicable, a rights-request exercise, and a deletion test that covers downstream copies and restore behavior. |
| Incident response and recovery | Assign incident and privacy breach responsibilities, notification paths, and recovery objectives. Exercise containment and recovery, and review outcomes. | A security or privacy incident exercise and a restore result measured against recovery objectives. |

## Review changes and releases

- At design and change review, identify affected controls and risks. Update evidence when a change affects access, data handling, suppliers, deployment, or the ability to detect and recover from incidents.
- Before production release, link the required checks and their results to the release revision. Record any gap with its affected requirement, impact, interim mitigation, residual risk, decision owner, remediation owner, and review or expiry date. Keep accepted gaps open until corrected and verified.
- Release only when applicable legal and contractual obligations are satisfied and the required checks pass or a permitted exception has been approved by the responsible risk owner and any required security or privacy approver. Record the release decision in the existing deployment process. [Deployment contract](../../.agents/skills/deploy/references/deploy-config.md)

## Maintain evidence and assess conformity

Schedule control monitoring, internal audits, and management reviews. Retain their results and corrective actions. Track each finding to a responsible owner and verify the effectiveness of the correction. Store sensitive evidence in an access-controlled system and link to it from the project records.

Assess conformity against the full applicable requirements for the documented ISMS and PIMS scopes. Use conformity claims only when the assessment supports them. Use certification claims only for the scope covered by a valid certificate issued by a certification body. [ISO certification guidance](https://www.iso.org/certification.html)

# API conventions

## Describe the contract from the consumer's perspective

Include the owner, consumer, supported versions, input and output examples, and the point at which success is durable. Specify field meanings, units, time zone, precision, identity, ordering, bounds, and the differences among absent, empty and null values. Publish a failure example that tells the consumer whether retrying is safe and how to correlate a failure with operator diagnostics.

| Boundary | Additional details to include |
| --- | --- |
| HTTP | Method, path, authorization scope, content type, status codes, pagination stability, cache behavior and concurrency conditions. Use [OpenAPI 3.2.1](https://spec.openapis.org/oas/v3.2.1.html) where supported. For structured errors using [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457), document problem types and extension fields that clients can rely on. |
| Events | Sender, receiver, channel, message identity, schema, delivery guarantees, ordering scope, replay window and handling of unprocessable messages. [AsyncAPI 3.1.0](https://www.asyncapi.com/docs/reference/specification/v3.1.0) describes channels, operations and messages. Record broker-specific guarantees alongside the description. |
| Files, views and datasets | Encoding, keys, row meaning, freshness, completeness marker, late corrections, deletion signals and the owner's reconciliation method |
| Commands and libraries | Arguments, defaults, return and exit semantics, diagnostic output, side effects, concurrency guarantees and compatibility of persisted results |

## Evolve a contract

Inventory the readers and writers that can coexist during rollout. Check an old consumer with new output and a new consumer with old input when both combinations are supported. An added enum value can break an exhaustive consumer even when the schema still validates. For a breaking change, identify the replacement, migration example, supported overlap, usage signal and owner of retirement. Pin the description format to the version your validation and generation tools can read.

## Implementation conventions

- Preserve backward compatibility unless the task explicitly authorizes a breaking change.
- Validate untrusted input at the boundary and return stable, actionable errors without leaking internals or secrets.
- Keep authentication separate from authorization, and enforce authorization on the server for every protected operation.
- Use consistent resource names, status semantics, pagination, idempotency, and error shapes across neighboring endpoints.
- Treat retries and duplicate delivery as normal for networked systems; make mutating operations idempotent where the domain permits it.
- Update contract tests and public documentation whenever request, response, event, or error behavior changes.

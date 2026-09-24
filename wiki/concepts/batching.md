---
type: concept
sources: [ch09-inference-service-optimization]
---
# Batching

Batching is a service-level [[inference-optimization]] that groups multiple simultaneous inference requests together for joint processing instead of handling each separately, reducing cost by improving throughput. The tradeoff is latency: like putting passengers on a bus instead of separate cars, a bus moves more people but can make each person's journey longer; done intelligently, the latency impact can be minimal (AIE p.440).

Three main techniques exist. **Static batching** groups a fixed number of inputs and waits until the batch is full before processing, so the first request is delayed until the last one arrives, however late (AIE p.440). **Dynamic batching** sets a maximum time window per batch (e.g. size 4, window 100ms), processing when the batch fills or the window elapses, whichever comes first; this bounds latency but can leave batches partially full, wasting compute (AIE p.441). **Continuous batching** (also called in-flight batching) returns each completed response to its user immediately rather than waiting for the whole batch, and slots a new request into a completed request's place, maximizing occupancy; it was introduced by the Orca paper (Yu et al., 2022) (AIE p.441).

## Key figures
None.

## Examples
- Static batching -- waits for the batch to fill before departing, like a bus (AIE p.440)
- Dynamic batching -- fixed time window or full batch, whichever first (AIE p.441)
- Continuous batching -- completed responses returned immediately, new requests fill vacated slots (AIE p.441)

## Related
- [[prefill-and-decode]]  (boundary: batching optimizes across requests at the service level, while prefill/decode decoupling addresses resource contention within request processing)
- [[inference-latency]]  (see-also: batching trades throughput gains against added per-request latency)
- [[throughput-and-goodput]]  (see-also: batching is a primary lever for improving service throughput)
- [[inference-optimization]]  (see-also: mentioned in this page's text)

## Provenance
- [[sources/ch09-inference-service-optimization]]

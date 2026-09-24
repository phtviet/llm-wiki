---
type: concept
sources: [ch06-tools]
---
# Write Actions

Write actions are tool actions that make changes to a data source, as distinct from read-only actions that merely read from it. A SQL executor can retrieve a data table (read) but also change or delete it (write); an email API can read an email but also respond to it; a banking API can retrieve a balance but also initiate a transfer (AIE p.279-280).

Write actions let an agent do more -- for example, automating a whole customer-outreach workflow: researching potential customers, finding contacts, drafting and sending emails, reading responses, following up, extracting orders, and updating databases. But giving AI the ability to automatically alter real systems is risky: just as one wouldn't give an intern authority to delete a production database, an unreliable AI should not be allowed to initiate bank transfers. Trust in a system's capabilities and security measures is crucial, and organizations must guard against bad actors manipulating the system into harmful actions. An AI system can cause harm without any physical-world presence, e.g. by manipulating markets, stealing copyrights, violating privacy, reinforcing biases, or spreading misinformation (AIE p.280).

## Key figures
None.

## Examples
- None.

## Related
- [[tool-inventory]]  (part-of: write actions are one of the two action types alongside read-only actions)
- [[safety]]  (boundary: write actions raise safety and trust concerns beyond those of read-only tools)
- [[prompt-attacks]]  (see-also: manipulation of an agent with write access is a heightened prompt-attack risk)

## Provenance
- [[sources/ch06-tools]]

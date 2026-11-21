# 03 · Several colleagues cannot send email

**Fictional incident · Two offices · High urgency because dispatch confirmations are delayed.** Three colleagues report delayed outbound mail within ten minutes.

| Check | Simulated result |
| --- | --- |
| Scope | People in two offices report the same symptom. |
| Client comparison | Affected users reproduce it in Outlook on the web as well as desktop Outlook. |
| Service health | A fictional Exchange Online advisory describes outbound delays for the same time and tenant scope. |

**L1 decision.** Link the reports to a parent incident. Multiple clients and sites narrow the scope. The matching advisory supports tracking a provider incident. If that advisory disappears from the evidence, escalate a suspected outage to L2 and leave the cause open.

**Owner and update.** The incident coordinator tracks the advisory. L1 updates affected employees on the parent ticket. “We’ve linked your report to a mail delay affecting both offices. Please avoid resending the same confirmation. Our next update is at 10:30, even if delivery is still delayed.”

**Closure check.** After reported recovery, ask an affected employee in each office to send a uniquely identified test message and confirm delivery with the recipient. Record outstanding queued messages separately before closing. All reports, times and outcomes in this exercise are fictional. [Input record](outage.json) · [Reference procedures](../docs/references.md)

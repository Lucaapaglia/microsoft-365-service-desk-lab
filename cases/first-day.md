# 01 · “I can sign in. Why won't my mailbox open?”

**Fictional service request · One new starter · Needed before the 10:00 induction.** The approved onboarding request includes a mailbox. At 09:05 Robin opens the Microsoft 365 portal on a managed laptop, but Outlook on the web says the account has no mailbox.

| Question | Simulated observation | What it changes |
| --- | --- | --- |
| Can Robin authenticate? | The portal opens under the intended work account in a fresh session. | A password reset would address a different symptom. Portal success alone cannot prove Outlook access. |
| Is the service available to a peer? | A teammate in the same office opens their own mailbox in the web client. | A site-wide failure looks less likely. One peer cannot rule out a partial outage. |
| Is there a matching service incident? | The fictional health record contains no advisory for this symptom and time. | Keep the individual request open. An empty health feed cannot rule out a new incident. |
| Is the requested service enabled? | The fictional licensing record has an assigned product but its Exchange Online service plan is disabled for Robin. | Route the approved request to licensing. Product assignment alone does not establish mailbox entitlement. |

**L1 decision.** Send the onboarding approval, plan status and affected app to the licensing owner. Ask them to confirm the correct entitlement and provisioning state. L1 owns the employee update and retest. No license changes occur in the demo.

**Employee update.** “Your work sign-in is working. I found a difference in how email is enabled for your account and have sent it to our licensing team. I’ll update you before your induction, even if we’re still waiting.”

**Closure check.** Keep the simulated ticket open. After the owner confirms entitlement and provisioning, ask Robin to open Outlook on the web, send a test message and confirm receipt of a reply. Record the result. Escalate persistent errors with the time and exact message.

**Change one clue.** Set `plan_enabled=yes` and leave the other three checks alone. Another license change now lacks evidence. The next useful check is the app-specific error and provisioning state. [Input record](first-day.json) · [Live reference procedures](../docs/references.md)

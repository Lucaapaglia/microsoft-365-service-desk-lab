# 02 · A managed laptop loses access to a work app

**Fictional incident · One employee · Time-sensitive before an afternoon site visit.** Sam can reach the sign-in page, but the work app refuses the enrolled Windows laptop.

| Evidence from the same attempt | Interpretation |
| --- | --- |
| Inventory and the sign-in event both identify LAB-W11-07. | The device being investigated is the one in use. |
| The fictional policy result names the requirement for a compliant device. | The block has a recorded device-related reason. |
| The latest Company Portal check lists the device as noncompliant and flags the encryption requirement. | This is evidence to give the endpoint team. The report alone cannot establish whether the disk is unencrypted or reporting is stale. |

**L1 action and owner.** Escalate to endpoint support with the device reference, check-in time, reported requirement and matching sign-in event. Keep the access control in place. Ask the owner to distinguish a stale report from a local configuration problem.

**Employee update.** “Your laptop is registered, but its latest check is preventing access. I’ve sent the device details to endpoint support. I’ll check back before your visit.”

**Closure check.** Endpoint support confirms the required device state, Company Portal reports access, and Sam opens the original app from this laptop. A successful sync alone leaves the case open. If Portal shows compliant while the event still reports a block, compare device identity and timestamps. [Input record](device.json) · [Reference procedures](../docs/references.md)

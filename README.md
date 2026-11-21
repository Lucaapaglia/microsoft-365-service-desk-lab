# Microsoft 365 service desk lab

**A new starter can sign in, but their mailbox won’t open. What should the service desk do next?** A teammate can open Outlook, the fictional health feed has no matching advisory, and the starter’s Exchange Online plan is disabled. Send the approved request to licensing and keep ownership of the employee’s retest. [Read the first-day ticket](cases/first-day.md)

## Run the first ticket

From the repository root with Python 3.8 or newer installed:

```sh
python3 triage.py first-day
```

On Windows with the Python launcher:

```powershell
py -3 triage.py first-day
```

The program prints each observation, the decision and the next check. It reads bundled fictional records and runs offline without packages or administrator access. [Actual example output](examples/first-day.txt)

## Try a different decision

```sh
python3 triage.py first-day --set plan_enabled=yes
```

Now the app entitlement appears enabled. The next handoff asks the app owner to investigate provisioning and the application error. Use `plan_enabled=unknown` to withhold the observation or `plan_enabled=conflict` when two records disagree. Overrides last for one run. On Windows, replace `python3` with `py -3`.

| Shift ticket | Decision to inspect | Demo argument |
| --- | --- | --- |
| [New starter lacks mail](cases/first-day.md) | Sign-in, entitlement or service incident? | `first-day` |
| [Enrolled laptop blocked](cases/device.md) | What belongs with the endpoint team? | `device` |
| [Mail delayed in two offices](cases/outage.md) | When can several reports share an incident? | `outage` |
| [Teams microphone silent](cases/audio.md) | Does audio reach the person on the call? | `audio` |

[Employee guide in English](docs/microphone-en.md) · [Dansk vejledning](docs/microphone-da.md) · [Copenhagen role research](docs/role-evidence.md) · [Microsoft reference procedures](docs/references.md)

## Verification and scope

Run `python3 -m unittest discover -s tests -v` (Windows: `py -3 -m unittest discover -s tests -v`). The suite exercises the CLI, altered evidence, uncertain results, sample output and local documentation links. The simulator recommends a next step. All employee conversations, observations and prospective closure checks are fictional. No live tenant administration was performed.

For on-premises Active Directory, PowerShell and Windows troubleshooting, see the [Windows Enterprise Helpdesk Lab](https://github.com/Lucaapaglia/windows-enterprise-helpdesk-lab).

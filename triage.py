"""Offline first-line support exercise. All inputs are synthetic observations."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CASES = ("first-day", "device", "outage", "audio")
SIGNALS = {
    "first-day": ("portal_signin", "peer_can_open", "matching_advisory", "plan_enabled"),
    "device": ("enrolled", "policy_block", "device_compliant"),
    "outage": ("multiple_users", "web_also_fails", "matching_advisory"),
    "audio": ("os_meter_moves", "teams_uses_tested_mic", "other_party_hears"),
}


def decide(case, signals):
    """Each signal refers to the same service, device or attempt as the case."""
    required = SIGNALS[case]
    if set(signals) - set(required):
        raise ValueError("Unrecognized signal for " + case)
    for key in required:
        if signals.get(key, "unknown") not in ("yes", "no", "unknown", "conflict"):
            raise ValueError("Invalid observation for " + key)
    values = [signals.get(key, "unknown") for key in required]
    if "conflict" in values:
        key = required[values.index("conflict")]
        return "Reconcile evidence", f"Two sources disagree on {key}. Match the user, device and timestamp, then repeat that check."
    if case == "first-day":
        signin, peer, advisory, plan = values
        if signin == "no":
            return "Investigate sign-in", "Capture the failed attempt time and error before checking application access."
        if advisory == "yes" and plan == "no":
            return "Track two possible blockers", "Link the matching advisory and ask licensing to verify the missing entitlement independently."
        if advisory == "yes":
            return "Track service incident", "Link the advisory and confirm that its scope and next update cover this employee."
        if values == ["yes", "yes", "no", "no"]:
            return "Route to licensing", "Send the approved request and disabled app-plan evidence to the licensing owner. Keep the ticket open for an employee retest."
        if values == ["yes", "yes", "no", "yes"]:
            return "Investigate app access", "Capture the app-specific error and time. Ask the app owner to check provisioning and access policy."
        if peer == "no":
            return "Check wider impact", "Compare affected accounts and service health before treating this as one user's issue."
    elif case == "device":
        enrolled, block, compliant = values
        if enrolled == "yes" and block == "yes" and compliant == "no":
            return "Escalate to endpoint support", "Send the device reference, failed requirement and policy result. Ask the endpoint owner to review remediation."
        if block == "yes" and compliant == "yes":
            return "Reconcile device status", "Compare the device ID and check-in time with the sign-in event before changing anything."
        if enrolled == "no":
            return "Check enrollment", "Verify the expected managed device and route enrollment to the endpoint owner."
    elif case == "outage":
        multiple, web, advisory = values
        if multiple == web == advisory == "yes":
            return "Track service incident", "Link affected tickets to the advisory. Assign a communications owner and set the next update time."
        if multiple == web == "yes" and advisory == "no":
            return "Escalate suspected outage", "Give L2 the affected locations, times and client comparisons. Keep the cause unconfirmed."
        if web == "no" and multiple == "yes":
            return "Compare desktop clients", "Use the working web client as a temporary option and compare desktop versions and sites."
    else:
        meter, selected, heard = values
        if heard == "yes":
            return "Verify recovery", "Repeat the call with the intended dock and microphone. Ask the employee to confirm before closing."
        if meter == "yes" and selected == "no" and heard == "no":
            return "Select the tested microphone", "Choose the working microphone in Teams and ask the other participant to confirm clear audio."
        if meter == "no" and heard == "no":
            return "Check the local audio path", "Check hardware mute and the Windows input selection, then repeat the input-meter test."
    missing = [key for key, value in zip(required, values) if value == "unknown"]
    if missing:
        return "Collect evidence", "Check " + ", ".join(missing) + " and record the result before assigning a cause."
    return "Continue investigation", "Reproduce the symptom with the employee and hand L2 the observations if it persists."


def report(case, signals):
    decision, action = decide(case, signals)
    lines = [f"SIMULATED TICKET | {case}", "Observations"]
    lines.extend(f"  {key}: {signals.get(key, 'unknown')}" for key in SIGNALS[case])
    return "\n".join(lines + [f"Decision: {decision}", f"Next check: {action}"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", choices=CASES, nargs="?", default="first-day")
    parser.add_argument("--set", metavar="SIGNAL=VALUE", action="append", default=[],
                        help="Override a synthetic observation: yes, no, unknown or conflict")
    args = parser.parse_args()
    try:
        signals = json.loads((ROOT / "cases" / (args.case + ".json")).read_text(encoding="utf-8"))
        for change in args.set:
            key, value = change.split("=", 1)
            signals[key] = value
        print(report(args.case, signals))
    except (ValueError, OSError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()

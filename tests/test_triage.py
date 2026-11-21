import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

import triage


def run_case(case, *changes):
    return subprocess.run([sys.executable, str(triage.ROOT / "triage.py"), case, *changes],
                          capture_output=True, text=True, check=False)


class ShiftTests(unittest.TestCase):
    def test_four_tickets(self):
        for case, decision in zip(triage.CASES, ("Route to licensing", "Escalate to endpoint support",
                                                  "Track service incident", "Select the tested microphone")):
            with self.subTest(case=case):
                result = run_case(case)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("Decision: " + decision, result.stdout)
                self.assertIn("Next check:", result.stdout)

    def test_signal_changes_handoff(self):
        self.assertIn("Decision: Investigate app access", run_case("first-day", "--set", "plan_enabled=yes").stdout)

    def test_missing_field(self):
        decision, action = triage.decide("first-day", {"portal_signin": "yes"})
        self.assertEqual(decision, "Collect evidence")
        self.assertIn("plan_enabled", action)

    def test_disagreement(self):
        self.assertIn("Reconcile evidence", run_case("first-day", "--set", "plan_enabled=conflict").stdout)

    def test_two_independent_blockers(self):
        self.assertIn("Track two possible blockers", run_case("first-day", "--set", "matching_advisory=yes").stdout)

    def test_device_status_disagrees_with_policy(self):
        self.assertIn("Reconcile device status", run_case("device", "--set", "device_compliant=yes").stdout)

    def test_unconfirmed_outage(self):
        self.assertIn("Escalate suspected outage", run_case("outage", "--set", "matching_advisory=no").stdout)

    def test_local_audio_fault(self):
        self.assertIn("Check the local audio path", run_case("audio", "--set", "os_meter_moves=no").stdout)

    def test_invalid_observations(self):
        for override in ("plan_enabled=maybe", "unknown_key=no", "missing_equals"):
            with self.subTest(override=override):
                self.assertEqual(run_case("first-day", "--set", override).returncode, 2)

    def test_sample_matches_cli(self):
        sample = (triage.ROOT / "examples/first-day.txt").read_text(encoding="utf-8")
        self.assertEqual(run_case("first-day").stdout, sample)

    def test_local_links(self):
        for doc in triage.ROOT.rglob("*.md"):
            for link in re.findall(r"\]\(([^)]+)\)", doc.read_text(encoding="utf-8")):
                if not link.startswith(("https://", "#")):
                    self.assertTrue((doc.parent / link).is_file(), (doc.name, link))

    def test_all_fixture_signals_documented_in_output(self):
        for case in triage.CASES:
            fixture = json.loads((triage.ROOT / "cases" / (case + ".json")).read_text())
            self.assertEqual(set(fixture), set(triage.SIGNALS[case]))
            output = run_case(case).stdout
            for key, value in fixture.items():
                self.assertIn(f"{key}: {value}", output)

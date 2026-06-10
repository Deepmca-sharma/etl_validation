# run_tests.py
# ─────────────────────────────────────────────────────
# PURPOSE: This is YOUR control panel for all test suites.
# Jenkins will call this file automatically after every git push.
# You can also run it manually from terminal anytime.
# ─────────────────────────────────────────────────────

import subprocess  # lets Python run terminal commands (like pytest)
import sys         # lets Python read arguments passed to this script
                   # and also lets Python tell Jenkins pass/fail

# ── SUITE DEFINITIONS ──────────────────────────────
# Think of this as a menu of what tests to run.
# Key   = short name Jenkins/you will type
# Value = actual pytest command that runs those tests

SUITES = {
    "sanity":     "pytest tests/ -v -m sanity",
    "regression": "pytest tests/ -v -m regression",
    "unit":       "pytest tests/ -v",
    "bvt":        "pytest tests/ -v -m bvt --junitxml=reports/results.xml",
    "all":        "pytest tests/ -v --junitxml=reports/results.xml",
}

# What each suite runs against YOUR folder structure:
#   sanity     → runs only tests marked @pytest.mark.sanity
#   regression → runs only tests marked @pytest.mark.regression
#   unit       → runs ALL tests in your tests/ folder
#                (test_schema, test_rowcount, test_nulls,
#                 test_duplicates, test_business_rules)
#   bvt        → build verification — marked @pytest.mark.bvt
#   all        → everything, saves XML report to reports/


# ── FUNCTION: actually runs the command ────────────
def run_suite(command):
    print(f"\n>>> Running: {command}\n")

    # subprocess.run() executes the pytest command in terminal
    # shell=True means it runs exactly like you typed it in PowerShell
    result = subprocess.run(command, shell=True)

    # returncode 0 = all tests passed
    # returncode 1 = one or more tests failed
    if result.returncode == 0:
        print("\n✅ All tests passed!")
    else:
        print("\n❌ Some tests failed. Check output above.")
        sys.exit(1)
        # sys.exit(1) is IMPORTANT for Jenkins —
        # it tells Jenkins "this build failed" → shows red


# ── MAIN LOGIC ─────────────────────────────────────

# sys.argv is the list of arguments passed when running this script
# Example: "python run_tests.py sanity"
#           sys.argv[0] = "run_tests.py"  (always the script name)
#           sys.argv[1] = "sanity"        (what we care about)

if len(sys.argv) > 1:
    # ── Called by Jenkins (or from terminal with argument) ──
    # Example: python run_tests.py all
    suite_name = sys.argv[1].lower()

    if suite_name in SUITES:
        run_suite(SUITES[suite_name])
    else:
        print(f"Unknown suite: '{suite_name}'")
        print(f"Available: {list(SUITES.keys())}")
        sys.exit(1)

else:
    # ── Called manually without argument → show menu ──
    # Example: just typing "python run_tests.py" in terminal
    print("\n========== Test Suite Runner ==========")
    print("1. sanity      → quick smoke check")
    print("2. regression  → full validation suite")
    print("3. unit        → all unit tests")
    print("4. bvt         → build verification tests")
    print("5. all         → run everything + save report")
    print("=======================================")

    choice = input("\nEnter suite name (sanity/regression/unit/bvt/all): ").strip().lower()

    if choice in SUITES:
        run_suite(SUITES[choice])
    else:
        print(f"Invalid choice: '{choice}'")
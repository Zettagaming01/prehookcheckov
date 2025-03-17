import os
import sys
from checkov.common.runners.runner_registry import RunnerRegistry
from checkov.runner_filter import RunnerFilter
from checkov.terraform.runner import Runner

# Initialize the runner
runner_registry = RunnerRegistry(
    banner="Custom Check Runner",
    runner_filter=RunnerFilter(framework=['terraform'], checks=['CKV_AZURE_STORAGE_1'])
)

# Add the custom rules directory to Python path
custom_rules_dir = os.path.join(os.getcwd(), 'custom_rules')
sys.path.append(custom_rules_dir)

# Run the check
report = runner_registry.run()

# Print results
if report:
    for record in report.failed_checks:
        print(f"\nFAILED CHECK: {record.check_id}")
        print(f"Resource: {record.resource}")
        print(f"File: {record.file_path}")
        print(f"Line: {record.file_line_range}")
        print(f"Guideline: {record.guideline}")

    for record in report.passed_checks:
        print(f"\nPASSED CHECK: {record.check_id}")
        print(f"Resource: {record.resource}")
        print(f"File: {record.file_path}")
        print(f"Line: {record.file_line_range}")

    print(f"\nTotal failed checks: {len(report.failed_checks)}")
    print(f"Total passed checks: {len(report.passed_checks)}")
else:
    print("No results found")

# Terraform Custom Security Checks

This repository includes custom security checks for Terraform using Checkov, integrated with pre-commit hooks.

## Prerequisites

1. Python 3.9 or higher
2. pre-commit
3. Checkov

## Setup

1. Install pre-commit:
```bash
pip install pre-commit
```

2. Install the pre-commit hooks:
```bash
pre-commit install
```

3. The pre-commit hook will automatically run Checkov with custom rules on every commit.

## Custom Rules

Custom security rules are located in the `custom_rules` directory. These rules will be automatically executed as part of:
- Pre-commit hooks
- Azure DevOps pipeline
- Manual Checkov runs

## Manual Execution

To run Checkov with custom rules manually:

```bash
checkov -d . --external-checks-dir custom_rules --framework terraform
```

## Pipeline Integration

The custom rules are integrated into the Azure DevOps pipeline and will run automatically during:
- Validation stage
- Plan stage
- Pre-commit checks

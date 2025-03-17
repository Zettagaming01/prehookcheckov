# Terraform Custom Security Checks

This repository includes custom security checks for Terraform using Checkov, integrated with pre-commit hooks. The checks focus on Azure Storage Account security best practices.

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

### Pre-commit Configuration

The pre-commit hook is configured to:
- Run custom security checks (CKV_AZURE_STORAGE_1 and CKV_AZURE_STORAGE_2)
- Skip the CKV_TF-1 check to avoid unnecessary validation
- Check for trailing whitespace and file formatting
- Validate YAML files
- Check for large file additions

## Custom Rules

Custom security rules are located in the `custom_rules` directory. Currently implemented rules:

1. **CKV_AZURE_STORAGE_1**: Ensures Azure Storage Accounts use Geo-Redundant Storage (GRS)
   - Validates that storage accounts are not using Locally Redundant Storage (LRS)
   - Requires `account_replication_type` to be set to a GRS option

2. **CKV_AZURE_STORAGE_2**: Ensures Storage Account has private endpoint enabled
   - Validates network rules configuration
   - Checks for `default_action = "Deny"` in network rules
   - Verifies private endpoint or private endpoint connection configuration

### Example of a compliant configuration:

```hcl
resource "azurerm_storage_account" "example" {
  name                     = "examplestorage"
  resource_group_name      = "example-rg"
  location                 = "West Europe"
  account_tier             = "Standard"
  account_replication_type = "GRS"  # Compliant with CKV_AZURE_STORAGE_1

  network_rules {
    default_action = "Deny"  # Compliant with CKV_AZURE_STORAGE_2
  }

  private_endpoint_connection {
    # Private endpoint configuration
  }
}
```

## Manual Execution

To run Checkov with custom rules manually:

```bash
# Run all custom rules
checkov -d . --external-checks-dir custom_rules --framework terraform

# Run specific custom rule
checkov -d . --external-checks-dir custom_rules --framework terraform --check CKV_AZURE_STORAGE_1

# Run with same configuration as pre-commit hook
checkov -d . --external-checks-dir custom_rules --framework terraform --check CKV_AZURE_STORAGE_1 --check CKV_AZURE_STORAGE_2 --skip-check CKV_TF-1
```

## Pipeline Integration

The custom rules are integrated into the Azure DevOps pipeline and will run automatically during:
- Validation stage
- Plan stage
- Pre-commit checks

The pipeline is configured to fail if any of the custom security checks fail, ensuring compliance with security standards before deployment.

## Contributing

To add new custom rules:
1. Create a new Python file in the `custom_rules` directory
2. Implement the rule following the Checkov BaseResourceCheck pattern
3. Register the rule in `custom_rules/__init__.py`
4. Update the pre-commit configuration to include the new rule
5. Update this README with details about the new rule

# prehookcheckov
Pre-hook using custom python rule checkov rules

## Description
This project implements custom Checkov rules for pre-commit hooks to enforce security and compliance standards in your Terraform configurations. It provides automated checks to ensure your infrastructure code follows best practices and security guidelines.

## Features
- Custom Checkov rules for Azure resources
- Pre-commit hook integration
- Automated compliance checks
- CI/CD pipeline integration with Azure DevOps

## Custom Rules
The project includes the following custom Checkov rules:
- `storage_private_endpoint_check.py`: Ensures Azure Storage accounts are configured with private endpoints
- `storage_account_check.py`: Validates Azure Storage account configurations for security best practices

## Prerequisites
- Python 3.x
- Checkov
- Git
- Azure CLI (optional)

## Installation
1. Clone the repository:
```bash
git clone <repository-url>
cd prehookcheckov
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install pre-commit hooks:
```bash
pre-commit install
```

## Usage
1. Run Checkov with custom rules:
```bash
checkov -d . --check CKV_CUSTOM_*
```

2. The pre-commit hook will automatically run when you commit changes:
```bash
git add .
git commit -m "Your commit message"
```

## Configuration
The project uses the following configuration files:
- `.pre-commit-config.yaml`: Pre-commit hook configuration
- `azure-pipelines.yml`: CI/CD pipeline configuration
- `requirements.txt`: Python dependencies

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
[Add your license information here]
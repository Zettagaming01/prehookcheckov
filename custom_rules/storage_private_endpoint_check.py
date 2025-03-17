from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class StoragePrivateEndpointCheck(BaseResourceCheck):
    def __init__(self):
        name = "Ensure Storage Account has private endpoint enabled"
        id = "CKV_AZURE_STORAGE_2"
        supported_resources = ['azurerm_storage_account']
        categories = [CheckCategories.NETWORKING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        # Check if network_rules block exists
        if 'network_rules' in conf.keys():
            network_rules = conf['network_rules'][0]
            # Check if default_action is "Deny" which is required for private endpoints
            if isinstance(network_rules, dict) and network_rules.get('default_action', ['Allow'])[0] == 'Deny':
                # Look for associated private endpoint in the same configuration
                if self.check_private_endpoint_exists(conf):
                    return CheckResult.PASSED
        return CheckResult.FAILED

    def check_private_endpoint_exists(self, conf):
        # This is a simplified check. In a real scenario, you'd want to verify:
        # 1. Private endpoint is properly configured
        # 2. Private endpoint is connected to the storage account
        # 3. Private DNS zone is configured
        if 'private_endpoint' in conf.keys() or 'private_endpoint_connection' in conf.keys():
            return True
        return False

check = StoragePrivateEndpointCheck()

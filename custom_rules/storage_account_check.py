from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class StorageAccountCheck(BaseResourceCheck):
    def __init__(self):
        name = "Ensure that Storage Account uses GRS replication"
        id = "CKV_AZURE_STORAGE_1"
        supported_resources = ['azurerm_storage_account']
        categories = [CheckCategories.BACKUP_AND_RECOVERY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if 'account_replication_type' in conf.keys():
            replication_type = conf['account_replication_type'][0]
            if replication_type in ['GRS', 'RAGRS']:
                return CheckResult.PASSED
            return CheckResult.FAILED
        return CheckResult.FAILED

    def get_evaluated_keys(self):
        return ['account_replication_type']

check = StorageAccountCheck()

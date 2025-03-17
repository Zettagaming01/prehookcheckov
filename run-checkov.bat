@echo off
checkov -d . --external-checks-dir custom_rules --framework terraform --check CKV_AZURE_STORAGE_1 > checkov_results.txt
type checkov_results.txt

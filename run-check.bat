@echo off
checkov -d . --external-checks-dir custom_rules --framework terraform --check CKV_AZURE_STORAGE_1 -o cli --soft-fail > check-results.txt
type check-results.txt

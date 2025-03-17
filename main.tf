resource "azurerm_storage_account" "example" {
  name                     = "examplestorage"
  resource_group_name      = "example-rg"
  location                 = "West Europe"
  account_tier             = "Standard"
  account_replication_type = "GRS"

  network_rules {
    default_action = "Deny"
    ip_rules       = ["100.0.0.1"]
  }

  private_endpoint_connection {
    name                           = "example-endpoint"
    is_manual_connection          = false
    private_service_connection {
      name                       = "example-privateserviceconnection"
      is_manual_connection      = false
      private_connection_resource_id = azurerm_storage_account.example.id
      subresource_names          = ["blob"]
    }
  }
}

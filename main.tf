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
      private_connection_resource_id = azurerm_private_endpoint.example.id
      subresource_names          = ["blob"]
    }
  }
}

# Private endpoint resource
resource "azurerm_private_endpoint" "example" {
  name                = "example-endpoint"
  location            = "West Europe"
  resource_group_name = "example-rg"
  subnet_id           = azurerm_subnet.example.id

  private_service_connection {
    name                           = "example-privateserviceconnection"
    private_connection_resource_id = azurerm_storage_account.example.id
    is_manual_connection          = false
    subresource_names             = ["blob"]
  }
}

# Required networking resources
resource "azurerm_virtual_network" "example" {
  name                = "example-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = "West Europe"
  resource_group_name = "example-rg"
}

resource "azurerm_subnet" "example" {
  name                 = "example-subnet"
  resource_group_name  = "example-rg"
  virtual_network_name = azurerm_virtual_network.example.name
  address_prefixes     = ["10.0.1.0/24"]

  private_endpoint_network_policies_enabled = true
}

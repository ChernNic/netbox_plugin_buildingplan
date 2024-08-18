from netbox.plugins import PluginConfig

class BuildingPlanConfig(PluginConfig):
    name = 'netbox_plugin_buildingplan'
    verbose_name = 'Building Plan'
    description = 'A plugin to add building plans to tenants in NetBox'
    version = '1.0.0'
    base_url = 'buildingplan'
    required_settings = []
    min_version = '3.0.0'

config = BuildingPlanConfig

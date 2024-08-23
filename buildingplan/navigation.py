from netbox.plugins import PluginMenu, PluginMenuItem

# Определение пункта меню для списка планов зданий
menuitem1 = PluginMenuItem(
    link="plugins:netbox_plugin_buildingplan:building_plan_list",
    link_text="Building Plans",
)

# Определение меню для плагина
menu = PluginMenu(
    label="Building Plans",
    groups=(
        ("Pages", [menuitem1]),
    ),
    icon_class="mdi mdi-human-greeting-variant",
)

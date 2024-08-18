from netbox.plugins import PluginTemplateExtension

class CustomTextExtension(PluginTemplateExtension):
    model = 'dcim.device'  # Replace with the model where you want the text to appear.

    def right_page(self):
        return self.render('netbox_plugin_buildingplan/custom_text.html')

template_extensions = [CustomTextExtension]

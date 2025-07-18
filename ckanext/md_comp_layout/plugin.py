import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.md_comp_layout import views


class MdCompLayoutPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    # plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IBlueprint)


    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
            'md_comp_layout')

    # IBlueprint
    def get_blueprint(self):
        return views.get_blueprints()
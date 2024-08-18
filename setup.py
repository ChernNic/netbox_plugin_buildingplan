from setuptools import find_packages, setup

setup(
    name='netbox_plugin_buildingplan',
    version='1.0.0',
    description='A NetBox plugin to add building plans to tenants.',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)

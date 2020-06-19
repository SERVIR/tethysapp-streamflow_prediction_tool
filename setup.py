from setuptools import setup, find_namespace_packages
from tethys_apps.app_installation import find_resource_files
import os
import sys
### Apps Definition ###
app_package = 'streamflow_prediction_tool'

release_package = 'tethysapp-' + app_package
resource_files = find_resource_files('tethysapp/' + app_package + '/templates', 'tethysapp/' + app_package)
resource_files += find_resource_files('tethysapp/' + app_package + '/public', 'tethysapp/' + app_package)
# App Packages
dependencies = []

setup(
    name=release_package,
    version='1.1.0',
    tags='Timeseries,Stream Flow,water',
    description=('Provides 15-day streamflow predicted estimates by using '
                 'ECMWF (ecmwf.int) runoff predictions routed with the RAPID '
                 '(rapid-hub.org) program. Return period estimates '
                 'and warning flags aid in determining the severity.'),
    long_description='',
    keywords='ECMWF, RAPID, Streamflow Prediction, Forecast',
    author='Alan D. Snow',
    author_email='alan.d.snow@usace.army.mil',
    url='https://github.com/erdc-cm/tethysapp-streamflow_prediction_tool',
    license='BSD 3-Clause',
    packages=find_namespace_packages(),
    package_data={'': resource_files},
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,

)

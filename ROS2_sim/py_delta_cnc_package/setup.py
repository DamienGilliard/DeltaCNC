from setuptools import find_packages, setup

package_name = 'py_delta_cnc_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='damien',
    maintainer_email='damien.gilliard@epfl.ch',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dummy_gcode_executer = py_delta_cnc_package.dummy_gcode_executer:main',
            'gcode_reader = py_delta_cnc_package.gcode_reader:main',
        ],
    },
)

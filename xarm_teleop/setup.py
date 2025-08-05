from setuptools import find_packages, setup

package_name = 'xarm_teleop'

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
    maintainer='Anirudh Krishnan Komaralingam',
    maintainer_email='anirudh.krishnankomaralingam@nist.gov',
    description='xarm6 teleop',
    license='Dont touch',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = xarm_teleop.publisher_member_function:main',
        ],
    },
)

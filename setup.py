from setuptools import setup, find_packages

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='sawyer_kinematics',
      version='0.0.1',
      description='Library for Rethink Robotics Sawyer kinematics',
      url='https://github.com/Heracleia/sawyer_kinematics',
      author='Michail Theofanidis, Joe Cloud',
      author_email='git@joe.cloud',
      license=license,
      packages=find_packages(exclude=('examples')),
      install_requires=required
)

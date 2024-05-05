from setuptools import setup, find_packages # type: ignore

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/samukelisiwenkosi/<package-name>',
    author='samukelisiwe',
    author_email='samukelisiwenkosi27@gmail.com'
)
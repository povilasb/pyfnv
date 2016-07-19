from setuptools import setup

setup(
    name='fnv',
    version='0.2.0',
    description='FNV hash functions.',
    long_description=open('README.rst').read(),
    url='https://github.com/povilasb/pyfnv',
    author='Povilas Balciunas',
    author_email='balciunas90@gmail.com',
    license='MIT',
    packages=['fnv'],
    install_requires=['typing==3.5.2.2'],
    zip_safe=False
)

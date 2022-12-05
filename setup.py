from setuptools import setup, find_packages
 
__version__ = '0.10' # version

setup(name = 'ngc', 
    version = __version__,
    url='https://github.com/ngc5139/pyngc',
    author='NGC5139',
    description='Python New General Common Tool',
    author_email='cencrx@outlook.com',
    packages=find_packages(exclude=["tests"]),
    install_requires=['requests'],
    include_package_data=True,
    python_requires='>=3.11'
)

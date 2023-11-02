import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='toolbox',
    version='0.0.1',
    author='Nicholas Daskalovic',
    author_email='daskalovic.n@gmail.com',
    description='Toolbox for finance platform',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ndaskalovic/finance-toolbox',
    project_urls = {
        "Bug Tracker": "https://github.com/ndaskalovic/finance-toolbox/issues"
    },
    license='MIT',
    packages=['toolbox'],
    install_requires=['requests', 'pandas', 'fredapi'],
)
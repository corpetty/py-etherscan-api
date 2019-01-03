import setuptools

setuptools.setup(
    name='py_etherscan_api',
    version='0.8.0',
    packages=['examples', 'examples.stats', 'examples.tokens',
              'examples.accounts', 'etherscan'],
    url='https://github.com/corpetty/py-etherscan-api',
    license='MIT',
    author='coreypetty',
    author_email='petty.btc@gmail.com',
    description='Python Bindings to Etherscan.io API',
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)

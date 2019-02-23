import setuptools

setuptools.setup(
    name='py_etherscan_api',
    version='0.8.0',
    packages=['examples', 'examples.stats', 'examples.tokens',
              'examples.accounts', 'examples.blocks', 'examples.transactions',  'etherscan'],
    url='https://github.com/corpetty/py-etherscan-api',
    license='MIT',
    author='coreypetty',
    author_email='petty.btc@gmail.com',
    description='Python Bindings to Etherscan.io API',
    install_requires=[
        'requests>=2.20.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)

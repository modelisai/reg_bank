from setuptools import setup, find_packages

setup(
    name='reg_bank',
    version='0.1',
    packages=find_packages(),
    description='AI-powered regulatory analysis and knowledge base for AI and GenAI regulations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Shashvat Sinha / modelis AI',
    author_email='ssinha@modelis.ai',
    url='https://github.com/modelisai/reg_bank',
    install_requires=[
        # List your project dependencies here
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

from setuptools import setup, find_packages

setup(
    name='ModelMyFinance',  # Replace with your package name
    version='1.0.0',  # Replace with your package version
    packages=find_packages(),
    install_requires=[
      
    ],
    entry_points={
        'console_scripts': [
            'ModelMyFinance = ModelMyFinance.opm:binomial_option_pricing',  # Replace 'your_script_name' with the actual name of your script
        ],
    },
    author='Gopalakrishnanamsha',
    author_email='gopalakrishnana02@gmail.com',
    description='Python Package for Financial Models',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gopalakrishnanarjun1194/ModelMyFinance',  # Update with your GitHub repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
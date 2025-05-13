from setuptools import setup, find_packages

setup(
    name='modelmyfinance',  # Replace with your package name
    version='1.0.6',  # Replace with your package version
    packages=find_packages(),
    install_requires=[
      
    ],
    entry_points={
        'console_scripts': [
            'modelmyfinancee = modelmyfinancee.opm:binomial_option_pricing',  # Replace 'your_script_name' with the actual name of your script
        ],
    },
    author='Gopalakrishnan Arjunan',
    author_email='gopalakrishnana02@gmail.com',
    description='Python Package for Financial Models',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gopalakrishnanarjun1194/modelmyfinancee',  # Update with your GitHub repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
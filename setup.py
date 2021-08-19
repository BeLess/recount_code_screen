from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name='recount-scraper',
    version='0.0.1',
    author='Benjamin Less',
    author_email='benaless12@gmail.com',
    license='FOSS',
    description='A tool used for scraping phone numbers from a given URL',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/BeLess/reount_code_screen',
    py_modules=['recount-scraper', 'app'],
    packages=find_packages(),
    install_require =[requirements],
    python_requires='>=3.9',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        cooltool=recount-scraper:main
    '''
)
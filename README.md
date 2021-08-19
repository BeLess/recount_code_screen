# Recount Code Screen
## Phone number web crawler/scraper

A simple tool designed to show case my development skills to the fine developers over at The Recount.

### Purpose
This is designed to take a URL and search the page found at this URL, as well as any children (in this case defined as "Any sublinks found within the HTML document"), for strings resembling phone numbers.

### Getting Started
This tool is built using Python 3.9 and an environment manager called [poetry](https://python-poetry.org/)

Thus poetry must be installed to create the python virtual environment. This is done as simply as:

`pip install poetry`

Once poetry is installed, you can create the virtual environment by doing the following:
* `cd {desired_location_of_project}`
* `git clone https://github.com/BeLess/reount_code_screen.git`
* `cd recount_code_screen`
* `poetry install`

All the external libraries can be found at pypi, so there should be no difficulties finding any thing

### Using the tool
You can either run this from the built an installed wheel, like so:
* `poetry build`
* `pip install ./dist/recount_code_screen-0.1.0-py3-none-any.whl`

Or by invoking the python locally:
* `.\recount_code_screen\main.py {options}`

This tool is built using [click](https://click.palletsprojects.com/en/8.0.x/) and is based around the `crawl` command. `crawl` has a subcommand called `phone-numbers`, which will crawl for phone numbers in the html. This command takes two arguments:
* `url`: The url of the web page you'd like to scrape
* `--depth`: the desired maximum depth you would like to search up to

Thus, you can run this to the given page and ALL of its children, recursively:
* `{chosen_invocation} crawl phone-numbers "https://therecount.github.io/interview-materials/project-a/1.html"`

Or this to only search the parent and its immediate children:
*`{chosen_invocation} crawl phone-numbers "https://therecount.github.io/interview-materials/project-a/1.html" --depth=2`



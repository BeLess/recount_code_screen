import click
from recount_code_screen.model.phone_crawler import PhoneNumberCrawler


@click.group()
def cli():
    pass


@cli.group()
def crawl():
    click.echo("You need to tell me what to crawl for")


@crawl.command()
@click.argument("url")
@click.option("--depth", default=None, help="Desired tree depth to crawl to. By default only scrapes the given URL")
def phone_numbers(url: str, depth: str):
    crawler = PhoneNumberCrawler(url=url, depth=int(depth) if depth else None)
    click.echo("Crawling for phone numbers...")
    for number in crawler.crawl():
        click.echo(number)


if __name__ == "__main__":
    cli()

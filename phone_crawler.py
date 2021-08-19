import re
from dataclasses import dataclass, field
from html.parser import HTMLParser
from typing import Iterable, List, Optional
from urllib.parse import urljoin
from urllib.request import urlopen

ENCODING = "utf-8"


class LinkParser(HTMLParser):
    """
    A custom HTMLParser (see HTMLParser docs) for finding the value of <a href> tags in an HTML string
    """
    def reset(self):
        HTMLParser.reset(self)
        self.extracting = False
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href":
                    self.links.append(value)


@dataclass()
class WebCrawler:
    """
    A base class for recursively crawling through a given URL to find each instance of a desired piece of information

    Implementations are responsible for parsing and formatting specific data out of the HTML page

    Args:
        url: the base (starting) URL for the domain tree
        depth: the maximum depth to search up to. None means "search every page discovered in the tree"
        crawled_urls: a list of urls previously discovered to prevent duplicate work
    """
    url: str
    depth: Optional[int] = None
    crawled_urls: List[str] = field(default_factory=list)

    def crawl(self, current_depth: int = 1,  url: Optional[str] = None) -> Iterable[str]:
        """
        Recursively crawls through the html of a given url, up to a specified depth, yielding desired information as it
        is found in each document
        :param current_depth: What level of the document tree is currently under examination
        :param url: the url of any child pages
        :return: An iterator of phone numbers found in each page
        """
        if not url:
            url = self.url
        html_str = self.get_html(url)
        yield from self.clean_data(self.scrape(html_str))
        self.crawled_urls.append(url)
        if not self.depth or current_depth < self.depth:
            next_depth = current_depth + 1
            sub_links = self.get_sublinks(html_str)
            if sub_links:
                for link in sub_links:
                    yield from self.crawl(next_depth, link)

    def get_sublinks(self, html_str) -> List[str]:
        """
        Given an HTML document in string form, find and format the value of every <a href> tag.

        if an href is an incomplete url, assumes that it relative to the original url
        :param html_str: The string representation of the HTML document
        :return: a list containing all found links in the document
        """
        sub_links = []
        parser = LinkParser()
        parser.feed(html_str)
        for link in parser.links:
            new_url = urljoin(self.url, link)
            if new_url not in self.crawled_urls:
                sub_links.append(new_url)

        return sub_links

    def get_html(self, url: str) -> str:
        """
        Gets the HTML document string for the given url
        :param url: the url under examination
        :return: a string containing the HTML document
        """
        page = urlopen(url)
        html_str = page.read().decode(ENCODING)
        return html_str

    def scrape(self, html_str: str):
        """
        An abstract method used to extract desired information from an HTML document.

        Child classes are responsible for implementing the logic to parse for the info
        :param html_str: an HTML document str
        :return:
        """
        raise NotImplementedError

    def clean_data(self, data):
        """
        An abstract method used to format the data pulled from the HTML string

        child classes are responsible for implementing the logic to format the raw data
        :param data:
        :return:
        """
        raise NotImplementedError


@dataclass()
class PhoneNumberCrawler(WebCrawler):
    def scrape(self, html_str: str) -> List[str]:
        """
        Uses a regex to search the HTML document for different formats for phone numbers
        :param html_str:
        :return:
        """
        phone_number_regex = "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
        phone_numbers = re.findall(phone_number_regex, html_str)
        return phone_numbers

    def clean_data(self, phone_numbers: List[str]):
        """
        Strips all existing punctuation for the given phone numbers, as well as any unnecessary leading 1s, and uses
        dashes (-) to separate out the different parts of a standard US phone number
        :param phone_numbers:
        :return:
        """
        cleaned_numbers = []
        for number in phone_numbers:
            phone = re.sub(r"\D", "", number)
            phone = phone.lstrip("1")
            cleaned_numbers.append(f"{phone[0:3]}-{phone[3:6]}-{phone[6:]}")

        return cleaned_numbers

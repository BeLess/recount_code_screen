from recount_code_screen.model.phone_crawler import PhoneNumberCrawler


def test_phone_formatting_dashes() -> None:
    crawler = PhoneNumberCrawler("test")
    result = crawler.clean_data(["555-555-1234"])
    assert result == ["555-555-1234"]


def test_phone_formatting_dots() -> None:
    crawler = PhoneNumberCrawler("test")
    result = crawler.clean_data(["555.555.1234"])
    assert result == ["555-555-1234"]


def test_phone_regex_no_punctuation() -> None:
    crawler = PhoneNumberCrawler("test")
    result = crawler.clean_data(["5555551234"])
    assert result == ["555-555-1234"]


def test_phone_regex_no_parens() -> None:
    crawler = PhoneNumberCrawler("test")
    result = crawler.clean_data(["(555)5551234"])
    assert result == ["555-555-1234"]

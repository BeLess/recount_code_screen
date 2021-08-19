from recount_code_screen.model.phone_crawler import PhoneNumberCrawler

TEST_URL_HOME = "https://therecount.github.io/interview-materials/project-a/1.html"
TEST_URL_2 = "https://therecount.github.io/interview-materials/project-a/2.html"
TEST_URL_3 = "https://therecount.github.io/interview-materials/project-a/3.html"


def test_crawling_single_page() -> None:
    crawler = PhoneNumberCrawler(TEST_URL_2)
    found_numbers = [number for number in crawler.crawl(1)]
    expected = ["555-555-1234", "555-555-2345"]
    assert found_numbers == expected


def test_crawling_from_top_of_tree() -> None:
    crawler = PhoneNumberCrawler(TEST_URL_HOME)
    found_numbers = [number for number in crawler.crawl(0)]
    expected = ["555-555-1234", "555-555-2345", "555-555-9876"]
    assert found_numbers == expected


def test_crawling_from_bottom_of_tree() -> None:
    crawler = PhoneNumberCrawler(TEST_URL_3)
    found_numbers = [number for number in crawler.crawl(1)]
    expected = ["555-555-9876", "555-555-1234", "555-555-2345"]
    assert found_numbers == expected


def test_limited_depth_crawl_proper() -> None:
    crawler = PhoneNumberCrawler(TEST_URL_HOME, 1)
    found_numbers = [number for number in crawler.crawl(1)]
    expected = []
    assert found_numbers == expected


def test_limited_depth_crawl_fail() -> None:
    crawler = PhoneNumberCrawler(TEST_URL_HOME, 2)
    found_numbers = [number for number in crawler.crawl(1)]
    expected = ["555-555-1234", "555-555-2345", "555-555-9876"]
    assert found_numbers == expected

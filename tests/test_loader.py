import pytest
from view_spam.loader import loader
from view_spam.config import details
from praw import Reddit
from praw.models import ListingGenerator


@pytest.fixture
def class_init():
    instance = loader(details)
    return instance


def test_if_instance_created(class_init):
    assert isinstance(class_init._reddit_instance, Reddit)


def test_listing_return(class_init):
    assert isinstance(class_init.get_latest_removal(), ListingGenerator)


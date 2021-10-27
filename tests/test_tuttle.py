#!/usr/bin/env python

"""Tests for `tuttle` package."""

import pytest

from tuttle.model import Account, User

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_account_creation():
    account = Account(
        name="Giro",
        number="DE39500105173911499952",
        owner=User(
            name="Harry Tuttle"
        )
    )


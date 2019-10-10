#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `accibsode` package."""

import pytest

from click.testing import CliRunner

from accibsode import accibsode
from accibsode import cli
from accibsode import specialrelativity

from scipy import constants as const

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


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'accibsode.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_beta_from_gamma_valid():
    expected = 0.0
    actual = specialrelativity.beta_from_gamma(1)
    assert expected == actual


def test_beta_from_gamma_invalid():
    with pytest.raises(ValueError):
        specialrelativity.beta_from_gamma(-0.5)


def test_beta_from_gamma_invalid2():
    with pytest.raises(ValueError):
        specialrelativity.beta_from_gamma(-5)


def test_velocity_from_beta_valid():
    expected = const.c
    actual = specialrelativity.velocity_from_beta(1.0)
    assert expected==actual


def test_velocity_from_beta_invalid():
    with pytest.raises(ValueError):
        specialrelativity.velocity_from_beta(2)


def test_gamma_from_beta_valid():
    expected =1
    actual = specialrelativity.gamma_from_beta(0)
    assert expected==actual


def test_gamma_from_beta_invalid():
    with pytest.raises(ValueError):
        specialrelativity.gamma_from_beta(1)

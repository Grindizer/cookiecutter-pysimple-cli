#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from click.testing import CliRunner

from {{cookiecutter.package_name}}.__main__ import main


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '{{cookiecutter.package_name|capitalize}} main command line invoked.\n'
    assert result.exit_code == 0

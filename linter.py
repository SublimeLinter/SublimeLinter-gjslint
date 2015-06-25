#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright (c) 2015 The SublimeLinter Community
#
# License: MIT
#

"""This module exports the GJSLint plugin linter class."""

from SublimeLinter.lint import Linter


class GJSLint(Linter):

    """Provides an interface to the gjslint executable."""

    syntax = ('javascript', 'javascriptnext', 'html')
    cmd = 'gjslint --nobeep --nosummary'
    regex = r'^Line (?P<line>\d+), (?:(?P<error>E)|(?P<warning>W)):\d+: (?P<message>[^"]+(?P<near>"[^"]+")?.*$)'
    comment_re = r'\s*/[/*]'
    defaults = {
        '--jslint_error:,+': '',
        '--disable:,': '',
        '--max_line_length:': None
    }
    inline_settings = 'max_line_length'
    inline_overrides = 'disable'
    tempfile_suffix = 'js'
    selectors = {
        'html': 'source.js.embedded.html'
    }
    config_file = ('--flagfile', '.gjslintrc', '~')

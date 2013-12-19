#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright (c) 2013 Aparajita Fishman
#
# License: MIT
#

"""This module exports the GJSLint plugin linter class."""

from SublimeLinter.lint import Linter, util


class GJSLint(Linter):

    """Provides an interface to the gjslint executable."""

    syntax = ('javascript', 'html')
    cmd = 'gjslint --nobeep --nosummary'
    regex = r'^Line (?P<line>\d+), (?:(?P<error>E)|(?P<warning>W)):\d+: (?P<message>[^"]+(?P<near>"[^"]+")?)'
    comment_re = r'\s*/[/*]'
    defaults = {
        '--jslint_error:,+': '',
        '--disable:,': '',
        '--max_line_length:': None
    }
    error_stream = util.STREAM_BOTH
    inline_settings = 'max_line_length'
    inline_overrides = 'disable'
    tempfile_suffix = 'js'
    selectors = {
        'html': 'source.js.embedded.html'
    }

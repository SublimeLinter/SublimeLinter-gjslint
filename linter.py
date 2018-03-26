from SublimeLinter.lint import Linter


class GJSLint(Linter):
    cmd = 'gjslint --nobeep --nosummary'
    regex = r'^Line (?P<line>\d+), (?:(?P<error>E)|(?P<warning>W)):\d+: (?P<message>[^"]+(?P<near>"[^"]+")?.*$)'
    defaults = {
        'selector': 'source.js - meta.attribute-with-value',
        '--jslint_error:,+': '',
        '--disable:,': '',
        '--max_line_length:': None
    }
    tempfile_suffix = 'js'

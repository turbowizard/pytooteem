from pytooteem import wraptag, tag, block
from styles import codeblock


@wraptag('td', style=codeblock)
def code():
    return """@tag('a', 'link')<br>def make_a():<br> &emsp; pass"""


@wraptag('td', style=codeblock)
@tag('a', 'link')
def make_code():
    pass


@wraptag('tr', style='')
@block(code)
@block(make_code)
def example():
    pass
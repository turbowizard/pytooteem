from pytooteem import wraptag, tag, block
from styles import codeblock


@wraptag('td', style=codeblock)
def code1():
    return """@tag('button', ('<<', 'Button', '>>'))<br>def make_code():<br>  &emsp;pass"""


@wraptag('td', style=codeblock, clas='button')
@tag('button', ('<<', 'Button', '>>'))
def make_code1():
    pass


@wraptag('tr', style='')
@block(code1)
@block(make_code1)
def example():
    pass


@wraptag('td', style=codeblock)
def code2():
    return """
        @tag('button', ('<<', 'Button', '>>'),<br> &emsp;&emsp;&emsp; clas="btn btn-default", type="submit")<br>
        def make_code2():<br>
            &emsp;pass"""


@wraptag('td', style=codeblock)
@tag('button', ('<<', 'Button', '>>'), clas="btn btn-default", type="submit")
def make_code2():
    pass


@wraptag('tr', style='')
@block(code2)
@block(make_code2)
def example2():
    pass
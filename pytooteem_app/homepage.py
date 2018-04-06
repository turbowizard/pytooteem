from pytooteem import *
from wrappers import basic_html
import examples_link, examples_buttons, examples_data
from styles import body, head_style


@wraptag('div', clas='container')
@wraptag('div', clas='hero-unit')
@wraptag('div', clas="text-center", style=head_style)
@tag('h1', 'Pytooteem')
@wraptag('p', clas="lead")
def page_header():
    return """Examples"""


@wraptag('thead')
@wraptag('tr')
@tag('th', 'Code')
@tag('th', 'HTML')
def table_head():
    pass


@wraptag('div', clas='container')
@wraptag('table', clas='table')
@block(table_head)
@block(examples_link.example)
@block(examples_buttons.example)
@block(examples_buttons.example2)
@block(examples_data.example)
@block(examples_data.example2)
@block(examples_data.example3)
def examples():
    pass


@tag('script', src='https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js')
@tag('link', rel='stylesheet', href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css', integrity='sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u', crossorigin='anonymous')
@tag('link', rel="stylesheet", href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css", integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp", crossorigin="anonymous")
@tag('script', src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js', integrity='sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa', crossorigin='anonymous')
def scripts():
    pass


@wraptag('body', style=body)
@block(page_header)
@block(examples)
@block(scripts)
def page_body():
    pass


@wraptag('head')
@tag('title', 'PyTooteem')
def page_head():
    pass


@basic_html
@block(page_head)
@block(page_body)
def pytooteem_home_page():
    pass



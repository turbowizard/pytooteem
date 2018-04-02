from flask import Flask, render_template
from pytooteem import wraptag, tag, plain, block
import styles as css

app = Flask('')


@wraptag('div', style=css.black_gradient_box)
@wraptag('button', style=css.red_round_button)
def boom_box(v):
    return v


@app.route('/1')
def boombox():
    return render_template('dev.html', micro_face=boom_box(''))


@wraptag('ul')
@tag('li', 'lis1')
@tag('li', 'lis2')
@tag('li', 'lis3')
def listit(v):
    v


@app.route('/2')
def listitex():
    return render_template('dev.html', micro_face=listit(''))


@wraptag('div', clas='btn-group', role="toolbar", style=css.black_gradient_box)
@tag('div', 'hoi', clas="btn btn-default")
@tag('div', 'hoi', clas="btn btn-default")
@tag('div', 'hoi', clas="btn btn-default")
def ittnn(v):
    return v


@app.route('/3')
def listt():
    return render_template('dev.html', micro_face=ittnn(''))

##########################################

@tag('script', src='https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js')
@tag('link', rel='stylesheet', href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css', integrity='sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u', crossorigin='anonymous')
@tag('link', rel="stylesheet", href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css", integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp", crossorigin="anonymous")
@tag('script', src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js', integrity='sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa', crossorigin='anonymous')
def scripts():
    pass

body = """align-items: center;
  justify-content: center;"""


@wraptag('p')
@wraptag('a', clas='btn btn-primary btn-large')
def example_button():
    return 'b1', 'b2'


@wraptag('head')
@tag('title', 'example_title')
def my_header():
    pass


@wraptag('body', style=body)
@wraptag('div', clas='container')
@wraptag('div', clas='hero-unit', style='background:lightgrey;padding:30px;')
@tag('h1', 'Example')
@tag('p', 'Example_Tagline')
@block(example_button)
@block(scripts)
def my_body():
    pass

@plain('<!DOCTYPE html>')
@wraptag('html', lang='en')
@block(my_header)
@block(my_body)
def my_example():
    pass


@app.route('/5')
def nojinja():
    return my_example()


if __name__ == '__main__':
    app.run()
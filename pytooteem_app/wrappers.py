from pytooteem import plain, wraptag, block


def basic_html(content):

    @plain('<!DOCTYPE html>')
    @wraptag('html', lang='en')
    @block(content)
    def simple_html_wrapper():
        pass

    return simple_html_wrapper



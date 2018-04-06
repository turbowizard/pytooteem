from pytooteem import wraptag, tag, block, data
from styles import codeblock
from data import recipe, get_recipe_steps


@wraptag('td', style=codeblock)
def code():
    return """
    @wraptag('table')<br>
    @data(recipe)<br>
    def make_code(element):<br>
        &emsp; @wraptag('tr')<br>
        &emsp; @tag('td', element[0])<br>
        &emsp; @tag('td', element[1])<br>
        &emsp; @tag('td', element[2])<br>
        &emsp; def make_row():<br>
            &emsp; &emsp; pass<br>
        &emsp; return make_row()"""


@wraptag('td', style=codeblock)
@wraptag('table')
@data(recipe)
def make_code(element):
    @wraptag('tr')
    @tag('td', element[0])
    @tag('td', element[1])
    @tag('td', element[2])
    def make_row():
        pass
    return make_row()


@wraptag('tr', style='')
@block(code)
@block(make_code)
def example():
    pass


@wraptag('td', style=codeblock)
def code2():
    return """
        @wraptag('table', clas='table table-bordered')<br>
        @data(recipe)<br>
        def make_code2(element):<br>
            &emsp; @wraptag('tr')<br>
            &emsp; @tag('td', element[0], clas="active")<br>
            &emsp; @tag('td', element[1], clas="info")<br>
            &emsp; @tag('td', element[2], clas='success')<br>
            &emsp; def make_row():<br>
                &emsp; &emsp; pass<br>
            &emsp; return make_row()"""


@wraptag('td', style=codeblock)
@wraptag('div', style='background:white;')
@wraptag('table', clas='table table-bordered')
@data(recipe)
def make_code2(element):
    @wraptag('tr')
    @tag('td', element[0], clas="active")
    @tag('td', element[1], clas="info")
    @tag('td', element[2], clas='success')
    def make_row():
        pass
    return make_row()


@wraptag('tr')
@block(code2)
@block(make_code2)
def example2():
    pass


@wraptag('td', style=codeblock)
def code3():
    return """
        @wraptag('table', clas='table table-bordered')<br>
        @data(get_recipe_steps())<br>
        def make_code3(step):<br>
            &emsp; @wraptag('tr')<br>
            &emsp; @tag('td', step.amount, clas="active")<br>
            &emsp; @tag('td', step.volume, clas="info")<br>
            &emsp; @tag('td', step.content, clas='success')<br>
            &emsp; def make_row():<br>
                &emsp; &emsp; pass<br>
            &emsp; return make_row()"""


@wraptag('td', style=codeblock)
@wraptag('div', style='background:white;')
@wraptag('table', clas='table table-bordered')
@data(get_recipe_steps())
def make_code3(step):
    @wraptag('tr')
    @tag('td', step.amount, clas="active")
    @tag('td', step.volume, clas="info")
    @tag('td', step.content, clas='success')
    def make_row():
        pass
    return make_row()


@wraptag('tr')
@block(code3)
@block(make_code3)
def example3():
    pass

# pytooteem  

HTML Tag Decorator.

## Getting Started

Clone or Download  
`python install setup.py`  
 
### examples 
`from pytooteem import tag` 
  
Bold wrap:    
`@tag('b')`  
`def make_bold(value):`  
&nbsp;&nbsp;&nbsp;&nbsp;`return value`  
`print make_bold('my_name')`  
Result: <b>my_name</b>  

Passing attributes (argument order preserved in 3.6):  
`@tag('a',href='#', taget='_self')`  
`def make_a(value):`  
&nbsp;&nbsp;&nbsp;&nbsp;`return value`  
`print make_a('my_link')`  
Result: <a href="#" target="_self">my_link</a>  

Passing class attribute ('class' reserved by python )  
`@tag('div',clas='my_div')`  
`def make_div(value):`  
&nbsp;&nbsp;&nbsp;&nbsp;`return value`  
`print make_div('my_div')`  
Result: <div class="my_div">my_div</div>  

Tag stacking  
`@tag('a')`  
`@tag('b')`  
`def make_a(value):`  
&nbsp;&nbsp;&nbsp;&nbsp;`return value`  
`print make_a('my_link')`  
Result: <a><b>my_link</b></a>  

## Testing	
`pytest -v`




 
  


    
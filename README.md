# pytooteem  

Wrap code with html using Python decorators.

## Getting Started

Clone or Download  
`cd pytooteem`  
`python setup.py install`  
 
### Simple Example 
	from pytooteem import wraptag
	
	@wraptag('button')     
	@tag('h3', 'pytooteem'.upper(), style='background:MediumSeaGreen;') 
	def make_h3():  
		pass  
	assert make_h3() == '<button><h3 style="background:MediumSeaGreen;">PYTOOTEEM</h3></button>'  
 
<button><h3 style="background:MediumSeaGreen;">PYTOOTEEM</h3></button>  

## Usage

### Blocks  

Block is a decorated function that defines HTML layering of an element 

	...  
	@pytooteemdecorator  
	@pytooteemdecorator  
	def block(): 
		pass   


***
### Tag Decorator  
 

	from pytooteem import tag 

Empty tag    
  
	@tag(String)  
ex: `@tag('button')` <button></button> 

Tag with value    
  
	@tag(String, String)   
ex: `@tag('button', 'button')` <button>button</button>  

Tag with attributes    
  
	@tag(String, **kwargs)    
ex: `@tag('button', disabled='')` <button disabled=""></button>  

* Pass 'class' as html attribute 
 
		@tag(String, clas='')    
ex: `@tag('button', clas='button')` <button class="button"></button>    

Tag with container    
  
	@tag(String, tuple))    
ex: `@tag('button', ('b1', 'b2'))` <button>b1</button><button>b2</button> 

***
### Wraptag Decorator 
 

	from pytooteem import wrapatg 

Empty wrap    
  
	@wraptag(String)  
ex: `@wraptag('button')` <button></button>  

Wrap with attributes    
  
	@wraptag(String, **kwargs)    
ex: `@wraptag('button', disabled='')` <button disabled=""></button> 

***
### Plain Decorator 
 
	from pytooteem import plain  

Empty wrap    
  
	@plain(String)  
ex: `@plain('<button>')` <button>  

***
### Block Decorator 
  
	from pytooteem import block  

	# example block  
	@tag('button')   
	def button_block():  
		pass    

Single block
 
	@block(button_block)   
	def parent_block():    
		pass`  
ex:  
 `parent_block()` <button></button>   

Multiple blocks   

	@block(button_block)    
	@block(button_block)   
	def parent_block():     
		pass   
ex:  
 `parent_block()` <button></button><button></button>   

***

### Recipes  

Recipe is a function containing dynamic HTML definition for a block.  

    def recipe():
		@pytooteemdecorator
        def make_recipe():
            pass
        return make_recipe()  
***

### Data Decorator  
Recipe decorator, combine Data with HTML

	from pytooteem import data  

2D container  
  
	@data(2dcontainer)  

ex:   
  
	@data((('d1', 'd2'), ('p1', 'p2')))  
    def li_recipe(element):  
        @wraptag('ul')  
        @tag('li', element[0])  
        @tag('li', element[1])  
        def li_block():  
            pass  
        return li_block()  

<ul><li>d1</li><li>d2</li></ul><ul><li>p1</li><li>p2</li></ul>  

Object Container  
  
	@data(object_container)  

ex:   
  
	@data(get_objects())  
    def li_recipe(element):  
        @wraptag('ul')  
        @tag('li', element.instance_variable1)  
        @tag('li', element.instance_variable2)    
        def li_block():  
            pass  
        return li_block()  

## Pytooteem_app  

Examples over Flask application

## Testing	

`pytest -v`




 
  


    
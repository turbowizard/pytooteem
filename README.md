# pytooteem  

Easy and Dynamic markup with Python decorators to close the distance between models and views.

## Getting Started

Clone or Download  
`cd pytooteem`  
`python setup.py install`  
 
### Simple Example 
	from pytooteem import wraptag, tag
	
	@wraptag('div', style='background:MediumSeaGreen;')     
	@tag('h3', 'pytooteem'.upper()) 
	def make_h3():  
		pass  
	assert make_h3() == '<div style="background:MediumSeaGreen;"><h3>PYTOOTEEM</h3></div> '  
 
<div style="background:MediumSeaGreen;"><h3>PYTOOTEEM</h3></div>  

## Usage

### Tag Decorator  

Use the tag decorator to define a tag and its properties. 
 

	from pytooteem import tag  

Tag decorator arguments 
	
	@tag(tag_name, tag_content, tag_attributes)	

	expected types:  
	tag_name as String  
	tag_content as String or Container
	tag_attributes as **kwargs  

Tag types


	Empty tag 
	@tag(String)

	Tag with value      
	@tag(String, String)    

	Tag with attributes      
	@tag(String, **kwargs)    

	Tag with container - create tag for each element in container     
	@tag(String, container)
  
Special cases

	Passing 'class' as attribute  
	@tag(String, clas='')    

Example

`@tag('b', ('hello', 'world'), style='margin:10px;background:lightBlue;')`  

<b style="margin:10px;background:lightBlue;">hello</b><b style="margin:10px;background:lightBlue;">world</b>

 



***
### Wraptag Decorator 

Use wraptag decorator to wrap following markup or value returned by function.  

	from pytooteem import wrapatg  

Wraptag decorator arguments 
	
	@tag(tag_name, tag_attributes)	

	expected types:  
	tag_name as String  
	tag_attributes as **kwargs  

Wraptag types  

	Empty wrap      
	@wraptag(String)   

	Wrap with attributes    
	@wraptag(String, **kwargs)    

Example

`@wraptag('p', style='background:DarkSlateGray;' )`   
`@tag('b', ('hello', 'world'), style='margin:10px;background:lightBlue;')`  

<p style="background:DarkSlateGray;">
<b style="margin:10px;background:lightBlue;">hello</b><b style="margin:10px;background:lightBlue;">world</b></p>  


***
### Plain Decorator 

Use to embed plain text
 
	from pytooteem import plain  

Example

`@plain('<b>BOLD</b>')`   


<b>BOLD</b> 

***

### Tootblock and Block decorator

**Tootblock** , group of markup tags, is a  decorated function that defines tag relations and relative appearance.  

	...  
	@pytooteemdecorator  
	@pytooteemdecorator  
	def toot_block(): 
		pass   

Example

	@wraptag('p', style='background:DarkSlateGray;' )  
	@tag('b', ('hello', 'world'), style='margin:10px;background:lightBlue;')  
	def my_tootblock():
		pass  

<p style="background:DarkSlateGray;">
<b style="margin:10px;background:lightBlue;">hello</b><b style="margin:10px;background:lightBlue;">world</b></p>  


### Block Decorator  

Use to insert a tootblock  
  
	from pytooteem import block   

Tootblock decorator arguments  

	@tag(tootblock)  

	expected types:
	tootblock as function  

Example

	@block(my_tootblock)
	@plain('<br>')
	@block(my_tootblock)
	def double_toot():
		pass  

<p style="background:DarkSlateGray;">
<b style="margin:10px;background:lightBlue;">hello</b><b style="margin:10px;background:lightBlue;">world</b></p> 
<br>
 <p style="background:DarkSlateGray;">
<b style="margin:10px;background:lightBlue;">hello</b><b style="margin:10px;background:lightBlue;">world</b></p>  
	 

***

### Toottemplates 

Toottemplate is a function containing markup instruction for a tootblock.  

    def template():
		@pytooteemdecorator
        def block():
            pass
        return block()   

Example

	def my_toottemplate():
		@wraptag('p', style='background:DarkSlateGray;' )  
		@tag('b', ('hello', 'world'), style='margin:10px;background:lightBlue;')  
		def my_tootblock():
			pass  
		return my_tootblock()


***

### Data Decorator  
Use to dynamically populate toottemapltes with each container elements.

	from pytooteem import data  

Data decorator arguments

	@data(elements)

	expected types:
	elements as 2d container or object container

Examples
 
embed arguments by position  

`my_data=(('this', 'is'), ('my', 'data'))`

	@data(my_data)  
    def toottemplate(element):  
        @wraptag('ul')  
        @tag('li', element[0])  
        @tag('li', element[1])  
        def li_block():  
            pass  
        return li_block()  

<ul><li>this</li><li>is</li></ul><ul><li>my</li><li>data</li></ul>  

embed arguments by name  
  
	@data(get_objects())  
    def toottemplate(element):  
        @wraptag('ul')  
        @tag('li', element.instance_variable1)  
        @tag('li', element.instance_variable2)    
        def li_block():  
            pass  
        return li_block()  

## Pytooteem_app  

Examples over Flask application.

## Testing	

`pytest -v`




 
  


    
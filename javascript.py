/**
*
*                 ************* JAVASCRIPT CAN CHANGE HTML CONTENT ***************
*
*To change the content in a html tag , we givr that tag an id and access it in javascript 
*via the  getElememntByid method . All conenet in the html can be accessed by the document tag
*We can then allter the conent by using element content innerHTML and equate it to the new value
*
*HTML                                          javascript
*<div id='demo'>George<div/>                documemnt.getElementById('demo').innehtml="Boniface"
*
*This changes the div content from George to Boniface
*
*
*                 ************* JAVASCRIPT CAN CHANGE ATTRIBUTE VALUES ***************
*    HTML                                            JAVASCRIPT
*  <img id='images' src="dog.img">                 document.getElementById('images').src='cat.img'
*                  ---------                                                          ----------   
*
*
*                 ************* JAVASCRIPT CAN CHANGE CSS STYLES VALUES OF HTML TAGS ***************
*     
*     HTML                                                          JAVASCRIPT 
*   <p id='demo' style="fontsize:15px">Hellow<p>                    document.getElementById('demo').style.fontSize='35px'
*
*
*
*                 ************* JAVASCRIPT DISPLAY POSSIBILITIES ***************
*                          
*              JavaScript can "display" data in different ways:
*              
*              Writing into an HTML element, using innerHTML.
*              Writing into an alert box, using window.alert().
*              Writing into the browser console, using console.log().
*              Writing into the HTML output using document.write().   NOTE --> NEVER USE THIS ONE .IT OVERWRITES/DELETES ALL HTML CONTENT.
*
*
*                 ************* JAVASCRIPT KEYWORDS ***************
*          KEYWORD                                         DESCRIPTION
*           var	                                              Declares a variable
*           let	                                              Declares a block variable
*           const                                             Declares a block constant
*           if	                                              Marks a block of statements to be executed on a condition
*           switch                                            Marks a block of statements to be executed in different cases
*           for	                                              Marks a block of statements to be executed in a loop
*           function                                          Declares a function
*           return                                            Exits a function
*           try                                               Implements error handling to a block of statements
*
*
*                ************** JAVASCRIPT EXPRESSIONS ***************
*      An expression is a combination of values, variables, and operators, which computes to a value.
*      The computation is called an evaluation.
*      For example, 5 * 10 evaluates to 50:
*      Or e.g let x =5 ,  x * 10 = 50:
*
*
*                ************** JAVASCRIPT IDENTIFIERS/VARIABLE NAMES ***************
*                      A JavaScript name must begin with:
*                          
*                          A letter (A-Z or a-z)
*                          A dollar sign ($)
*                          Or an underscore (_)
*
*                         JavaScript is Case Sensitive
*                         All JavaScript identifiers are case sensitive. 
*                         The variables lastName and lastname, are two different variables
*                         JavaScript does not interpret LET or Let as the keyword let.
*
*                ************** JAVASCRIPT MULTIPLE NAMES FOR VARIABLES ***************
*               Historically, programmers have used different ways of joining multiple words into one variable name:
*                   what is allowed
*
*                   Underscore:                       first_name, last_name, master_card, inter_city.
*                   Upper Camel Case (Pascal Case):   FirstName, LastName, MasterCard, InterCity.
*                   Lower Camel Case:                 firstName, lastName, masterCard, interCity. 
*
*              JavaScript programmers tend to use camel case that starts with a lowercase letter:
*              
*                   What is not allowed
*                     Hyphens:                         Hyphens are not allowed in JavaScript. They are reserved for subtractions.
*
*
*
*                ************** JAVASCRIPT   ->  LET ***************
*
*                   Variables defined with let cannot be Redeclared.
*                   Variables defined with let must be Declared before use.
*                   Variables defined with let have Block Scope.
*
*               The block scope simply means using the double parentheesis i.e {}
*               All code written in those parenthesis are in that block and variables 
*               declared using the let key word can only be accessed within this block.
*               { 
*                  let x =10   
*                     console.log(x)               Here we can access x  since we are within  the block scope                      
*               }
*              console.log(x)  -  Here we can not access the x because it is not within the block scope
*     
*                           How ever this is not the case with the var key word
*                    Variables declared with the var keyword can NOT have block scope.
*                    Variables declared inside a { } block can be accessed from outside the block.
*                                      {
*                                         var x = 2;
*                                       }
*                                       // x CAN be used here
*
*                          REDECLARING VARIABLES using var key word
*                 It is possible to redclare variables using the var keyword
*                 How ever redeclaring a variable using the var keyword can impose problems.
*                 This is because redeclaring a variable inside a block will also redeclare the variable outside the block:

*                                var x = 10;
*                                // Here x is 10
*
*                                {
*                                var x = 2;
*                                // Here x is 2
*                                }
*
*                                // Here x is 2
*
*
*                        How ever Redeclaring variables using the let key world sollves this problem
*                        Redeclaring a variable inside a block will not redeclare the variable outside the block:     
*                                     FOR EXAMPLE
*                               let x = 10;
*                               // Here x is 10
*                               
*                               {
*                               let x = 2;
*                               // Here x is 2
*                               }
*                               
*                               // Here x is 10
*
*
*                         REDECRAING VARIABLES WITH VAR AND LET
*                              Redeclaring a JavaScript variable with var is allowed anywhere in a program:
*                              var x = 2;
*                              // Now x is 2
*                              
*                              var x = 3;
*                              // Now x is 3
*                              
*                              With let, redeclaring a variable in the same block is NOT allowed:
*                              
*                              Example
*                              var x = 2;   // Allowed
*                              let x = 3;   // Not allowed
*                              
*                              {
*                              let x = 2;   // Allowed
*                              let x = 3;   // Not allowed
*                              }
*                              
*                              {
*                              let x = 2;   // Allowed
*                              var x = 3;   // Not allowed
*                              }
*                              Redeclaring a variable with let, in another block, IS allowed:
*                              
*                              Example
*                              let x = 2;   // Allowed
*                              
*                              {
*                              let x = 3;   // Allowed
*                              }
*                              
*                              {
*                              let x = 4;    // Allowed
*                              }
*                ************** JAVASCRIPT   ->  CONST ***************
*
Variables defined with const cannot be Redeclared.
Variables defined with const cannot be Reassigned.
Variables defined with const have Block Scope.

*                                Cannot be Reassigned
A const variable cannot be reassigned:

Example
const PI = 3.141592653589793;
PI = 3.14;      // This will give an error
PI = PI + 10;   // This will also give an error

*                                 Must be Assigned
JavaScript const variables must be assigned a value when they are declared:

Correct
const PI = 3.14159265359;
Incorrect
const PI;
PI = 3.14159265359;
*                                 When to use JavaScript const?
Always declare a variable with const when you know that the value should not be changed.

Use const when you declare:

A new Array
A new Object
A new Function
A new RegExp

*                            Constant Objects and Arrays
The keyword const is a little misleading.
It does not define a constant value. It defines a constant reference to a value.
Because of this you can NOT:

Reassign a constant value
Reassign a constant array
Reassign a constant object

But you CAN:

Change the elements of constant array
Change the properties of constant object

Constant Arrays
You can change the elements of a constant array:

Example
// You can create a constant array:
const cars = ["Saab", "Volvo", "BMW"];

// You can change an element:
cars[0] = "Toyota";

// You can add an element:
cars.push("Audi");
But you can NOT reassign the array:

Example
const cars = ["Saab", "Volvo", "BMW"];

cars = ["Toyota", "Volvo", "Audi"];    // ERROR


*            ******************** JAVASCRIPT ASSIGNMENT OPERATORS ******************

Assignment operators assign values to JavaScript variables.

The Addition Assignment Operator (+=) adds a value to a variable.

Operator	   Example	           Same As
=	           x = y	           x = y
+=	           x += y	           x = x + y
-=	           x -= y	           x = x - y
*=	           x *= y	           x = x * y
/=	           x /= y	           x = x / y
%=	           x %= y	           x = x % y
**=	           x **= y	           x = x ** y

*                       ********* JAVASCRIPT COMPARISON OPERATORS **************
*                    Operator	                   Description
*                    ==	                             equal to
*                    ===	                         equal value and equal type
*                    !=	                             not equal
*                    !==	                         not equal value or not equal type
*                    >	                             greater than
*                    <	                             less than
*                    >=	                             greater than or equal to
*                    <=	                             less than or equal to
*                    ?	                             ternary operator
*                    
*                                   JavaScript Logical Operators
*                                 Operator	            Description
*                                 &&	               logical and
*                                 ||	               logical or
*                                 !	                   logical not
*                                 
*
*                             ********************  Common HTML Events  *******************
*                                     Here is a list of some common HTML events:

*                                     Event	                 Description
*                                     onchange	                An HTML element has been changed
*                                     onclick	                The user clicks an HTML element
*                                     onmouseover               The user moves the mouse over an HTML element
*                                     onmouseout	            The user moves the mouse away from an HTML element
*                                     onkeydown	                The user pushes a keyboard key
*                                     onload	                The browser has finished loading the page
*
*                
*                             ********************  How to put double quotes in strings  *******************

*                                    use the backslash escape character.*                                    
*                                    The backslash (\) escape character turns special characters into string characters:
*                                    
*                                    Code      	Result    	Description
*                                    \'         '	       Single quote
*                                    \"	        "	       Double quote
*                                    \\	        \	       Backslash
*
*
*

#myLambda#
This example is written in github flavored markdown if we want to publish it later. For optimum reading experience copy and paste it into: http://github.github.com/github-flavored-markdown/preview.html

##Motivation##
myLambda is a minimalist approach to write a functional programming language which implements not too much more than the underlying theorie, the [lambda calculus](http://en.wikipedia.org/wiki/Lambda_calculus).

We call it currently myLambda because it's just a personal project from a bunch of students trying to understand how programming languages and their foundational formal systems work. If you don't really like that name, please suggest
another. We don't like it that much either ;-)

##A brief example##
Let me give you a taste of the currently planned syntax. For more information consult the EBNF, our grammar. The syntax of myLambda is close to the usual way to describe functions in the lambda calculus.
How to calculate a given faculty? Well, easy:
fac = #x: if(<=(x 1) 1 +(fak(-(x 1) -(x 2)))).

Calculate a given fibonacci number:
fibo = #x: if(==(x 0) 0 
           (if(==(x 1) 1)
           +(fibo(-(x 1)) fibo(-(x 2))))).


As you may noticed currently we use prefix notation, so x+1 is written +(x 1). We plan to migrate to the familiar infix notation once myLambda is up and running.

##Functions##
An anonymous function, a lambda, that takes x as a parameter, adds 1 and exits is expressed as below:
\#x: +(x 1).
The # is our substitute for λ, the trailing dot marks the end of an expression. (If you only read the markdown source code, please notice that the backslash is used only to escape the hash mark.)

Lambda expressions can be nested like this:
\#x: (#y: *(x y)).
This is just a complicated way to express #x y: *(x y). It is called Currying. The interpreter does that automatically, don't worry. 
A lambda expression without arguments always returns itself:
\#x: +(x 1).
=> \x: +(x 1).

There are some builtin functions like == for equality, != for inequality, or, respectively ^ for logical or and so on. Quite important is the if function. It is written as:
if(cond1 doThisIfConditionMatches doThisIfItDoesNot). For example:
greater_than_42? = #x: if(>(x 42) true).

###Function Invocations###
To apply a given value to a function we have to type:
\#x: +(x 1) (5).
=> 6.
At first the function's identifier and than the arguments separated by whitespace.

##Binding Expressions via Identifiers##
Everything in myLambda is a function expression. What is, let's say 3? It's just #x: 3. Or it can be expressed as #x: + (1 (#x: + (1 (#x: +(1 (#x: 0)))))). which is 0+1+1+1.

If we want to bind an expression to a name for reusing it for example for recursion or to make the code more readable you can do it like this: 

= (increment #x: +(1 x)).
As a shortcut it is allowed to write:
increment = #x: +(1 x).
is_even? = #x: %(x 2).
sum = #x y: +(x y).
Pi = #x: 3.14. 
As a shortcut it is also allowed to write Pi = 3.14.
Of course Pi() returns 3.14. and is_even?(23) returns false.

Identifiers have to start with a letter or underscore, then any alphanumeric char is allowed and they can end with a question mark.

##Types##
We have only a few types. Functions, numbers, booleans, more? In addition myLambda is dynamically typed for good reasons. Which? FIXME!

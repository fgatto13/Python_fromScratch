# Polymorphism
*to have many forms or faces*

It is an essential concept in Object-Oriented Programming.
There are **two** ways to achieve it:
1. *Inheritance*: an object could be treated of the same type as a parent class
2. *Duck Typing*: object **must have** necessary attributes/methods

In the example found in ```poly_inheritance.py``` we use inheritance to showcase polymorphism:
- we define the super class as having an abstract method
- each child class has to implement its own version of the abstract method

In ```poly_ducktyping.py``` there are a few examples of how to use duck typing:
- an object **must have** the minimum necessary attributes/methods
- *if it looks like a duck, and quacks like a duck, it must be a duck*

Basically, in duck typing we don't use inheritance, but rather its characteristics.
For instance, both dogs and cats are animals, and are able to produce sounds.
- Therefore, they will both have a speak() method
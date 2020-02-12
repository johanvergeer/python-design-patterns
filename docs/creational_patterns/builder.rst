Builder
=======

Intent
------
Separate the construction of a complex object from its representation
so that the same construction process can create different representations.

Explanation
-----------

Real world example

    Imagine a character generator for a role playing game.
    The easiest option is to let computer create the character for you.
    But if you want to select the character details like profession, gender, hair color etc.
    the character generation becomes a step-by-step process that completes when all the selections are ready.

In plain words

    Allows you to create different flavors of an object while avoiding constructor pollution.
    Useful when there could be several flavors of an object.
    Or when there are a lot of steps involved in creation of an object.

Wikipedia says

    The builder pattern is an object creation software design pattern
    with the intentions of finding a solution to the telescoping constructor anti-pattern.

Having said that let me add a bit about what **telescoping constructor anti-pattern** is.
At one point or the other we have all seen an init function like below:

.. code-block:: python

    def __init__(self, profession: Profession, name: str, hair_type: HairType, hair_color: HairColor, weapon: Weapon)


As you can see the number of parameters can quickly get out of hand and it might become difficult to understand the arrangement of parameters.
Plus this parameter list could keep on growing if you would want to add more options in future.
This is called telescoping constructor anti-pattern.

Applicability
-------------

Use the Builder pattern when

* the algorithm for creating a complex object should be independent of the parts that make up the object and how they're assembled
* the construction process must allow different representations for the object that's constructed


Class Diagram
-------------

.. uml:: builder.puml


Programmatic Example
--------------------


.. testsetup::

    from python_design_patterns.builder import *

.. automodule:: python_design_patterns.builder
    :members:

Credits
-------

* |gof_dp|
* |jdp|

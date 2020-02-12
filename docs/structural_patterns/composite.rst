Composite
=========

Intent
------
Compose objects into tree structures to represent part-whole hierarchies.
Composite lets clients treat individual objects and compositions of objects uniformly.

Explanation
-----------

Real world example

    Every sentence is composed of words which are in turn composed of characters.
    Each of these objects is printable and they can have something printed before or after them
    like sentence always ends with full stop and word always has space before it

In plain words

    Composite pattern lets clients treat the individual objects in a uniform manner.

Wikipedia says

    In software engineering, the composite pattern is a partitioning design pattern.
    The composite pattern describes that a group of objects is to be treated
    in the same way as a single instance of an object.

    The intent of a composite is to "compose" objects into tree structures to represent part-whole hierarchies.
    Implementing the composite pattern lets clients treat individual objects and compositions uniformly.


Applicability
-------------
Use the Composite pattern when

* you want to represent part-whole hierarchies of objects
* you want clients to be able to ignore the difference between compositions of objects and individual objects.
  Clients will treat all objects in the composite structure uniformly

Class diagram
-------------

.. uml:: composite.puml

Programmatic Example
--------------------

.. testsetup::

    from python_design_patterns.composite import *

.. automodule:: python_design_patterns.composite
    :members:

Credits
-------

* |gof_dp|
* |jdp|

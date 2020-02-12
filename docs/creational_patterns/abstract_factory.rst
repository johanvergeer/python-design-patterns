Abstract Factory
================

Also known as
-------------

Kit

Intent
------

Provide an interface for creating families of related or dependent objects without specifying their concrete classes.

Explanation
-----------

Real world example

    To create a kingdom we need objects with common theme.
    Elven kingdom needs an Elven king, Elven castle and Elven army whereas Orcish kingdom needs an Orcish king,
    Orcish castle and Orcish army. There is a dependency between the objects in the kingdom.

In plain words

    A factory of factories; a factory that groups the individual but related/dependent factories together without specifying their concrete classes.

Wikipedia says

    The abstract factory pattern provides a way to encapsulate a group of individual factories that have a common theme without specifying their concrete classes

Applicability
-------------

Use the Abstract Factory pattern when

* a system should be independent of how its products are created, composed and represented
* a system should be configured with one of multiple families of products
* a family of related product objects is designed to be used together, and you need to enforce this constraint
* you want to provide a class library of products, and you want to reveal just their interfaces, not their implementations
* the lifetime of the dependency is conceptually shorter than the lifetime of the consumer.
* you need a run-time value to construct a particular dependency
* you want to decide which product to call from a family at runtime.
* you need to supply one or more parameters only known at run-time before you can resolve a dependency.
* you need consistency among products
* you don’t want to change existing code when adding new products or families of products to the program.

Use Cases
---------

* Selecting to call the appropriate implementation of FileSystemAcmeService or DatabaseAcmeService or NetworkAcmeService at runtime.
* Unit test case writing becomes much easier
* UI tools for different OS

Consequences
------------

* While the pattern is great when creating predefined objects, adding the new ones might be challenging.
* The code may become more complicated than it should be,
  since a lot of new interfaces and classes are introduced along with the pattern.


Class Diagram
-------------

.. uml:: ./abstract_factory.puml

Programmatic Example
--------------------

.. testsetup::

    from python_design_patterns.abstract_factory import *

.. automodule:: python_design_patterns.abstract_factory
    :members:

Credits
-------

* |gof_dp|
* |jdp|

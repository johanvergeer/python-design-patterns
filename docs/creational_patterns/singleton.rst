Singleton
=========

Intent
------

Ensure a class only has one instance, and provide a global point of access to it.

Explanation
-----------

Real world example

    There can only be one ivory tower where the wizards study their magic. The same enchanted ivory tower is always used by the wizards.
    Ivory tower here is singleton.

In plain words

    Ensures that only one object of a particular class is ever created.

Wikipedia says

    In software engineering, the singleton pattern is a software design pattern that restricts the instantiation of a class to one object.
    This is useful when exactly one object is needed to coordinate actions across the system.

Applicability
-------------

Use the Singleton pattern when

* There must be exactly one instance of a class, and it must be accessible to clients from a well-known access point
* When the sole instance should be extensible by subclassing,
  and clients should be able to use an extended instance without modifying their code

Typical Use Cases
-----------------

* The logging class
* Managing a connection to a database
* File manager

Consequences
------------

* Violates Single Responsibility Principle (SRP) by controlling their own creation and lifecycle.
* Encourages using a global shared instance which prevents an object and resources used by this object from being deallocated.
* **Creates tightly coupled code.** The clients of the Singleton become difficult to test.
* Makes it almost impossible to subclass a Singleton.

Class diagram
-------------
.. uml:: singleton.puml

Programmatic Example
--------------------

.. testsetup::

    from python_design_patterns.singleton import *

.. automodule:: python_design_patterns.singleton
    :members:

Credits
-------

* |gof_dp|
* |jdp|
* |j2ee_dp|

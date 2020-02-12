Memento
=========

Also known as
-------------

Token

Intent
------

Without violating encapsulation, capture and externalize an
object's internal state so that the object can be restored to this state later.

Explanation
-----------

.. todo:: Describe explanation


Applicability
-------------

Use the Memento pattern when

* a snapshot of an object's state must be saved so that it can be restored to that state later, and
* a direct interface to obtaining the state would expose implementation details and break the object's encapsulation

Class diagram
-------------
.. uml:: memento.puml


Typical Use Cases
-----------------

.. todo:: Describe typical use cases

Programmatic Example
--------------------

.. testsetup::

    from python_design_patterns.memento import *

.. automodule:: python_design_patterns.memento
    :members:

Credits
-------

* |gof_dp|

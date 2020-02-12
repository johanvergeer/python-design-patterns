#set($Pattern_name = ${StringUtils.removeAndHump(${NAME}, ".")})
#set($Pattern_name = $Pattern_name.substring(0,1).toUpperCase() + $Pattern_name.substring(1))
${Pattern_name}
=========

Also known as
-------------

.. todo:: Describe alternative names

Intent
------

.. todo:: Describe intent

Explanation
-----------

.. todo:: Describe explanation


Applicability
-------------

Use the ${Pattern_name} pattern when

.. todo:: Describe applicability

Class diagram
-------------
.. uml:: ${NAME}.puml


Typical Use Cases
-----------------

.. todo:: Describe typical use cases

Consequences
------------

.. todo:: Describe consequences

Programmatic Example
--------------------

.. testsetup::

    from python_design_patterns.${NAME} import *

.. automodule:: python_design_patterns.${NAME}
    :members:

Credits
-------

* |gof_dp|
* |jdp|
* |j2ee_dp|

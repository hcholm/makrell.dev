Program Flow
============

Conditionals
------------

.. code-block:: makrell

    {if 2 < 3                       # an expression that evaluates to "2 is less than 3"
        "2 is less than 3"
        "2 is not less than 3"
    }

Loops
-----

.. code-block:: makrell

    a = 0
    {while a < 5                    # a loop that prints numbers from 0 to 4
        a | print
        a = a + 1
    }

Pattern Matching
----------------

.. code-block:: makrell

    {match 2
        2
            "two"
        [_ 3|5]
            "list with two elements, second is 3 or 5"
        _:str
            "a string"
        _ 
            "something else"
    }
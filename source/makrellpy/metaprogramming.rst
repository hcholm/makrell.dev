Metaprogramming
===============

Metaprogramming is a programming technique in which computer programs can treat other program code as data and modify the program code. This is a powerful technique, but should be used with caution, as it can make the code harder to understand and maintain. In MakrellPy, metaprogramming code is executed at compile time, and can be used to generate code, implement domain-specific languages and more.

Macros
------

A common use of metaprogramming is to define macros, which are code templates that can be expanded into other code. In MakrellPy, macros are defined using the ``macro`` keyword. The macro body is a block of code that is executed when the macro is expanded. The macro body can contain other macros, which are expanded recursively.

.. code-block:: makrell

    {macro

    }


The Meta
--------

.. code-block:: makrell

    {meta

    }

TBD

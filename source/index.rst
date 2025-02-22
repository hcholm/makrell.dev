Makrell
=======

Makrell is a family of programming languages implemented in Python. It consists currently of these languages:

* MakrellPy, a general-purpose, functional programming language with two-way Python interoperability, metaprogramming support and simple syntax.
* MRON (Makrell Object Notation), a lightweight alternative to JSON.
* MRML (Makrell Markup Language), a lightweight alternative to XML and HTML.
* Makrell Base Format (MBF), a simple data format that forms the basis for both MakrellPy, MRON and MRML.

The project is in an early stage of development and is not yet ready for production use.

Here is a basic Makrell function:

.. code-block:: makrell

    # function definition
    
    {add [x y]
        x + y  # implicit return
    }

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   introduction
   syntax
   examples

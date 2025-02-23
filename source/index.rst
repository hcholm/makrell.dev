.. image:: /_static/makrell.png
    :alt: Makrell
    :align: center
    :width: 200
    :height: 200

Makrell
=======

Makrell is a family of programming languages implemented in Python. It consists currently of these languages:

* **MakrellPy**, a general-purpose, functional programming language with two-way Python interoperability, metaprogramming support and simple syntax.
* **MRON** (Makrell Object Notation), a lightweight alternative to JSON.
* **MRML** (Makrell Markup Language), a lightweight alternative to XML and HTML.
* **Makrell Base Format** (MBF), a simple data format that forms the basis for both MakrellPy, MRON and MRML.

Quick Start
-----------

Installation
^^^^^^^^^^^^

.. code-block:: bash

    $ pip install makrell


MakrellPy REPL usage
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ makrell
    > 2 + 3
    5
    > [2 3 5] | sum
    10

Run a MakrellPy script
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ makrell myscript.mr

IDE Support
-----------

MakrellPy is supported by the MakrellPy Language Server, included in the Makrell package. The language server is based on the [LSP](https://microsoft.github.io/language-server-protocol/) protocol and can be used with any LSP-compatible editor, such as Visual Studio Code, Sublime Text, Atom, Vim, Emacs etc. A VS Code extension is available [here](https://marketplace.visualstudio.com/items?itemName=hcholm.vscode-makrell).

.. image:: /_static/ide.png
    :alt: MakrellPy in VS Code

MakrellPy
---------

Main article: :doc:`makrellpy/index`

The following is a quick introduction by example to the MakrellPy language.

.. code-block:: makrell

    # This is a comment.
    a = 2                   # assignment
    b = a + 3               # arithmetic expression 
    {sum [a b 5]}           # function call
    [a b 5] | sum           # function call by pipe operator
    sum \ [a b 5]           # function call by reverse pipe operator

    {if a < b               # conditional expression
        "a is less than b"
        "a is not less than b"}

    {fun add [x y]          # function definition
        x + y}

    add3 = {add 3 _}        # partial application
    {add3 5}                # 8

    a = 2 | {+ 3} | {* 5}   # operators as functions, evaluates to 25

    {match a                # pattern matching, user extensible
        2
            "two"
        [_ 3|5]
            "list with two elements, second is 3 or 5"
        _:str
            "a string"
        _ 
            "something else"
    }

    {operator 😐 100         # custom operator with precedence level
        $left + $right + 1}
    {operator 😵 90
        $left - $right}
    a = 2 😵 3 😐 5
    a | print                 # -7
    {assert a == -7}
    b = 2 | {😐 3}           # 6

    # A macro that composes a sequence of functions
    {def macro pipe [ns]            # ns is a list of syntax nodes (AST nodes) inside the macro
        ns = {regular ns}       # built-in function to remove whitespace and comments nodes
        p = ns@0                # ns@0 is the first element of ns
        i = 1
        {while i < {len ns}     # while loop
            p = {quote {unquote p} | {unquote ns@i}}  # Lisp-style quote and unquote
            i = i + 1
        }
        p                       # return value
    }
    f = [x] -> x * 2                    # lambda function
    mul = [x y] -> x * y                # lambda function
    c = {pipe 3 f f {mul 10 _} f f}     # 480

Note:

* The syntax is determined by lists and binary expressions.
* Return values are implicit, i.e. the last expression in a block is the return value.

Other Features
^^^^^^^^^^^^^^

* Class definitions
* String interpolation
* Function composition
* Meta programming, including macros, custom operators and embedded mini-languages
* Python interoperability

TODOs, wishlist and ideas
^^^^^^^^^^^^^^^^^^^^^^^^^

* More built-in functions, operators, data types etc.
* Fix bugs
* Various missing Python features, such as decorators, yield and async/await
* Basic typing or type hints as in Python
* Pattern matching and destructuring
* More advanced typing, possibly with inference and unified with pattern matching and grammar expressions in some mini-language
* Better error messages and better IDE support
* More documentation and examples
* Compilers and code generators for other languages and platforms
* A composable query language for heterogeneous sources, such as databases, object structures, web services etc.
* Mini-languages for regular expressions and BNF
* An API for traversing and transforming MBF trees
* A templating language
* A website with tutorials, documentation and a playground
* Implementations in other languages


MRON
----

Main article: :doc:`mron`

Sample MRON document:

.. code-block:: makrell

    owner "Rena Holm"
    last_update "2023-11-30"

    books [
        {
            title  "That Time of the Year Again"
            year   1963
            author "Norton Max"
        }
        {
            title  "One for the Team"
            year   2024
            author "Felicia X"
        }
    ]

The above code corresponds to the following Python dictionary tree:

.. code-block:: makrell

    {
        "owner": "Rena Holm",
        "last_update": "2023-11-30",
        "books": [
            {
                "title": "That Time of the Year Again",
                "year": 1963,
                "author": "Norton Max"
            },
            {
                "title": "One for the Team",
                "year": 2024,
                "author": "Felicia X"
            }
        ]
    }

It's possible to embed MakrellPy code in MRON documents, and vice versa. Example:

.. code-block:: makrell

    a 2
    b {$ 3 + 5 }

This will be evaluated to this Python dictionary:

.. code-block:: makrell

    {
        "a": 2,
        "b": 8
    }

MRML
----

Main article: :doc:`mrml`

Sample MRML document:

.. code-block:: makrell

    {html
        {head
            {title A Test}
        }
        {body
            {h1 This is a Test}
            {p [style="color: red"] Just some {b bold} text here.}
        }
    }

The above code corresponds to the following HTML:

.. code-block:: html

    <!DOCTYPE html>
    <html>
        <head>
            <title>A Test</title>
        </head>
        <body>
            <h1>This is a Test</h1>
            <p style="color: red">Just some <b>bold</b> text here.</p>
        </body>
    </html>

It's possible to embed MakrellPy code in MRML documents, and vice versa. Example:

.. code-block:: makrell

    {a [b = {$ [2 3 5 7] | sum}] asd}

This will be evaluated to:

.. code-block:: html

    <a b="17">asd</a>


Makrell Base Format
-------------------

Main article: :doc:`base-format`

The Makrell Base Format is a simple data format that forms the basis for both MakrellPy, MRON and MRML. It is a simple text-based format that is easy to read and write. It is designed to be easy to parse and generate, and to be easy to work with in a text editor.

These element types are supported:

* **Identifier**: A simple name. Examples:
    * ``x``
    * ``Y1``
    * ``$Example_Æ23``.
* **String**: A sequence of characters surrounded by double quotes. The backslash character is used to escape double quotes and backslashes. A string may have a suffix that specifies an implementation-specific data type. Examples:
    * ``"Hi."``
    * ``"This is a string: \"Hi.\""``
    * ``"2024-02-02"date`` : a date
    * ``"12AF"hex`` : a hexadecimal number
* **Number**: A numeric value. As with strings, a number may have a suffix that specifies an implementation-specific data type or value. Examples:
    * ``42``
    * ``2.5e9``
    * ``2.5G`` = 2,500,000,000
    * ``2pi`` = 6.283185307179586
* **List**: A sequence of elements, surrounded by brackets and usually separated by spaces. Lists may be nested. There are three types of lists:
    * **"Round"**, e.g. ``(2 3 5)``
    * **"Square"**, e.g. ``["a" "b" "c"]``
    * **"Curly"**, e.g. ``{asd qwe zxc}``
* **Operator**: A symbol consisting of one or more non-alphanumeric characters. Examples:
    * ``+``
    * ``==``
    * ``|*``
    * ``<*>``

For parsing purposes, the following element types are also defined:

* **Whitespace**: A sequence of space, tab and newline characters.
* **Comment**: A sequence of characters that is ignored by the parser. A line comment starts with a `#` character and continues to the end of the line, while a block comment starts with `/*` and ends with `*/`.
* **Other Token**: A sequence of characters that does not match any of the other element types.

In addition, the following element type is defined in the core library:

* **Binary Expression**: An operator with two operands.

License
-------

Makrell is developed by Hans-Christian Holm and licensed under the MIT License.

Disclaimer
----------
The project is in an early stage of development and is not yet ready for production use.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting-started
   makrellpy/index
   mron
   mrml
   base-format


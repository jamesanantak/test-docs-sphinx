=====================
RST Elements Showcase
=====================

Basic Text Formatting
-------------------

This is a paragraph with *italic text* and **bold text**.
You can also have ``inline code`` or *italics* and **bold**.

Links can be `inline <https://example.com>`_ or referenced_.

.. _referenced: https://example.com

Lists
-----

Bullet Lists:

* First bullet
* Second bullet
    * Sub-bullet 1
    * Sub-bullet 2
* Third bullet

Numbered Lists:

1. First item
2. Second item
    a) Sub-item A
    b) Sub-item B
3. Third item

Definition Lists:

Term 1
    Definition of term 1
Term 2
    Definition of term 2

Code Blocks
----------

Simple code block using double colon::

    def hello_world():
        print("Hello, World!")
        return True

Code block with syntax highlighting:

.. code-block:: python
    :linenos:
    :emphasize-lines: 2

    def example_function():
        important_line = True
        return important_line

Tables
------

Simple Table:

=====  =====  ======
Input  Output  Notes
=====  =====  ======
A      B       Notes1
C      D       Notes2
=====  =====  ======

Grid Table:

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| cell 1     | cell 2     | cell 3    |
+------------+------------+-----------+
| cell 4     | cell 5     | cell 6    |
+------------+------------+-----------+

Admonitions
-----------

.. note::
   Thi
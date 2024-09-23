Styleguide for your docs
========================


.. code-block::

   # Documentation styleguide

   The purpose of the styleguide is to maintain a consistent and cohesive voice and appearance within the documentation.

   For any questions on specific style questions not addressed here, refer to the Microsoft style guide.

   ## Define language and styles

   For writing prose, we use American English.

   Documentation is written in reStructured Text.
   See `this guide <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
   for reStructured Text primer.

   Python docstrings follow the `NumPy style <https://numpydoc.readthedocs.io/en/latest/format.html>`_.

   Bibliographies follow the
   `APA style <https://apastyle.apa.org/style-grammar-guidelines/references/examples/journal-article-references>`_.

   ## Define specifics rules and expectations

   * When discussing the simulator in prose, NEST should always be written as all upper case, never as 'Nest'.
     When describing how to use the package (like ``import nest``), use  ``nest`` with all lower case in double back ticks.

   * Link to API functions when describing them in text.

     Syntax:

     :py:func:`.Connect`

   * Headings and subheadings should be descriptive and specify the topic.
     Titles like 'Introduction' or 'Part 1' are uniformative.
     Say 'How to do X' or use a verb in the present tense like 'Create you own network model'.

   * Do not write multiple extensive paragraphs. Break up long sections of text with examples,
     bullet lists, or images to make readability easier.

   * Do not use complex phrases or vocabularly if it is not specific to the subject matter.
     Use `plain language <https://www.plainlanguage.gov/about/definitions/>`_.






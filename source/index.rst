.. sample_project documentation master file, created by
   sphinx-quickstart on Fri Aug  9 11:29:26 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the RSE Documententation Page!
=========================================


Here you can find resources based on the RSE summer school workshop on Documentation.

Slide deck
----------

Here is a copy of the slides used during the workshop:

:download:`slides <../rse-summerschool.pdf>`

You can also find summary documents about

* :doc:`documentation organization and content <content_organization>`
* :doc:`documentation maintenance <documentation_maintenance>`
* :doc:`writing tutorials <tutorials>`


Documentation templates
-----------------------

* :doc:`README template <doc_templates/README_template>`
* :doc:`Style guide template<doc_templates/doc_styleguide_template>`
* :doc:`Contributor guidelines template <doc_templates/contributing_guidelines_template>`
* :doc:`Reviewer guidelines template <doc_templates/reviewer_guidelines_template>`
* :doc:`Documentation issue template <doc_templates/doc_issue_template>`

Tutorial-driven development
---------------------------

A method to develop new features with documentation as the driving force.

See :ref:`an example of how to use tutorial-driven development <ttd_example>`.

Documentation generators
------------------------

Turn plain text and code into discoverable, understandable, and clean output

-  `MkDocs <https://www.mkdocs.org/>`__

   -  plugins for Python, Javascript, Doxygen, etc `see
      list <https://github.com/mkdocs/catalog>`__

   -  compatible with Read the Docs

-  `Sphinx <https://www.sphinx-doc.org/>`__


   - **Python**, C++, C, Javascript

   - compatible with Read the Docs

-  `Doxygen <https://doxygen.nl/manual/index.html>`__

   -  **C++**, C, Python, PHP, Java, C#, Objective-C, Fortran, VHDL,
      Splice, IDL, and Lex

-  `Roxygen2 <https://roxygen2.r-lib.org/>`__

   -  **R**

-  `RMarkdown <https://rmarkdown.rstudio.com/>`__

   -  **R**, Python, Julia, C++, and SQL

-  `Quarto <https://quarto.org>`_
   
   - **R**, Python, Julia, Observable (JS


-  `FORD <https://forddocs.readthedocs.io/en/stable/>`__

   -  **Fortran**

-  `Documenter.jl <https://documenter.juliadocs.org/stable/man/guide/>`__

   -  **Julia**

-  `Swagger API <https://swagger.io/>`__

   -  Documeantion for OpenAPI or AsyncAPI specification


-  `And many more <https://jamstack.org/generators/>`_

Sample Sphinx project
~~~~~~~~~~~~~~~~~~~~~~

Go to this page to see some examples of various things you can do with Sphinx

:doc:`sample_sphinx`

A list of Sphinx extensions we have found useful:

:doc:`sphinx_ext_list`


Sample RMarkdown page using GitHub Pages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Here is an :ref:`example <rmarkdown_ghpage>` of using RMarkdown with GitHub pages.




Documentation hosting platforms
-------------------------------

-  `Read the Docs <https://docs.readthedocs.io/en/stable/tutorial/index.html>`__

-  `GitHub Pages <https://pages.github.com/>`__

-  `Gitlab Pages <https://docs.gitlab.com/ee/user/project/pages/>`__

Free for open source projects.

More interesting and useful documentation resources
---------------------------------------------------

-  `Write the docs <https://www.writethedocs.org/>`__

   -  a global community of people who care about documentation. Numerous
      articles and videos, a newsletter, conferences, and a Slack channel 
      with over 20,000 members!

-  A `curated list <https://github.com/testthedocs/awesome-docs>`__ of
   awesome documentation tools, guides, and good practice

-  `pandoc <https://pandoc.org/>`__ - a universal document converter

-  `Tables generator <https://www.tablesgenerator.com/>`__ - Generate
   tables in LaTeX, Markdown, HTML, MediaWiki, or text from a GUI

-  `nbgitpuller <https://hub.jupyter.org/nbgitpuller/link.html>`__ -
   Generate links to launch notebooks in a selected service (like
   JupyterHub and Binder)

-  `lychee <https://lychee.cli.rs/>`__ - Link checker for your docs





.. toctree::
   :maxdepth: 2
   :caption: Contents:






.. toctree::
   :hidden:
   :glob:

   content_organization
   documentation_maintenance
   tutorials
   doc_templates/*
   tutorial-driven-development_example
   sample_sphinx
   sphinx_ext_list
   RMarkdown_example

Contributing Guideline Template
===============================



.. code-block::

   # Contributor guidelines

   ## Start with a friendly greeting!

   >Thank you for considering contributing to <software>. It's people like you that make <software> such a great tool.

    ## Explain what kinds of contributions you are looking for.

    > <software> is an open source project and we love to receive contributions from our community!
    There are many ways to contribute, from writing tutorials or guides, improving the documentation,
    submitting bug reports and feature requests or writing code.


    ## Define expectations

    Tell users what you expect them to do. Tell them what you will do.
    Make sure to provide links to sources or references that might be helpful.

    1. Create your own fork of the code
    2. Do the changes in your fork (see below for code and documentation changes)
    3. If you like the change and think the project could use it:
        * Be sure you have followed the code style for the project.
        * Sign the Contributor License Agreement.
        * Submit a pull request.


    ### Documentation related changes

    If you are looking to improve or fix documentation, you need to be able to build
    the documentation locally to check that your changes work properly.

    * Create an environment

    * Install requirements for documentation build

       `pip install -r doc_requirements.txt`

    * Clone the <repository>

    * Create a new branch

      `git checkout -b <my-new-feature>`

    * Make your changes

    * build the documentation:

      `cd </docs/folder>`

      `sphinx-build . ../_build/html -b html`

    * Open ``_build/html/index.html`` in a browser and review your changes. Make sure links works and the
      formatting looks correct.

    ### Code related changes

    If you are looking to improve or fix code, see our guidelines for C++.




    ### Review process

    We will assign reviewers once the Pull request is made, and they will review it as soon as time allows.

    Check that all tests pass in the CI, if not a failing test may indicate something isn't right
    with your changes. You can look at the log output for each job. If you need help, ask a reviewer.


    Once reviewers are satisified with your changes, they will only approve your submission
    if there are no conflicts with the main branch and all checks have passed in our CI workflow.


    If you want to report a bug, suggest an improvement, or a feature request. Submit an issue using the issue templates
    provided.


Links to resources
------------------

* `A very detailed CONTRIBUTING template <https://github.com/nayafia/contributing-template/blob/master/CONTRIBUTING-template.md>`_
* `Example from Read the Docs <https://dev.readthedocs.io/en/latest/contribute.html>`_
* `Example from Write the Docs <https://www.writethedocs.org/guide/contributing/>`_




Sample Sphinx project page
==========================

This project showcases a few things you can do with Sphinx. 

* For the complete documentation see `the official Sphinx documentation <https://www.sphinx-doc.org/en/master/>`_.

* For some interesting extensions :doc:`see this list <ext_list>`.


Sphinx uses the concept of directives and roles to create the various formats and structure.
You can write your documents in either reStructured Text or Markdown.

Restructured Text syntax for directive and roles:

::

   .. directive_name::

        Text here

   Some text with :role_name:`text`

An image example
----------------


You can include figures and images. No extensions are needed.


**Syntax:**

::

   .. figure:: _static/sloth.jpg

      A baby sloth

**Output:**

.. figure:: _static/sloth.jpg

      A baby sloth

A math example
--------------


For math formulas, you can add the mathjax extension. In ``conf.py``, add ``"sphinx.ext.mathjax"`` to
your list of extensions.

Write your math formulas in LaTeX and mathjax will render the HTML output

**Syntax:**

::

    .. math::

      \frac{dV_\text{m}}{dt} = -\frac{V_{\text{m}} - E_\text{L}}{\tau_{\text{m}}} +  \\
      \frac{I_{\text{syn}} + I_\text{e}}{C_{\text{m}}}

**Output:**

.. math::

    \frac{dV_\text{m}}{dt} = -\frac{V_{\text{m}} - E_\text{L}}{\tau_{\text{m}}} +  \\
    \frac{I_{\text{syn}} + I_\text{e}}{C_{\text{m}}}



**Syntax:**

::

   Roles are use for inline markup like in the case of :math:`x >= 10`

**Output:**

Roles are use for inline markup like in the case of :math:`x >= 10`

An API example
--------------

If you have an API you would like to document you can use the `autodoc` and `autosummary`
extensions. In ``conf.py``, add ``"sphinx.ext.autodoc"`` or ``"sphinx.ext.autosummary"`` to your list
of extensions, along with the path to your Python files.

**Syntax:**

::

  .. automodule:: templating_example
      :members:

**Output:**


.. automodule:: templating_example
    :members:



Advanced
---------

A custom role and directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can create your own extensions in Sphinx.
Here is the code in ``_ext/helloworld.py`` for creating a `hello world`  custom directive and role.
See the Sphinx documentation for `extending Sphinx  <https://www.sphinx-doc.org/en/master/development/index.html>`_


.. literalinclude:: _ext/helloworld.py



**Syntax:**


::

  My custom greeting:

  .. hello:: world

  This can also be done as a role in line like so :hello:`my baby`.

**Output:**

My custom greeting:

.. hello:: world

This can also be done as a role in line like so :hello:`my baby`.

Jinja template in documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Say you have external dataset that you want to show in your documentation. We can use Jinja template syntax in our
docs with a little Python code to render the data. Sphinx uses Jinja templates internally so it is not an external dependency.
See this `blog post from Eric Holscher (developer at Read the Docs and Write the Docs)
<https://www.ericholscher.com/blog/2016/jul/25/integrating-jinja-rst-sphinx/>`_ for details.



We need a JSON formatted data set, and in this case we create a sample file in our ``_ext`` folder
called ``my_data.json``.


.. literalinclude:: _ext/my_data.json
    :language: JSON


We then need to write a script (``_ext/templating_example.py``). This script will connect the Jinja template provided
in the document with the dataset. The script is triggered at a specific event ``source-read`` during the Sphinx build process.

Make sure to add that script filename to our list of extensions in ``conf.py``. 
And ensure that the path to extensions is also in the ``conf.py``
(e.g., ``sys.path.append(os.path.abspath("./_ext")``).


.. literalinclude:: _ext/templating_example.py


In our document (``index.rst``), we need to use Jinja template syntax to generate the desired output.

We want to display a subselection of the data as lists. 
Jinja is similar to Python, but has some differences.
See the `Jinja templating documentation for details <https://jinja.palletsprojects.com/en/3.1.x/templates/>`_.



**Syntax:**


::

    {% raw %}
        {% for items in pet_data %}

        {% if items.pet == "dog" %}
        Show available  dog breeds:

        {% for item in items.breeds | sort %}
        * {{ item }}
        {% endfor %}

        {% endif %}

        {% if items.pet == "dinosaur" %}
        Show available dinosaur breeds:

        {% for item in items.breeds | sort %}
        * {{ item }}
        {% endfor %}

        {% endif %}

        {% endfor %}

    {% endraw %}

.. note::

   Note that the variable name "pet_data" must match the name given in ``html_context`` in the extension
   script (``templating_example.py``)

**Output:**


{% for items in pet_data %}

{% if items.pet == "dog" %}
Show available  dog breeds:

{% for item in items.breeds | sort %}
* {{ item }}
{% endfor %}

{% endif %}

{% if items.pet == "dinosaur" %}
Show available dinosaur breeds:

{% for item in items.breeds | sort %}
* {{ item }}
{% endfor %}

{% endif %}

{% endfor %}




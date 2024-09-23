.. _ttd_example:

An example workflow of tutorial-driven development
===================================================

Tutorial-driven development puts the focus on user needs rather than code implementation.
The tutorial is written first, then the code.

It is a rather new concept, and you can see a great use case from this `RSE talk <https://www.youtube.com/watch?v=XjpfgP2SPt8>`_
by Christopher Woods in 2022.

For more information on tutorials in general, see :doc:`tutorials`.

A tutorial is generally considered a step-by-step procedure that provides the reader with the necessary
information to complete a task successfully.

How would this development approach actually work?
--------------------------------------------------

This type of approach could be particularly useful for developing new features in software.
The focus shifts from how to implement the feature in code to how the user would use that feature.

The tutorial becomes the guide for how the code should be developed.

Let's take a look at an example workflow:

Request for new feature
~~~~~~~~~~~~~~~~~~~~~~~~

We will pretend that you have tool that takes built-in models, runs calculations on them, and plots output.
Someone requests a new feature: They want your tool to import models from an external database.

In tutorial-driven development, we have to first ask how would we ideally want to execute this feature.
How would a user want to accomplish the task?

Development steps
~~~~~~~~~~~~~~~~~~

You now need to approach this problem as if you are a user.


1.  Decide on tutorial format (should this be plain text with code snippets, Jupyter Notebook etc.)
2.  Start writing the tutorial:

    What is the goal of the tutorial?


       This tutorial will show  you how you can import data from an external database and compare results between built-in model and the imported model.

    What are the prerequisite before starting?

      You will need our tool installed as well as access to the external database.

3. Write the steps that would be *ideal* to accomplish the task. Here we are making very simple statements. But the real text should be expanded
   to provide sufficient detail that a new user would be able to understand what is happening at each step.

.. code-block:: python

   # Step 1 Load the built-in model from our tool
   x_model = load.model("x")

   # Step 2 Calculate equation
   result_x = calculate(x_model)

   # Step 3 Get the external model you want to compare
   y_model =  get_model("y")

   # Step 4 Calculate equations
   result_y = calculate(y_model)

   # Step 5 Compare x and y models
   compare_results =  compare(result_x,result_y)

   # Step 6 Show results
   plot(compare_results)


4. Once we have a decent tutorial laid out, we can then go through each of the steps and see how we can implement
   them in the code.

   Step 1 and Step 2 is something our tool can already do, so code does not need to change.


   Next we take a look at Step 3 importing "y"

   We start to evaluate how we will write code to accomplish this task.
   We determine that code for this step will require 3 functions:
   -  Fetch the model
   -  Move the model to the right location
   -  Convert model to the correct format

   As we develop the code for this step, we realize that we actually want the user to set the location 
   for the imported models.


   So we go back to our tutorial and modify the instructions:


.. code-block:: python

  # Step 3 provide a path to the model location

  my_models = "/path/to/models"

  # Step 4 Get the model from the specified location
  y_model =  get_model("y", my_models)


5. Continue to work through each step of the tutorial. As you create and modify code, you update the tutorial.


6. Once each step is completed in the code, you have functional code along with a functional tutorial, which you can 
   use to test if the code executes as expected!



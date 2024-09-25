Reviewer Guidelines Template
============================


  .. code-block::

     # Reviewer guidelines

     It is the responsibility of a reviewer to review and respond to comments in a timely fashion.
     If this is not possible, the reviewer should ask to be removed from the Pull request.

     For most PRs, we require 2 reviewers approval before merging, with passing CI tests.
     The two reviews have to cover the technical side (i.e., if the code does the right thing and
     is architecturally sound) and the content side (i.e., if the code is scientifically correct and
     fixes an actual issue).

     For larger and more complex PRs, more reviewers may be assigned
     to address different aspects of the changes.

     For documentation and minor changes, we generally require 1 reviewer.


     ## Reviewer feedback rules:


     1. Always try to dicuss feedback in a open and friendly manner.
     2. Use 'I' statements: Formulate messages from your point of view. Avoid 'you' statements as it can sound like an 
        attack on the person.
        Wrong: “You are writing cryptic code."
        Right: “It’s hard for me to grasp what’s going on in this code."
     3. Talk about the code not the coder.
     4. Say thanks!

     See more [tips here](https://phauer.com/2018/code-review-guidelines/#code-reviews-guidelines-for-the-reviewer).

     ## Checklist for reviewers:

     - Is this PR targeting the correct branch?
     - Is there an adequate description of the PR in the description box?
     - Has the PR been assigned to the correct project or milestone?
     - For code changes, does the affected code have corresponding tests?
     - Do the code changes adhere to conventions?
     - Are the changes documented correctly and adequately?
     - Are there major breaking changes? (Consider if a version bump is needed)
     - For documentation changes, does the documentation build correctly? Are the changes aligned with the code?


     BEFORE APPROVING:

     - Check that all tests pass in the CI pipeline.
     - Check that there are no conflicts with base branch.

     BEFORE MERGING:

     - Check that the title of the PR makes sense
     - If there are corresponding issues, make sure they are linked
     - Check that the PR is correctly labeled
     - Ensure that all comments and questions are resolved
     - Check that the correct number of reviewers have approved

Links to resources
-------------------

* `An example from GitLab <https://egghead.io/lessons/javascript-introduction-to-github>`_
* `Code review guidelines for humans  <https://phauer.com/2018/code-review-guidelines/#code-reviews-guidelines-for-the-reviewer>`_



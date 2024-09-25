How to create sustainable documentation
=======================================

General recommendations
-----------------------

-  Use a single source of truth (do not duplicate content!). Small
   chunks of content can be repeated in different places if necessary,
   but source documents, code, and code comments should not have
   multiple copies that can diverge if not all is kept up-to-date.

-  Use scripts and automation to extract and modify content.

-  Make sure documentation (both technical and user facing) are part of
   the project development plans and workflows!

Docs as Code
------------

A philosophy that you should be writing documentation with the same
tools as code:

-  Docs in the same repo as code

-  Use issue trackers for documentation

-  Version Control (Git)

-  Plain Text Markup (Markdown, reStructuredText, Asciidoc etc.)

-  Add documentation to review process

-  Automated tests for docs

Create-Manage-Deploy: DocOps
----------------------------

Generally speaking, “DocOps” is like
`DevOps <https://www.atlassian.com/devops>`__. Instead of applying
broadly to software development, DocOps specifically applies to the
creation, management, and release of documentation. A set of practices
that works to automate and integrate the process of developing
documentation. It is the application of `docs as code` in a workflow.

In principle, the goal is to make documentation available and
discoverable.

You can use static site generators (SSGs) to convert plain text markup
(such as markdown or reStructured Text) as well as scripts into
HTML/PDF output.

SSGs have configuration files that allow you to add extensions, alter
themes, etc.

Platforms for hosting docs, take care of the build and can be set to
build at every new Pull(merge) request.

You can have development branches to work and test new features and fix
documentation issues.

You can set up tests that trigger at every new pull request (check for
broken links, language linting, successful build).

Tasks
~~~~~

Tasks involved in setting up and maintaining documentation with DocOps
and Docs as Code concepts

-  Reviewing, assigning, and taking care of issues related to
   documentation

-  Selecting and managing tools used to produce
   documentation – markup language, static site generator (SSG), hosting
   provider, etc.

-  Defining processes and established ways of working, including where
   docs fit into development methodologies.
   (For example, setting up a project tracker for documentation; defining rules
   on review processes for documentation changes).

-  Helping developers/users contribute to docs

-  Managing content (creation of content but also ensure the content is discoverable)

-  Building and maintaining a theme for an SSG

-  Implementing software versioning strategies as they pertain to
   documentation

-  Creating and maintaining build scripts

-  Developing testing solutions and setting up CI/CD pipelines for
   documentation

-  Assessing pre-existing documentation and getting feedback for content improvement

A Write the Docs collection of practical tips
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From `Write the Docs <https://www.writethedocs.org/>`__ community
discussion: summary of key points make documentation maintenance easier

-  Implement well-structured information architecture

-  Automate as much as possible, especially in areas of rapid change, >
   and make sure that automation scripts are easy to maintain >
   *Examples: code includes, API reference docs, screenshots*

-  Make it easy to find and update groups of related topics

-  Create and promote a lightweight style guide

-  Stick to an `“Every page is page >
   one” <http://everypageispageone.com/>`__ approach

-  Use templates to make writing new content easier for new and >
   returning contributors

-  Set up doc sprints (onsite or remote) to help focus groups on a >
   predefined set of docs issues

-  Set up continuous integration/continuous deployment on doc builds to
   > promote an agile attitude toward doc contributions and fixe- Make
   the process for contributing as simple as possible

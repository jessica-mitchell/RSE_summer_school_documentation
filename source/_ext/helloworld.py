from __future__ import annotations

from docutils import nodes

from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective, SphinxRole
from sphinx.util.typing import ExtensionMetadata


class HelloRole(SphinxRole):
    """
    A custom Sphinx role that outputs a greeting.

    This class extends the SphinxRole class, which defines custom roles for Sphinx.
    The main logic is implemented in the `run` method, which returns a tuple consisting of:
    - A list of inline-level docutils nodes that represent the processed content.
    - An optional list of system messages, which are typically used for warnings or errors.

    Returns:
        tuple: A tuple containing:
            - list[nodes.Node]: A list of nodes to be processed, representing the inline content.
            - list[nodes.system_message]: An optional list of system messages.
    """

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        node = nodes.inline(text=f"Hello {self.text}!")
        return [node], []


class HelloDirective(SphinxDirective):
    """
    A custom Sphinx directive that outputs a greeting.

    This class extends the SphinxDirective class and defines a custom directive that
    generates a paragraph node with a greeting message.

    Attributes:
        required_arguments (int): Specifies the number of arguments the directive requires.

    The main logic is implemented in the `run` method, which returns a list of block-level
    docutils nodes that represent the processed content.

    Returns:
        list: A list of nodes to be processed, representing the block content.
    """

    required_arguments = 1

    def run(self) -> list[nodes.Node]:
        paragraph_node = nodes.paragraph(text=f"hello {self.arguments[0]}!")
        return [paragraph_node]


def setup(app: Sphinx) -> ExtensionMetadata:
    """
    Set up the custom Sphinx extension by adding the new role and directive.

    This function registers the custom role and directive with the Sphinx application,
    allowing them to be used within Sphinx documents. This function is a requirement
    for any Sphinx extension.

    Args:
        app (Sphinx): The Sphinx application object.

    Returns:
        ExtensionMetadata: Metadata about the extension, including version and parallel safety.
    """
    app.add_role("hello", HelloRole())
    app.add_directive("hello", HelloDirective)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


from pathlib import Path
import json

def template_renderer(app, docname, source):
    """
    Renders a Sphinx documentation page using a Jinja template with custom data.

    This function is connected to the Sphinx `source-read` event and modifies the
    source content of a documentation page before it is rendered. It loads data
    from a JSON file and injects it into the context of the Jinja template, allowing
    for dynamic content generation.

    Parameters:
    app (Sphinx): The Sphinx application object.
    docname (str): The name of the document currently being processed.
    source (list): A list containing the source of the document as a single string.

    Returns:
    None
    """
    if app.builder.format != "html":
        return

    with open(Path(__file__).parent / "my_data.json") as file:
        my_data = json.load(file)

    if docname == "sample_sphinx":
        # Render the specified page using the Jinja template with custom data
        html_context = {"pet_data": my_data}
        src = source[0]
        rendered = app.builder.templates.render_string(src, html_context)
        source[0] = rendered

def setup(app):
    """
    Sets up the Sphinx extension by connecting the `template_renderer` function
    to the `source-read` event.

    Parameters:
    app (Sphinx): The Sphinx application object.

    Returns:
    dict: A dictionary containing the version and parallel processing information for the Sphinx extension.
    """
    app.connect("source-read", template_renderer)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


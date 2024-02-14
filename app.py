from flask import Flask, render_template, render_template_string
import folium


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello world", test="Hello")

@app.route("/test")
def test():
    return render_template("index.html", title="Hello world", test="Hello Test")

@app.route("/iframe")
def iframe():
    """Embed a map as an iframe on a page."""
    m = folium.Map(location=[28.116667, -17.216667])

    # set the iframe width and height
    m.get_root().width = "800px"
    m.get_root().height = "600px"
    iframe = m.get_root()._repr_html_()

    return render_template_string(
        """
            <!DOCTYPE html>
            <html>
                <head></head>
                <body>
                    <h1>Using an iframe</h1>
                    {{ iframe_content|safe }}
                </body>
            </html>
        """,
        iframe_content=iframe,
    )
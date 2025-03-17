import os
from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route("/")
def serve_index():
    # Read the HTML file
    with open("static/index.html", "r") as file:
        html_content = file.read()

    # Replace placeholder with environment variable
    api_host = os.environ.get("API_HOST", "http://localhost:8080")
    modified_html = html_content.replace("{{API_HOST}}", api_host)

    return modified_html


@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory("static", path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

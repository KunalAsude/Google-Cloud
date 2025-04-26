from flask import Flask
from typing import Any

# Create the Flask app
app = Flask(__name__)

@app.route("/")
def hello() -> str:
    """
    Return a friendly HTTP greeting.

    Returns:
        A simple greeting string.
    """
    return "👋 Hello, World! Welcome to Google App Engine 🚀"

def main() -> Any:
    """Run the app locally."""
    app.run(host="127.0.0.1", port=8080, debug=True)

if __name__ == "__main__":
    main()

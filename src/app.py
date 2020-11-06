import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(os.environ.get("APP_CONFIG"))


@app.route("/")
@app.route("/search")
def search():
    return render_template(
        template_name_or_list="search.html",
        title="High Score - Best Music Score Seach Engine",
    )


"""
@app.route("/favicon.ico")
def favicon():
    pass
    return send_from_directory(
        os.path.join(app.root_path, "static"), "favicon.ico", mimetype="image/vnd.microsoft.icon"
    )
"""

if __name__ == "__main__":
    app.run()

import json
import os
import subprocess

from flask import Flask, render_template, request
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


@app.route("/results", methods=["POST"])
def results():
    song = request.form.get("song")
    subprocess.check_output(["scrapy", "crawl", "musescore", "-a", f"song='{song}'"])

    with open("highscore/result.json") as file:
        data = json.load(file)

    return render_template(
        template_name_or_list="results.html",
        title="High Score - Best Music Score Seach Engine",
        data=data,
    )


if __name__ == "__main__":
    app.run()

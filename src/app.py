import json
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


@app.route("/results")
def results():

    # This is for developers purposes only!
    # real app will scrap sites at real time!
    # with open("src/result.json", "r") as file:
    #     data = json.load(file)

    return render_template(
        template_name_or_list="results.html",
        title="High Score - Best Music Score Seach Engine",
        # data=data,
    )


if __name__ == "__main__":
    app.run()

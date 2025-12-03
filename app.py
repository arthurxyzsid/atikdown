from flask import Flask, render_template, request
import requests
import datetime

app = Flask(__name__)

API = "https://tikwm.com/api/"

def format_date(ts):
    try:
        return datetime.datetime.fromtimestamp(ts).strftime("%d %B %Y")
    except:
        return "-"

@app.route("/", methods=["GET", "POST"])
def index():
    video = None
    error = None

    if request.method == "POST":
        url = request.form.get("url")

        try:
            r = requests.post(
                API,
                data={"url": url},
                headers={"User-Agent": "Mozilla/5.0"}
            ).json()

            if r["code"] != 0:
                error = "Link tidak valid."
            else:
                d = r["data"]
                video = {
                    "cover": d["cover"],
                    "caption": d["title"],
                    "author": d["author"]["unique_id"],
                    "date": format_date(d["create_time"]),
                    "video": d["play"],
                    "video_hd": d.get("hdplay"),
                    "audio": d["music"],
                }

        except:
            error = "Server error."

    return render_template("index.html", video=video, error=error)

app.run(host="0.0.0.0", port=5000, debug=True)
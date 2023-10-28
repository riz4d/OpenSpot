from flask import Flask,render_template,request,redirect
from modules.core import playlist_dl,play_fetch
import os
app = Flask("__main__",template_folder="templates",static_folder="static")

@app.route("/fetch",methods=["POST","GET"])
def fetch():
    req_id = request.cookies.get("csrftoken")
    playlist_url = request.form.get("playlist")
    playlist_id = playlist_url.split("/")[-1]
    playlist_fetched = play_fetch(playlist_id=playlist_id)
    print(playlist_fetched)
    play_data = {"status":"True","playlist_url":playlist_url,"playlist_name":playlist_fetched[0],"Owner":playlist_fetched[1],"total":playlist_fetched[2]}
    return render_template("index.html",context=play_data)
@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        try:
            print(request.cookies.get("csrftoken"))
            req_id = request.cookies.get("csrftoken")
            playlist_url = request.form.get("playlist")
            playlist_id = playlist_url.split("/")[-1]
            play_link=playlist_dl(playlist_id=playlist_id,req_id=req_id)
            try:
                os.remove(play_link[1])
            except OSError as e:
                print(f"Error deleting file: {e}")
            return redirect(play_link[0])
        except Exception as e:
            print(e)
    data = {"status":"False"}
    return render_template("index.html",context = data)

app.run(host="0.0.0.0",port=int(os.getenv('PORT', 80)),use_reloader=True, threaded=True,debug=False)

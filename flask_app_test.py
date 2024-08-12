# Flask網站前後端互動 09 - 超連結與圖片
# 載入Flask、Request、render_template
from flask import Flask, request, render_template

# 建立 Application 物件,設定靜態檔案的路徑處理
# http://127.0.0.1:5000/head.png 為圖片路徑
# app = Flask(__name__, static_folder="public", static_url_path="/")
app = Flask(__name__, template_folder='template')
# 處理路徑 / 的對應函市


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/page")
def page():
    name = request.args.get("nameis")
    return render_template("page.html", namepage=name)


# 啟動Server
app.run()
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='./html')


@app.route("/")
def page_main():
    return render_template("page_main.html")

@app.route("/page_Learn_German")
def page_Learn_German():
    return render_template("page_Learn_German.html")

# @app.route("/page")
# def page():
#     name = request.args.get("nameis")
#     return render_template("page.html", namepage=name)

# @app.route("/page_run_python_scripts")
# def page_run_python_scripts():
#     return render_template("page_run_python_scripts.html")

# 啟動Server
app.run()
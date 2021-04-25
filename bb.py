from flask import Flask, render_template, redirect, request, url_for

web_server = Flask(__name__)


@web_server.route("/", methods=['GET'])
def home():
    return render_template('home page.html')


if __name__ == '__main__':
    web_server.env = "development"
    web_server.debug = True
    web_server.run(host="127.0.0.1", port=5000)

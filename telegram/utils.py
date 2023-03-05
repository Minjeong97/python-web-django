
# pip install flask
from flask import Flask  # [Ctrl] 누르고 'Flask' 누르면 실제 우리가 다운 받은 것들이 나옴.

app = Flask()  # class: 대문자 F로 시작함.

@app.route("/")  # @:  데코레이터
def home():
    return 'Hello Server!'

@app.route("/hi")  # @:  데코레이터
def hi():
    return 'hi'

app.run(port=80, debug=True)

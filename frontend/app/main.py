from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def pagecreate():
  time = "Hammer Time?!"
  return render_template('index.html', time=time)

if __name__ == "__main__":
  app.run(debug=False, host='0.0.0.0')

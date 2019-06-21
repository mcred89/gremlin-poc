from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def pagecreate():
  request_ip = request.remote_addr
  dashed_ip = request_ip.replace(".", "-")
  time = "Hammer Time?!"
  return render_template('index.html', time=time)

if __name__ == "__main__":
  app.run(debug=False, host='0.0.0.0')

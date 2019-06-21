from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def pagecreate():
  request_ip = request.remote_addr
  dashed_ip = request_ip.replace(".", "-")
  try:
    r = requests.get(f'ip-by-geo.themcilroy.com/{dashed_ip}', timeout=0.01)
    response = r.json()
    time = str(response['time'])
  except Exception as e:
    time = "Hammer Time?!"
  return render_template('index.html', time=time)

if __name__ == "__main__":
  app.run(debug=False, host='0.0.0.0')

from flask import Flask,render_template
import socket

app = Flask(__name__)

@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        response = requests.get('https://ipinfo.io')
        data = response.json()
        country_code = data.get('country', 'Unknown') 
        return render_template('index.html', hostname=host_name, ip=host_ip, country_code=country_code )
    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

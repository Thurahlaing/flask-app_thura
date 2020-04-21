from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://blog.commlabindia.com/wp-content/uploads/2019/07/animated-gifs-corporate-training.gif",
    "https://1.bp.blogspot.com/-B7Lq6M7mi2g/VW2k4qqKh_I/AAAAAAAAAQs/coblzE1xKhI/s1600/336a28215c215237ff39636e06e035cb.gif"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
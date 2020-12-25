# encoding:utf-8
# @TIME:  2020/12/21  21:57 

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('grid_geo_bar.html')
    # return 'hello world'


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)

    # new branch1

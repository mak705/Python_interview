from flask import Flask, render_template
from flask import  request

app = Flask(__name__)


#http://127.0.0.1:5000/showRandArticle?lang=tel
@app.route('/showRandArticle', methods=['GET', 'POST'])
def getByLangAndRandId():

    language = request.args.get('lang')
    return render_template('index.html')

if __name__ == "__main__":
    app.run('0.0.0.0')


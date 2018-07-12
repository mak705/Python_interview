from flask import Flask
from flask import  request
app = Flask(__name__)

@app.route('/showRandArticle', methods=['GET', 'POST'])
def getByLangAndRandId():

    language = request.args.get('lang')
    return 'Hello ' + language + ' usr'

if __name__ == "__main__":
    app.run()

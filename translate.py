from os import error
from flask import Flask, render_template, request, url_for, redirect
from flask_googletrans import translator

app = Flask(__name__)

ts = translator(app)




@app.route('/', methods=["POST", "GET"])
def home():
    if request.method=="POST":
        try:
            text = request.form["area"]
        
            textb = request.form["them"]
            textc = request.form["them1"]
            return redirect(url_for("text", txt = text, sct = textb, sct1 = textc))

        except Exception as e:
            return render_template('error.html', e=e)



    else:
        return render_template('home.html')



@app.route('/<txt>/<sct>/<sct1>')
def text(txt, sct, sct1):
    return render_template('trans.html', text = txt, textb = sct, textc = sct1)




if __name__=='__main__':
    app.run(debug=True)
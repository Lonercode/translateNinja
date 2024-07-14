import os
from os import error
from flask import Flask, render_template, request, url_for, redirect, send_file
from flask_googletrans import translator
import gtts.lang
from playsound import playsound
import time
from gtts import gTTS
import gtts



app = Flask(__name__)

ts = translator(app)


@app.route('/manifest.json')
def serve_manifest():
    return send_file('manifest.json', mimetype='application/manifest+json')


@app.route('/sw.js')
def serve_sw():
    return send_file('sw.js', mimetype='application/javascript')

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
    if sct1 in gtts.lang.tts_langs().keys():
        aud = gTTS(text=ts.translate(text=txt, src=sct, dest=[sct1]), lang=sct1)
        aud.save('./static/translated.mp3')
    else:
        ts.translate(text=txt, src=sct, dest=[sct1])
        aud = gTTS(text = "I am sorry, but there is no audio for this language", lang = 'en')
        aud.save('./static/translated.mp3')
    return render_template('trans.html', text = txt, textb = sct, textc = sct1)




if __name__=='__main__':
    app.run(debug=True)
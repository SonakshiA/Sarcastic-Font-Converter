import os
from flask import Flask, render_template, request;
from main import convertAlternateCharacters, convertRandomCharacters

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/submit",methods=["POST"])
def get_data():
    string_input = request.form['input']
    print(string_input)
    output_string_alternate = convertAlternateCharacters(string_input)
    print(output_string_alternate)
    output_string_random = convertRandomCharacters(string_input)
    print(output_string_random)
    return render_template('index.html',output_alternate=output_string_alternate,output_random=output_string_random)


if __name__=='__main__':
    app.run()

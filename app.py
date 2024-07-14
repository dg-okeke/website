from flask import Flask, render_template
from helper import program, descriptions, details

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/info/<int:id>")
def info(id):
    return render_template(
            'info.html',
            template_program=program[id],
            template_description=descriptions[id],
            template_detail=details[id]
        )


if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template
app = Flask(__name__, static_url_path='', static_folder='web/templates', template_folder='web/templates')

@app.route('/')
def index():
   return render_template("table1.html")

if __name__ == '__main__':
   app.run(debug = True)
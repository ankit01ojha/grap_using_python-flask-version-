import json
import flask

from flask import Flask
app = Flask(__name__)
 
@app.route("/bar")
def home():
#code for making chart
	with open('bar.json','r') as bar_file:
    		data = json.load(bar_file)
	chart = pygal.Bar()
    	mark_list = [x['mark'] for x in data]
    	chart.add('Annual Mark List',mark_list)
    	chart.x_labels = [x['year'] for x in data]
    	chart.render_to_file('static/images/bar_chart.svg')
    	img_url = 'static/images/bar_chart.svg?cache=' + str(time.time())
    	return render_template('chart.html',image_url = img_url)
    
 
if __name__ == "__main__":
    app.run()


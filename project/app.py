from flask import Flask, jsonify, render_template, request
import requests
import json

app = Flask(__name__)
app.config['DEBUG'] = True #disable me in deployment


@app.route('/')
def hello():
	return render_template("hello.html")

@app.route('/search', methods=["GET", "POST"])
def search():
	if request.method == "POST":
		url = "https://api.github.com/search/repositories?q=" + request.form["user_search"]
		response_dict = requests.get(url).json()
		parsed_dict = parse_response(response_dict)
		return render_template("results.html", api_data=response_dict)
	else:
		return render_template("search.html")

@app.route('/test')
def test():
	return render_template("test.html")

def parse_response(response_dict):
	parsed = dict()
	parsed['total_count'] = response_dict['total_count']
	parsed['items'] = []
	for d in response_dict['items']:
		entry = parse_entry(d)
		parsed['items'].append(entry)
	return parsed

def parse_entry(entry_dict):
	entry = dict()
	entry['name'] = entry_dict['name']
	entry['html_url'] = entry_dict['html_url']
	entry['description'] = entry_dict['description']
	entry_owner = dict()
	owner = entry_dict['owner']
	entry_owner['login'] = owner['login']
	entry_owner['avatar_url'] = owner['avatar_url']
	entry_owner['html_url'] = owner['html_url']
	entry['owner'] = entry_owner
	return entry

@app.route('/search/exception')
def exception():
	return "Gotcha!"

@app.route('/add/<x>/<y>')
def add(x,y):
	return str(int(x)+int(y))

@app.errorhandler(404)
def not_found(error):
	return "Sorry, I haven't coded that yet, I'll get back to yaaa", 404

@app.errorhandler(500)
def internal_server_error(error):
	return "My code broke, my bad", 500

if __name__ == '__main__':
	app.run(host='0.0.0.0')

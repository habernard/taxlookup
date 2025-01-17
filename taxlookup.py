from flask import Flask, render_template, request, escape
from taxbracket import tax

app = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
	with open('taxbracket.log', 'a') as log:
		print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

@app.route('/mytax' , methods= ['POST'])
def do_search() -> 'html':
    income = request.form['income']
    title = 'Here is the amount you owe:'
    results = tax(income)
    log_request(request, results)
    return render_template('results.html',
    						the_income = income,
    						the_title = title,
    						the_results = results,)

@app.route('/')
@app.route('/entry')
def entry_page()-> 'html':
    return render_template('entry.html', the_title = 'Welcome to the official tax calculator on the web!')

@app.route('/viewlog')
def view_the_log() -> 'html':
	contents = []
	with open('taxbracket.log') as log:
		for line in log:
			contents.append([])
			for item in line.split('|'):
				contents[-1].append(escape(item))
	titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
	return render_template('viewlog.html',
							the_title='View log',
							the_row_titles=titles,
							the_data=contents,)

if __name__ == '__main__':
	app.run(debug=True)
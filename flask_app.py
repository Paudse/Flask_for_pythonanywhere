from flask import Flask
import Learn_German
app = Flask(__name__)

@app.route('/')
def hello_world():
	testing = 1
	while testing:
		test(foler_file_name)
		testing = input('Enter 1 for testing again: ')
	return 'Enter 1 for testing again: '

if __name__=="__main__":
	app.run()
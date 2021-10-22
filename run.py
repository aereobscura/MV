from morseview import create_app

app = create_app()

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")
	#host="0.0.0.0" for global access

# PythonWeb


Home page contains 3 buttons About Us contact Us and Calculator

Calculator calculates the numbers which are entered by the user as according to the opertor selected by him
------------------------------------------------------------------------------------------------------------------
app = Flask(__name__)
Flask is the main class from the Flask module.

__name__ is a special Python variable that holds the name of the current file/module.

When you pass __name__ to Flask, it tells Flask:

“Hey, this file is the starting point of the application.”
This helps Flask know where to:

Look for HTML templates (templates/)

Load static files (like CSS/JS)

Handle routing properly
🧠 Example:
If your file is called app.py, then __name__ will be "__main__" when you run it directly.
if __name__ == "__main__":
    app.run(debug=True)
This ensures the Flask server runs only when you execute the script directly

If someone imports your Flask file as a module in another script, it won’t auto-run


-----------------------------------------------------------------------------------------------------
🔥 app.run(debug=True):
Starts the Flask development web server

debug=True:

Enables auto-reload on code change

Shows detailed error messages
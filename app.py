from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("Success!")
        if "file" not in request.files: # Checks if there is a file, if not it redirects back to the homepage
            return redirect(request.url)

        file = request.files["file"]
        
        if file.filename == "": # Checks to make sure the file has a name, if not it redirects back to the homepage
            return redirect(request.url)

        if file: # If file is valid, we analyze it with speech recogniztion and have the transcript
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as sourceFile:
                data = recognizer.record(sourceFile)
            transcript = recognizer.recognize_google(data, key = None)

    return render_template('index.html', transcript = transcript)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)

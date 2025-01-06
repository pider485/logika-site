from flask import Flask, render_template, request, flash

from db_scripts import DatabaseManager
db = DatabaseManager("blog.db")

app = Flask(__name__) # Створюємо веб–додаток Flask

@app.route("/") # Вказуємо url-адресу для виклику функції
def index():
    image = db.get_image()
    return render_template("start.html", image=image)




if __name__ == "__main__":
    app.run(debug=True) # Запускаємо веб-сервер з цього файлу
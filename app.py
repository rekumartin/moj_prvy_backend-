from flask import Flask, jsonify

app = Flask(__name__)

# Databaza studentov
students = [
    {
        "id": 1,
        "name": "Adam Novák",
        "age": 20,
        "grade": "A",
        "image": "https://i.pravatar.cc/150?img=1"
    },
    {
        "id": 2,
        "name": "Barbora Kováčová",
        "age": 21,
        "grade": "B",
        "image": "https://i.pravatar.cc/150?img=2"
    },
    {
        "id": 3,
        "name": "Cyril Horváth",
        "age": 19,
        "grade": "A",
        "image": "https://i.pravatar.cc/150?img=3"
    },
    {
        "id": 4,
        "name": "Dana Slobodová",
        "age": 22,
        "grade": "C",
        "image": "https://i.pravatar.cc/150?img=4"
    },
    {
        "id": 5,
        "name": "Erik Blaho",
        "age": 20,
        "grade": "B",
        "image": "https://i.pravatar.cc/150?img=5"
    },
    {
        "id": 6,
        "name": "Filip Mináč",
        "age": 21,
        "grade": "A",
        "image": "https://i.pravatar.cc/150?img=6"
    },
    {
        "id": 7,
        "name": "Gabriela Lukáčová",
        "age": 19,
        "grade": "B",
        "image": "https://i.pravatar.cc/150?img=7"
    },
    {
        "id": 8,
        "name": "Henrich Polák",
        "age": 23,
        "grade": "C",
        "image": "https://i.pravatar.cc/150?img=8"
    },
    {
        "id": 9,
        "name": "Ivana Šimková",
        "age": 20,
        "grade": "A",
        "image": "https://i.pravatar.cc/150?img=9"
    },
    {
        "id": 10,
        "name": "Jakub Varga",
        "age": 21,
        "grade": "B",
        "image": "https://i.pravatar.cc/150?img=10"
    }
]


# Route 1: Privítanie
@app.route("/")
def index():
    return "<h1>Vitaj v mojom prvom Flask API!</h1><p>Použi <a href='/api'>/api</a> pre zoznam študentov.</p>"


# Route 2: Všetci študenti
@app.route("/api")
def get_students():
    return jsonify(students)


# Route 3: Jeden študent podľa ID
@app.route("/api/student/<int:student_id>")
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if student:
        return jsonify(student)
    return jsonify({"error": "Študent nenájdený"}), 404


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos simulados de jugadores
players = [
    {
        "name": "Roger Federer",
        "imageName": "federer2",
        "pais": "Switzerland",
        "paisimagen": "suiza",
        "link": "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDRqaGd0b3VibjNrMjRrb2J5NndsOXh2NjltaDJlbmRpOGNsZ292cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DOe8bDbHs41tbxUhpp/giphy.gif"
    },
    {
        "name": "Jannik Sinner",
        "imageName": "sinner2",
        "pais": "Italy",
        "paisimagen": "italia",
        "link": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHg1eHprcGxibXRtbXY3ejlhMnFzcGtydGRqNTBrNWVoNG1xNmlscyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/oxMitSE7cDXM2gL3Ss/giphy.gif"
    },
    {
        "name": "Rafael Nadal",
        "imageName": "nadal",
        "pais": "Spain",
        "paisimagen": "españa",
        "link": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzV3ejN5cGNrODh5eXplZXhpY3gyYmU3Mng4cjgyeXl4c3Vrd2ZkZSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/klyJ5gEdJT9L05Zecr/giphy.gif"
    },
    {
        "name": "Juan Martín del Potro",
        "imageName": "delpotro",
        "pais": "Argentina",
        "paisimagen": "argentina",
        "link": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGYzeTJzYzVwbThvcWgwY2phYjd4ZWF2Z3Vhb3NoaXBlZTdwa3U2ZyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3ov9jTSQJQpsmfBBg4/giphy.gif"
    },
    {
        "name": "Carlos Alcaraz",
        "imageName": "alcaraz",
        "pais": "Spain",
        "paisimagen": "españa",
        "link": "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeG5vcW51eDNqdjJjMW9pZm00aDQzdDdudHpoYzk1YnJnbjByYXk3MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4KcwWO1jN5hXqlDKm7/giphy.gif"
    }
]

@app.route("/", methods=["GET"])
def index():
        who = request.args.get("who", "world")
        return jsonify({"message": f"it works, {who}!"})

@app.route("/players", methods=["GET"])
def get_players():
    return jsonify(players)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

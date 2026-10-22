from flask import Blueprint, render_template, abort, request, flash

bp = Blueprint("main", __name__)


# Datos de demostración para el Checkpoint 1 (todavía no vienen de la base de datos)

MOVIES = {
    1: {
        "id": 1,
        "title": "The Love Hypothesis",
        "genre": "Romance / Comedy",
        "duration": 118,
        "age_rating": "+12",
        "synopsis": "When a fake-dating experiment between two scientists turns into unexpected real feelings, chaos and romance collide in the academia lab.",
        "poster": "/static/posters/love_hypothesis.jpg",
    },
    2: {
        "id": 2,
        "title": "La Bola Negra",
        "genre": "Mystery / Psychological Thriller",
        "duration": 105,
        "age_rating": "+16",
        "synopsis": "An enigmatic black sphere appears unexpectedly, unraveling secrets, hidden desires, and paranoia within an isolated community.",
        "poster": "/static/posters/la_bola_negra.jpg",
    },
    3: {
        "id": 3,
        "title": "Barbie in A Mermaid Tale",
        "genre": "Animation / Family / Adventure",
        "duration": 75,
        "age_rating": "All",
        "synopsis": "Merliah, a surfing champion from Malibu, discovers an astonishing family secret: she is actually a mermaid destined to save Oceana.",
        "poster": "/static/posters/barbie.jpg",
    },
}

SHOWTIMES = {
    101: {"id": 101, "movie_id": 1, "time": "16:30", "screen": "Screen 1 (Standard)", "price": 8.00},
    102: {"id": 102, "movie_id": 1, "time": "19:15", "screen": "Screen 2 (VIP)", "price": 10.50},
    103: {"id": 103, "movie_id": 1, "time": "21:45", "screen": "Screen 1 (Standard)", "price": 8.00},
    201: {"id": 201, "movie_id": 2, "time": "18:00", "screen": "Screen 1 (Standard)", "price": 8.00},
    202: {"id": 202, "movie_id": 2, "time": "20:30", "screen": "Screen 2 (VIP)", "price": 10.50},
    203: {"id": 203, "movie_id": 2, "time": "22:50", "screen": "Screen 1 (Standard)", "price": 8.00},
    301: {"id": 301, "movie_id": 3, "time": "16:00", "screen": "Screen 3 (Standard)", "price": 8.00},
    302: {"id": 302, "movie_id": 3, "time": "17:45", "screen": "Screen 3 (Standard)", "price": 8.00},
}


def showtimes_for(movie_id):
    """Devuelve la lista de sesiones de una película."""
    return [st for st in SHOWTIMES.values() if st["movie_id"] == movie_id]


@bp.route("/")
def index():
    movies = []
    for movie in MOVIES.values():
        movies.append({**movie, "showtimes": showtimes_for(movie["id"])})
    return render_template("main/index.html", movies=movies)


@bp.route("/movie/<int:movie_id>")
def movie_detail(movie_id):
    movie = MOVIES.get(movie_id)
    if movie is None:
        abort(404)
    return render_template(
        "main/movie_detail.html",
        movie=movie,
        showtimes=showtimes_for(movie_id),
    )


# Páginas de inicio de sesión y registro (solo diseño para el Checkpoint 1:
# todavía no guardan ni comprueban nada en la base de datos)

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        flash("Log in is not available yet (coming in the next checkpoint).")
    return render_template("auth/login.html")


@bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        flash("Sign up is not available yet (coming in the next checkpoint).")
    return render_template("auth/signup.html")


import datetime
from flask import Blueprint, render_template, abort, request, flash
 
from . import model
 
bp = Blueprint("main", __name__)
 
 
 
def demo_movies():
    # screens
    screen1 = model.Screen(id=1, name="Screen 1", capacity=96)
    screen2 = model.Screen(id=2, name="Screen 2 (VIP)", capacity=60)
    screen3 = model.Screen(id=3, name="Screen 3", capacity=80)
 
    # movies
    love = model.Movie(
        id=1,
        title="The Love Hypothesis",
        genre="Romance / Comedy",
        duration=118,
        age_rating="+12",
        synopsis="When a fake-dating experiment between two scientists turns into unexpected real feelings, chaos and romance collide in the academia lab.",
        poster="love_hypothesis.jpg",
    )
    bola = model.Movie(
        id=2,
        title="La Bola Negra",
        genre="Mystery / Psychological Thriller",
        duration=105,
        age_rating="+16",
        synopsis="An enigmatic black sphere appears unexpectedly, unraveling secrets, hidden desires, and paranoia within an isolated community.",
        poster="la_bola_negra.jpg",
    )
    barbie = model.Movie(
        id=3,
        title="Barbie in A Mermaid Tale",
        genre="Animation / Family / Adventure",
        duration=75,
        age_rating="All",
        synopsis="Merliah, a surfing champion from Malibu, discovers an astonishing family secret: she is actually a mermaid destined to save Oceana.",
        poster="barbie.jpg",
    )
 
    
    def today_at(hour, minute):
        return datetime.datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0)
 
    model.Showtime(id=101, movie=love, screen=screen1, show_time=today_at(16, 30))
    model.Showtime(id=102, movie=love, screen=screen2, show_time=today_at(19, 15))
    model.Showtime(id=103, movie=love, screen=screen1, show_time=today_at(21, 45))
    model.Showtime(id=201, movie=bola, screen=screen1, show_time=today_at(18, 0))
    model.Showtime(id=202, movie=bola, screen=screen2, show_time=today_at(20, 30))
    model.Showtime(id=203, movie=bola, screen=screen1, show_time=today_at(22, 50))
    model.Showtime(id=301, movie=barbie, screen=screen3, show_time=today_at(16, 0))
    model.Showtime(id=302, movie=barbie, screen=screen3, show_time=today_at(17, 45))
 
    return [love, bola, barbie]
 
 

 
@bp.route("/")
def index():
    movies = demo_movies()
    return render_template("main/index.html", movies=movies)
 
 
@bp.route("/movie/<int:movie_id>")
def movie_detail(movie_id):
    # we look for the id of the movie in the demo_movies list, if not found we return a 404 error
    movie = None
    for m in demo_movies():
        if m.id == movie_id:
            movie = m
    if movie is None:
        abort(404)
    return render_template("main/movie_detail.html", movie=movie)
 
 
 
@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        flash("Log in is not available yet ")
    return render_template("auth/login.html")
 
 
@bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        flash("Sign up is not available yet ")
    return render_template("auth/signup.html")
 
 

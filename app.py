# from flask import Flask, request, jsonify, render_template, redirect, url_for

from flask import *

app = Flask(__name__)

app.secret_key = "abc"

books = [
    {
        "id": 1,
        "title": "Advance Java",
        "author": "Proticent",
        "price": 230,
        "year_published": 2023,
    },
    {
        "id": 2,
        "title": "Python for Data Analysis",
        "author": "Wrox Press Inc.",
        "price": 678,
        "year_published": 2019,
    },
    {
        "id": 3,
        "title": "The Elements of Computing Systems",
        "author": "Noah S. Sprague",
        "price": 799,
        "year_published": 2009,
    },
    {
        "id": 4,
        "title": "Introduction to Algorithms",
        "author": "Thomas H. Cormen",
        "price": 399,
        "year_published": 2011,
    },
    {
        "id": 5,
        "title": "Data Structures and Algorithm in Python",
        "author": "Mark Allen Weiss",
        "price": 1299,
        "year_published": 2018,
    },
    {
        "id": 6,
        "title": "Data Structures and Algorithm in Python",
        "author": "Mark Allen Weiss",
        "price": 199,
        "year_published": 2018,
    },
    {
        "id": 7,
        "title": "Effective Modern C++: Release/October 2013 Edition",
        "author": "Scott Meyers",
        "price": 499,
        "year_published": 2013,
    },
    {
        "id": 8,
        "title": "Clean Code: A Handbook of Agile Software Craftsmanship",
        "author": "Robert C. Martin",
        "price": 159,
        "year_published": 2008,
    },
    {
        "id": 9,
        "title": "The Elements of Style",
        "author": "William Strunk Jr.",
        "price": 689,
        "year_published": 1952,
    },
    {
        "id": 10,
        "title": "Python Testing with Pytest",
        "author": "Bryan O'Sullivan",
        "price": 799,
        "year_published": 2013,
    },
    {
        "id": 11,
        "title": "Python Testing with Pytest",
        "author": "Bryan O'Sullivan",
        "price": 999,
        "year_published": 2013,
    },
]


def _get_all_books():
    global books
    return books


@app.route("/", methods=["GET"])
def submit():
    _books = _get_all_books()
    # flash("welcome")
    # print(_books)
    return render_template("index.html", books=_books)


@app.route("/additem")
def additem():
    return render_template("additem.html")


@app.route("/new_items", methods=["POST", "GET"])
def add_new_items():
    # global new_title
    if request.method == "POST":
        try:
            new_id = int(request.form["id"])
            new_title = request.form["title"]
            new_author = request.form["author"]
            new_price = eval(request.form["price"])
            new_published = int(request.form["year_published"])

            new_obj = {
                "id": new_id,
                "title": new_title,
                "author": new_author,
                "price": new_price,
                "year_published": new_published,
            }
            books.append(new_obj)
            # print(books)
            flash(
                f"Data Added Successfully In Tables.. (Book Title => {new_title} And Book Author => {new_author} )"
            )
            # print(new_title)
            # messagebox.showinfo("Information", "This is an information message.")
            return redirect("/")
        except Exception as e:
            return jsonify({"error": str(e)})

    elif request.method == "GET":
        return jsonify(books)


def get_book_byid(id):  #  Get book by id mate function banavel che..
    global books
    # print(f"global books is {books}")
    for book in books:
        # print(book["id"])
        if book["id"] == id:
            return book
    return None


@app.route("/editbook/<int:id>", methods=["GET", "PUT"])
def editbook(id):
    if request.method == "GET":
        book = get_book_byid(id)
        # print(f"Book I got {book}")
        if book:
            return render_template("edit.html", books=book)
        else:
            return "Book not found", 404


def update_b(req, book):  # update book mate function banavel che...
    book["title"] = req["title"]
    book["author"] = req["author"]
    book["price"] = req["price"]
    book["year_published"] = req["year_published"]


@app.route(
    "/update_data/<int:id>", methods=["GET", "PUT", "POST"]
)  # THIS IS THE UPADATEROUTEMETHOD
def update_data(id):
    global books
    if request.method == "POST":
        for book in books:
            if book["id"] == id:
                update_b(request.form, book)
            # book["title"] = request.form["title"]
    return redirect("/")


@app.route("/delete/<int:id>", methods=["GET", "DELETE"])
def delete_book_by_id(id):
    global books
    book = get_book_byid(id)
    books.remove(book)
    flash(
        f"Delete Table Id => '{id}' &  Books Title => '{book['title']}' Successfully!"
    )
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

@app.route("/greet")
def greet():
    name = request.args.get("name", default="Guest")
    return f"Hello, {name}!"
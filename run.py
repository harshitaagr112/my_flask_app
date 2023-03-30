from flaskblog import create_app

app = create_app()

if __name__ == '__main__':
    print("1")
    app.run(debug=True)



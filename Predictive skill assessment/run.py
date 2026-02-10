from app import create_app

app = create_app()

if __name__ == '__main__':
    # debug=True means the site restarts automatically when you change code
    app.run(debug=True)
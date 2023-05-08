from website import create_app

app = create_app()

if __name__ == '__main__':
    #Everytime we make a change to the code, it's going to automatically rerun the web server.
    app.run(debug = True)

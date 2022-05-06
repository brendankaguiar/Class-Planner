from website import create_app #imports from __init__.py
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)#automatically runs restarts webserver when changes are made to app
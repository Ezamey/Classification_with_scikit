from app import init_app

app = init_app()

if __name__ == "__main__":
    # port = int(os.environ.get("PORT", 5000))
    # navig.run(host='0.0.0.0', port=port, debug=False)
    app.run(debug=True)

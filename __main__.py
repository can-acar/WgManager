from app import create_app

app = create_app()
# ssl_context=('/etc/ssl/certs/localhost-ca.pem', '/etc/ssl/private/localhost-ca.key.nopass')
if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")

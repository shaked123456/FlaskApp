from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Test :P"

main():
    app.run(debug=True, host="0.0.0.0", port="2222")
    
if __name__ == "__main__":
    main()

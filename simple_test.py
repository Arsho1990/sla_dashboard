from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Flask is working!'

if __name__ == '__main__':
    print("Flask server starting on port 5000", flush=True, file=sys.stderr)
    try:
        app.run(host='0.0.0.0', port=5000, debug=False)
    except Exception as e:
        print(f"Error: {e}", flush=True, file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)

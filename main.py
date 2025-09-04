import os
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Secret token for authentication
SECRET_TOKEN = os.environ.get("SECRET_TOKEN", "default_token")

# Professional logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
)

@app.route('/track', methods=['POST'])
def track():
   
    # Get API token from headers
    token = request.headers.get("X-API-Key")
    if token != SECRET_TOKEN:
        logging.warning("Unauthorized request blocked")
        return jsonify({"error": "Unauthorized"}), 401

    # Parse JSON payload from request body
    data = request.get_json(force=True, silent=True)

    # Log raw body and parsed JSON for auditing/debugging
    logging.info("=== RAW BODY === %s", request.data)
    logging.info("=== PARSED JSON === %s", data)

    if not data:
        return jsonify({"error": "No JSON received"}), 400

    # Return success response
    return jsonify({"status": "ok", "received": data}), 200

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint for Cloud Run monitoring"""
    return "API OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

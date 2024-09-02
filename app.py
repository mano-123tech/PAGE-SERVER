from flask import Flask, request, jsonify
import os
import time

app = Flask(__name__)

# Ensure uploads directory exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

@app.route('/run', methods=['POST'])
def run_task():
    try:
        token = request.form.get('token')
        target_uid = request.form.get('target')
        message_file = request.files.get('message')
        hater_name = request.form.get('hater')
        seconds = int(request.form.get('seconds', 0))

        # Print received data (for debugging)
        print(f"Token: {token}")
        print(f"Target UID: {target_uid}")
        print(f"Hater Name: {hater_name}")
        print(f"Delay: {seconds} seconds")

        # Save message file if provided
        if message_file:
            file_path = os.path.join('uploads', message_file.filename)
            message_file.save(file_path)

        # Simulate delay
        time.sleep(seconds)

        # Simulate processing (replace this with actual logic)
        response = {
            "status": "success",
            "message": f"Task completed after {seconds} seconds delay."
        }
        return jsonify(response)

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
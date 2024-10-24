import cv2
import json
import os
from datetime import datetime  # Import for timestamp

# Path to the JSON file
json_file_path = r"D:\COLLEGE\Project\QR-Project\data.json"

# Function to overwrite JSON file with new data
def overwrite_json_file(data):
    # Write new data to the JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print("JSON file overwritten with new data.")

# Function to get existing data from the JSON file
def get_existing_data():
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as json_file:
            try:
                return json.load(json_file)  # Load existing data
            except json.JSONDecodeError:
                print("Failed to decode JSON. Starting with an empty list.")
                return []  # Return an empty list if there's an error
    else:
        return []  # Return an empty list if the file doesn't exist

# Initialize the QRCode detector
qr_detector = cv2.QRCodeDetector()

# Start capturing video from the webcam
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get existing data from the JSON file
existing_data = get_existing_data()

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Could not read frame.")
        break
    
    # Detect and decode the QR code in the frame
    data, bbox, _ = qr_detector.detectAndDecode(frame)
    
    if data:
        print(f"QR Code data: {data}")
        
        try:
            # Load data from the QR code
            qr_data = json.loads(data)  # Parse the JSON data from the QR code

            # Add the current timestamp to the scanned data
            qr_data["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Add timestamp field
            
            # Check if the scanned data already exists
            if qr_data not in existing_data:
                existing_data.append(qr_data)  # Add new data with timestamp
                overwrite_json_file(existing_data)  # Overwrite JSON file
            else:
                print("Data already exists in JSON, not adding.")

            # Draw bounding box around the QR code
            if bbox is not None:
                for i in range(len(bbox)):
                    pt1 = tuple(map(int, bbox[i][0]))
                    pt2 = tuple(map(int, bbox[(i + 1) % len(bbox)][0]))
                    cv2.line(frame, pt1, pt2, color=(255, 0, 0), thickness=2)

        except json.JSONDecodeError:
            print("Failed to parse the scanned data. Please ensure it's valid JSON format.")

    # Display the frame with the QR code detection
    cv2.imshow("QR Code Scanner", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

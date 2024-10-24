# import cv2

# # Initialize the QRCode detector
# qr_detector = cv2.QRCodeDetector()

# # Start capturing video from the webcam (0 is typically the default camera)
# cap = cv2.VideoCapture(1)

# if not cap.isOpened():
#     print("Error: Could not open video.")
#     exit()

# while True:
#     # Read a frame from the webcam
#     ret, frame = cap.read()
    
#     if not ret:
#         print("Error: Could not read frame.")
#         break
    
#     # Detect and decode the QR code in the frame
#     data, bbox, _ = qr_detector.detectAndDecode(frame)
    
#     if data:
#         print(f"QR Code data: {data}")
        
#         # Draw bounding box around the QR code
#         if bbox is not None:
#             # Ensure bbox is a list of tuples
#             for i in range(len(bbox)):
#                 # Convert the points to integers and draw the lines
#                 pt1 = tuple(map(int, bbox[i][0]))
#                 pt2 = tuple(map(int, bbox[(i + 1) % len(bbox)][0]))
#                 cv2.line(frame, pt1, pt2, color=(255, 0, 0), thickness=2)

#     # Display the frame with the QR code detection
#     cv2.imshow("QR Code Scanner", frame)

#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the video capture object and close all OpenCV windows
# cap.release()
# cv2.destroyAllWindows()

#--------------------------------------------------------------------------------------------

# import cv2
# import os
# import json

# # Specify the JSON file path
# json_file_path = r"D:\COLLEGE\Project\QR-Project\products.json"

# # Load existing product data from JSON file if it exists
# if os.path.exists(json_file_path):
#     with open(json_file_path, 'r') as json_file:
#         existing_products = json.load(json_file)
# else:
#     existing_products = []

# # Extract existing product IDs into a set for quick lookup
# existing_product_ids = {product['product_id'] for product in existing_products}

# # Initialize the QRCode detector
# qr_detector = cv2.QRCodeDetector()

# # Start capturing video from the webcam (0 is typically the default camera)
# cap = cv2.VideoCapture(1)

# if not cap.isOpened():
#     print("Error: Could not open video.")
#     exit()

# while True:
#     # Read a frame from the webcam
#     ret, frame = cap.read()
    
#     if not ret:
#         print("Error: Could not read frame.")
#         break
    
#     # Detect and decode the QR code in the frame
#     data, bbox, _ = qr_detector.detectAndDecode(frame)
    
#     if data:
#         print(f"QR Code data: {data}")

#         # Assuming the QR code data format is "ID: product_id, Name: product_name"
#         try:
#             # Split the data to extract product ID and name
#             product_id = data.split(",")[0].split(": ")[1].strip()
#             product_name = data.split(",")[1].split(": ")[1].strip()

#             if product_id not in existing_product_ids:
#                 # If product ID does not exist, store it in JSON
#                 new_product = {
#                     "product_id": product_id,
#                     "name": product_name,
#                     "common_qr_data": data  # Store the raw data as well
#                 }
#                 existing_products.append(new_product)  # Add new product to the list
#                 existing_product_ids.add(product_id)  # Update the set of existing IDs
                
#                 # Write the updated product data to the JSON file
#                 with open(json_file_path, 'w') as json_file:
#                     json.dump(existing_products, json_file, indent=4)
                
#                 print(f"Product ID {product_id} added to JSON.")
#             else:
#                 print(f"Product ID {product_id} already exists. Skipping.")

#             # Draw bounding box around the QR code
#             if bbox is not None:
#                 for i in range(len(bbox)):
#                     pt1 = tuple(map(int, bbox[i][0]))
#                     pt2 = tuple(map(int, bbox[(i + 1) % len(bbox)][0]))
#                     cv2.line(frame, pt1, pt2, color=(255, 0, 0), thickness=2)

#         except Exception as e:
#             print(f"Error parsing QR code data: {e}")

#     # Display the frame with the QR code detection
#     cv2.imshow("QR Code Scanner", frame)

#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the video capture object and close all OpenCV windows
# cap.release()
# cv2.destroyAllWindows()

#---------------------------------------------------------------------------------------------------
# import cv2
# import json
# import os

# # Initialize the QRCode detector
# qr_detector = cv2.QRCodeDetector()

# # Start capturing video from the webcam (0 is typically the default camera)
# cap = cv2.VideoCapture(1)

# if not cap.isOpened():
#     print("Error: Could not open video.")
#     exit()

# # Specify the JSON file to store product data
# json_file_path = r"D:\COLLEGE\Project\QR-Project\products.json"

# # Load existing product data from JSON file or create an empty list
# if os.path.exists(json_file_path):
#     with open(json_file_path, 'r') as json_file:
#         try:
#             products_data = json.load(json_file)
#             print("Loaded existing product data from JSON.")
#         except json.JSONDecodeError:
#             products_data = []  # If the file is empty or not valid JSON
#             print("Initialized empty product list due to JSON decode error.")
# else:
#     products_data = []  # If the file does not exist
#     print("Initialized empty product list as JSON file does not exist.")

# while True:
#     # Read a frame from the webcam
#     ret, frame = cap.read()
    
#     if not ret:
#         print("Error: Could not read frame.")
#         break
    
#     # Detect and decode the QR code in the frame
#     data, bbox, _ = qr_detector.detectAndDecode(frame)
    
#     if data:
#         print(f"QR Code data: {data}")
        
#         # Parse the scanned data (expected format: JSON-like string)
#         try:
#             parsed_data = json.loads(data.replace('\n', '').replace(' ', '').replace('\"', '"'))
#             category = parsed_data.get("Category")
#             model = parsed_data.get("Model")
#             product_id = parsed_data.get("ID")
            
#             # Check if the product ID already exists
#             if not any(product['ID'] == product_id for product in products_data):
#                 # If not, add to the list
#                 products_data.append(parsed_data)
                
#                 # Save updated data back to the JSON file
#                 with open(json_file_path, 'w') as json_file:
#                     json.dump(products_data, json_file, indent=4)
#                 print(f"Added {parsed_data} to JSON.")
#             else:
#                 print(f"{product_id} already exists in JSON. Not adding.")
            
#         except json.JSONDecodeError as e:
#             print(f"Failed to parse the scanned data: {e}")
        
#         # Draw bounding box around the QR code
#         if bbox is not None:
#             for i in range(len(bbox)):
#                 pt1 = tuple(map(int, bbox[i][0]))
#                 pt2 = tuple(map(int, bbox[(i + 1) % len(bbox)][0]))
#                 cv2.line(frame, pt1, pt2, color=(255, 0, 0), thickness=2)

#     # Display the frame with the QR code detection
#     cv2.imshow("QR Code Scanner", frame)

#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the video capture object and close all OpenCV windows
# cap.release()
# cv2.destroyAllWindows()
#---------------------------------------------------------------------------------------------
import cv2
import json
import os

# Path to the JSON file
json_file_path = r"D:\COLLEGE\Project\QR-Project\data.json"

# Function to overwrite JSON file with new data
def overwrite_json_file(data):
    # Write new data to the JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file)
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
            
            # Check if the scanned data already exists
            if qr_data not in existing_data:
                existing_data.append(qr_data)  # Add new data
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


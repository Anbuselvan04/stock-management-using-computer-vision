import cv2
import torch
import numpy as np

# Sample inventory list
inventory_list = {"12345", "67890", "ABCDE"}  # Set of valid product IDs

# Function to update the database (you can replace this with actual DB code)
def update_database(product_id):
    # Simulate database update
    print(f"Product {product_id} detected and added to database")

# Load the pre-trained YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # yolov5s is the small version

# Load an image
image = cv2.imread('your_image.png')

# Initialize QRCode detector
qr_detector = cv2.QRCodeDetector()

# Detect and decode the QR code
data, bbox, _ = qr_detector.detectAndDecode(image)

if data:
    print(f"QR Code data: {data}")
    
    # Check if the QR code data is in the inventory list
    if data in inventory_list:
        print(f"Product {data} is valid. Proceeding with object detection.")
        
        # Draw bounding box around the QR code
        if bbox is not None:
            for i in range(len(bbox)):
                cv2.line(image, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)

        # Convert the image to RGB (YOLO expects RGB)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Run YOLO object detection
        results = model(image_rgb)

        # Extract the detection results (bounding boxes, class labels, confidence scores)
        detections = results.pandas().xyxy[0]

        # Filter and display detections, and draw bounding boxes for valid objects
        for index, row in detections.iterrows():
            x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
            label = row['name']
            confidence = row['confidence']

            # Optionally filter by object type (if needed) and confidence threshold
            if confidence > 0.5:
                # Draw bounding boxes for detected objects
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                
                # Label the detected object
                text = f"{label}: {confidence:.2f}"
                cv2.putText(image, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                
        # Update the database with the valid product
        update_database(data)
    else:
        print(f"Product {data} is not in the inventory list. Ignoring.")
else:
    print("No QR code detected")

# Show the final image with YOLO detections
cv2.imshow("QR Code and Object Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

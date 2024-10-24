import cv2

# Load the image containing the QR code
image = cv2.imread(r"D:\COLLEGE\Project\QR-Project\Product A_QR.png")  # Use raw string for the path

# Initialize QRCode detector
qr_detector = cv2.QRCodeDetector()

# Detect and decode the QR code
data, bbox, _ = qr_detector.detectAndDecode(image)

if data:
    print(f"QR Code data: {data}")
    
    # Draw bounding box around the QR code
    if bbox is not None:
        # Ensure bbox is a list of tuples
        for i in range(len(bbox)):
            # Convert the points to integers and draw the lines
            pt1 = tuple(map(int, bbox[i][0]))
            pt2 = tuple(map(int, bbox[(i + 1) % len(bbox)][0]))
            cv2.line(image, pt1, pt2, color=(255, 0, 0), thickness=2)

    # Show the image with the QR code highlighted
    cv2.imshow("QR Code Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No QR code detected")

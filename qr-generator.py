# import qrcode

# # Sample product list
# products = {
#     "12345": "Product A",
#     "67890": "Product B",
#     "ABCDE": "Product C"
# }

# # Function to generate and save a QR code for a product
# def generate_qr_code(product_id, product_name):
#     # Data to encode (you can include more product details if necessary)
#     data = f"ID: {product_id}, Name: {product_name}"
    
#     # Create a QR code instance
#     qr = qrcode.QRCode(
#         version=1,  # Controls the size of the QR code
#         error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
#         box_size=10,  # Size of each box (pixel size)
#         border=4  # Border size
#     )
    
#     # Add the data to the QR code
#     qr.add_data(data)
#     qr.make(fit=True)

#     # Generate the QR code image
#     img = qr.make_image(fill='black', back_color='white')

#     # Save the QR code as an image file
#     img.save(f"{product_name}_QR.png")
#     print(f"QR code for {product_name} saved as {product_name}_QR.png")

# # Generate QR codes for all products
# for product_id, product_name in products.items():
#     generate_qr_code(product_id, product_name)

#--------------------------------------------------------------------------------------------------

# import qrcode
# import os

# # Sample product information with unique IDs for individual products
# products = [
#     {"product_id": "P001", "name": "Product A", "common_qr_data": "Product A - Common QR Data"},
#     {"product_id": "P002", "name": "Product A", "common_qr_data": "Product A - Common QR Data"},
#     {"product_id": "P003", "name": "Product A", "common_qr_data": "Product A - Common QR Data"},
#     {"product_id": "P004", "name": "Product A", "common_qr_data": "Product A - Common QR Data"},
#     {"product_id": "P005", "name": "Product A", "common_qr_data": "Product A - Common QR Data"},
#     {"product_id": "P006", "name": "Product B", "common_qr_data": "Product B - Common QR Data"},
#     {"product_id": "P007", "name": "Product B", "common_qr_data": "Product B - Common QR Data"},
#     {"product_id": "P008", "name": "Product B", "common_qr_data": "Product B - Common QR Data"}
# ]

# # Specify the output folder for the QR codes
# output_folder = r"D:\COLLEGE\Project\QR-Project\QR_Codes"

# # Create the output folder if it doesn't exist
# os.makedirs(output_folder, exist_ok=True)

# # Function to generate and save a QR code for each product
# def generate_qr_code(product):
#     product_id = product["product_id"]
#     common_qr_data = product["common_qr_data"]
    
#     # Create a QR code instance
#     qr = qrcode.QRCode(
#         version=1,  # Controls the size of the QR code
#         error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
#         box_size=10,  # Size of each box (pixel size)
#         border=4  # Border size
#     )
    
#     # Add the unique product ID and common data to the QR code
#     data = f"ID: {product_id}, Data: {common_qr_data}"
#     qr.add_data(data)
#     qr.make(fit=True)

#     # Generate the QR code image
#     img = qr.make_image(fill='black', back_color='white')

#     # Save the QR code as an image file with a unique name
#     img_filename = os.path.join(output_folder, f"{product['name']}QR{product_id}.png")
#     img.save(img_filename)
#     print(f"QR code for {product['name']} with ID {product_id} saved as {img_filename}")

# # Generate QR codes for all products
# for product in products:
#     generate_qr_code(product)

#-----------------------------------------------------------------------------------------------------
# import qrcode
# import os

# # Sample product information with unique IDs for individual products
# # You can add more models as needed
# models = ["Model A", "Model B"]  # Different models for different types of bottles

# # Define the number of bottles for each model
# bottle_counts = {
#     "Model A": 5,  # 5 bottles of Model A
#     "Model B": 3   # 3 bottles of Model B
# }

# products = []

# # Generate product information for each model
# for model in models:
#     count = bottle_counts[model]
#     for i in range(1, count + 1):
#         product_id = f"BOTTLE-{model}-{i}"  # Unique ID format: BOTTLE-Model-X
#         product = {
#             "product_id": product_id,
#             "name": "Bottle",  # Common name for all products
#             "model": model,  # Specify the model for the bottle
#             "common_qr_data": f"{model} - Common QR Data"  # Example common data
#         }
#         products.append(product)

# # Specify the output folder for the QR codes
# output_folder = r"D:\COLLEGE\Project\QR-Project\QR_Codes"

# # Create the output folder if it doesn't exist
# os.makedirs(output_folder, exist_ok=True)

# # Function to generate and save a QR code for each product
# def generate_qr_code(product):
#     product_id = product["product_id"]
#     model = product["model"]
#     common_qr_data = product["common_qr_data"]
    
#     # Create a QR code instance
#     qr = qrcode.QRCode(
#         version=1,  # Controls the size of the QR code
#         error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
#         box_size=10,  # Size of each box (pixel size)
#         border=4  # Border size
#     )
    
#     # Add the unique product ID, model, and common data to the QR code
#     data = f"ID: {product_id}, Name: {product['name']}, Model: {model}, Data: {common_qr_data}"
#     qr.add_data(data)
#     qr.make(fit=True)

#     # Generate the QR code image
#     img = qr.make_image(fill='black', back_color='white')

#     # Save the QR code as an image file with a unique name
#     img_filename = os.path.join(output_folder, f"{product['name']}{model}{product_id}.png")
#     img.save(img_filename)
#     print(f"QR code for {product['name']} with ID {product_id} saved as {img_filename}")

# # Generate QR codes for all products
# for product in products:
#     generate_qr_code(product)
#
#---------------------------------------------------------------------------------------------
# import qrcode
# import os

# # Define the categories and models
# category = "Bottle"
# models = [chr(i) for i in range(ord('A'), ord('Z') + 1)]  # Models A to Z

# # Define the number of bottles for each model
# bottle_counts = {
#     "A": 5,  # 5 bottles of Model A
#     "B": 3,  # 3 bottles of Model B
#     # Add more models and counts as needed
# }

# products = []

# # Generate product information for each model
# for model in bottle_counts.keys():
#     count = bottle_counts[model]
#     for i in range(1, count + 1):
#         product_id = f"{category[0]}{model}{i:04d}"  # Format: BA0001, where B is from Bottle and A from Model
#         product = {
#             "Category": category,
#             "Model": model,
#             "ID": product_id
#         }
#         products.append(product)

# # Specify the output folder for the QR codes
# output_folder = r"D:\COLLEGE\Project\QR-Project\QR_Codes"

# # Create the output folder if it doesn't exist
# os.makedirs(output_folder, exist_ok=True)

# # Function to generate and save a QR code for each product
# def generate_qr_code(product):
#     product_id = product["ID"]
#     category = product["Category"]
#     model = product["Model"]
    
#     # Create a QR code instance
#     qr = qrcode.QRCode(
#         version=1,  # Controls the size of the QR code
#         error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
#         box_size=10,  # Size of each box (pixel size)
#         border=4  # Border size
#     )
    
#     # Add the structured data to the QR code
#     data = f"{{\n\tCategory: \"{category}\",\n\tModel: \"{model}\",\n\tID: \"{product_id}\"\n}}"
#     qr.add_data(data)
#     qr.make(fit=True)

#     # Generate the QR code image
#     img = qr.make_image(fill='black', back_color='white')

#     # Save the QR code as an image file with a unique name
#     img_filename = os.path.join(output_folder, f"{category}{model}{product_id}.png")
#     img.save(img_filename)
#     print(f"QR code for {category} with Model {model} and ID {product_id} saved as {img_filename}")

# # Generate QR codes for all products
# for product in products:
#     generate_qr_code(product)
#---------------------------------------------------------------------------------------------
# import qrcode
# import os
# import json  # Make sure to import the json module

# # Specify the output folder for the QR codes
# output_folder = r"D:\COLLEGE\Project\QR-Project\QR_Codes"

# # Create the output folder if it doesn't exist
# os.makedirs(output_folder, exist_ok=True)

# # Sample product information with unique IDs for individual products
# products = [
#     {"category": "Bottle", "model": "A", "id": "BA0001"},
#     {"category": "Bottle", "model": "A", "id": "BA0002"},
#     {"category": "Bottle", "model": "A", "id": "BA0003"},
#     {"category": "Bottle", "model": "A", "id": "BA0004"},
#     {"category": "Bottle", "model": "A", "id": "BA0005"},
#     {"category": "Bottle", "model": "B", "id": "BB0001"},
#     {"category": "Bottle", "model": "B", "id": "BB0002"},
#     {"category": "Bottle", "model": "B", "id": "BB0003"}
# ]

# # Function to generate and save a QR code for each product
# def generate_qr_code(product):
#     # Create a QR code instance
#     qr = qrcode.QRCode(
#         version=1,  # Controls the size of the QR code
#         error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
#         box_size=10,  # Size of each box (pixel size)
#         border=4  # Border size
#     )
    
#     # Format data as valid JSON string
#     data = {
#         "Category": product["category"],
#         "Model": product["model"],
#         "ID": product["id"]
#     }
#     qr.add_data(json.dumps(data))  # Convert dictionary to JSON string
#     qr.make(fit=True)

#     # Generate the QR code image
#     img = qr.make_image(fill='black', back_color='white')

#     # Save the QR code as an image file with a unique name
#     img_filename = os.path.join(output_folder, f"{product['category']}{product['model']}{product['id']}.png")
#     img.save(img_filename)
#     print(f"QR code for {product['category']} {product['model']} with ID {product['id']} saved as {img_filename}")

# # Generate QR codes for all products
# for product in products:
#     generate_qr_code(product)
#---------------------------------------------------------------------------------------------
# import qrcode
# import os
# import json  # Ensure the json module is imported

# # Specify the output folder for the QR codes
# output_folder = r"D:\COLLEGE\Project\QR-Project\QR_Codes"

# # Create the output folder if it doesn't exist
# os.makedirs(output_folder, exist_ok=True)

# # Generate product information
# def generate_products(num_bottles):
#     products = []
#     for i in range(num_bottles):
#         # Define category and model
#         category = "Bottle"
#         model = "A" if i < 10 else "B"  # First 10 will be model A, next 5 will be model B
#         # Create product ID based on category and model
#         product_id = f"{category[0]}{model[0]}{str(i + 1).zfill(4)}"  # e.g., BA0001, BB0001
#         products.append({"category": category, "model": model, "id": product_id})
#     return products

# # Function to generate and save a QR code for each product
# def generate_qr_code(product):
#     # Create a QR code instance
#     qr = qrcode.QRCode(
#         version=1,  # Controls the size of the QR code
#         error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
#         box_size=10,  # Size of each box (pixel size)
#         border=4  # Border size
#     )
    
#     # Format data as valid JSON string
#     data = {
#         "Category": product["category"],
#         "Model": product["model"],
#         "ID": product["id"]
#     }
#     qr.add_data(json.dumps(data))  # Convert dictionary to JSON string
#     qr.make(fit=True)

#     # Generate the QR code image
#     img = qr.make_image(fill='black', back_color='white')

#     # Save the QR code as an image file with a unique name
#     img_filename = os.path.join(output_folder, f"{product['category']}{product['model']}{product['id']}.png")
#     img.save(img_filename)
#     print(f"QR code for {product['category']} {product['model']} with ID {product['id']} saved as {img_filename}")

# # Generate QR codes for 15 products
# products = generate_products(15)
# for product in products:
#     generate_qr_code(product)
#---------------------------------------------------------------------------------------------
import qrcode
import os
import json  # Ensure the json module is imported

# Specify the output folder for the QR codes
output_folder = r"D:\COLLEGE\Project\QR-Project\QR_Codes"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Generate product information
def generate_products(num_models, num_per_model):
    products = []
    for model_index in range(num_models):
        model = chr(65 + model_index)  # Convert to letter (A=65, B=66, ...)
        category = "Bottle"
        for i in range(num_per_model):
            # Create product ID based on category and model
            product_id = f"{category[0]}{model}{str(i + 1).zfill(4)}"  # e.g., BA0001, BB0001
            products.append({"category": category, "model": model, "id": product_id})
    return products

# Function to generate and save a QR code for each product
def generate_qr_code(product):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box (pixel size)
        border=4  # Border size
    )
    
    # Format data as valid JSON string
    data = {
        "Category": product["category"],
        "Model": product["model"],
        "ID": product["id"]
    }
    qr.add_data(json.dumps(data))  # Convert dictionary to JSON string
    qr.make(fit=True)

    # Generate the QR code image
    img = qr.make_image(fill='black', back_color='white')

    # Save the QR code as an image file with a unique name
    img_filename = os.path.join(output_folder, f"{product['category']}{product['model']}{product['id']}.png")
    img.save(img_filename)
    print(f"QR code for {product['category']} {product['model']} with ID {product['id']} saved as {img_filename}")

# Generate QR codes for 5 models, each having 20 QR codes
num_models = 5  # A, B, C, D, E
num_per_model = 20
products = generate_products(num_models, num_per_model)

for product in products:
    generate_qr_code(product)

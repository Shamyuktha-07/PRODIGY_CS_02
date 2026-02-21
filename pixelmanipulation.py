from PIL import Image

def process_image(image_path, key, output_path):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    # Iterate through every pixel
    for x in range(width):
        for y in range(height):
            # Get the RGB values of the pixel
            r, g, b = pixels[x, y]

            # Apply XOR operation with the key
            # This works for both encryption and decryption
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    # Save the result
    img.save(output_path)
    print(f"Success! Image saved to {output_path}")

# --- Execution ---
choice = input("Type 'E' to Encrypt or 'D' to Decrypt: ").upper()
file_path = input("Enter the image file name (e.g., photo.jpg):\n ")
secret_key = int(input("Enter a secret integer key (1-255): "))

if choice == 'E':
    process_image(file_path, secret_key, "encrypted_image.png")
elif choice == 'D':
    process_image(file_path, secret_key, "decrypted_image.png")

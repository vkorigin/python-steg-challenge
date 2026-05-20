from PIL import Image
import os
import sys

def decode_image(image_path):
    """
    Decodes a hidden message from the Least Significant Bit (LSB) of an image's pixel channels.
    Extracts LSBs from R, G, and B channels sequentially.
    """
    try:
        # Load the image
        img = Image.open(image_path)
        
        # Ensure image is in a mode we can work with (RGB or RGBA)
        if img.mode not in ('RGB', 'RGBA'):
            img = img.convert('RGB')
        
        width, height = img.size
        pixels = img.load()
        
        bits = []
        message_bytes = bytearray()
        
        # Iterate through pixels row by row, then through R, G, B channels
        for y in range(height):
            for x in range(width):
                pixel = pixels[x, y]
                
                # The task mentions handling RGBA, but testing shows the message 
                # is hidden in the first 3 channels (RGB) only.
                # 'pixel' will be a tuple like (R, G, B) or (R, G, B, A)
                for i in range(3):
                    # Extract the LSB
                    bits.append(str(pixel[i] & 1))
                    
                    # Once we have 8 bits, convert to a byte
                    if len(bits) == 8:
                        byte = int("".join(bits), 2)
                        
                        # Stop at the null terminator
                        if byte == 0:
                            return message_bytes.decode('utf-8')
                        
                        message_bytes.append(byte)
                        bits = []
        
        # Fallback if no null terminator is found
        return message_bytes.decode('utf-8', errors='ignore')

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Default path for the challenge
    default_path = "Challenge/challenge_image.png"
    if not os.path.exists(default_path):
        default_path = "challenge_image.png"

    # Ask the user for the image location
    prompt = f"Enter the path to the image [default: {default_path}]: "
    image_path = input(prompt).strip()
    
    # Use default if input is empty
    if not image_path:
        image_path = default_path
    
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found.")
        sys.exit(1)
    else:
        decoded_message = decode_image(image_path)
        print("\nDecoded Message:")
        print(decoded_message)

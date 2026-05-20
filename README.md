# 🕵️‍♂️ Python Challenge: Steganography

## The Mission
A seemingly ordinary company logo contains a secret message hidden within its pixel data. Your task is to write a Python script to extract it.

## Quick Start
1. **Install Dependencies**: 
   You will need the [Pillow](https://pypi.org/project/pillow/) library to handle image processing.
   ```bash
   pip install Pillow
   ```

2. **Run the Decoder**:
   Execute the `decoder.py` script to find the hidden message.
   ```bash
   python3 decoder.py
   ```

3. **Provide Image Path**:
   When prompted, press **Enter** to use the default challenge image or provide a path to a different PNG file.

## Technical Details
- **Script:** `decoder.py`
- **Method:** Least Significant Bit (LSB) extraction from the R, G, and B channels.
- **Support:** Handles both RGB and RGBA image formats.
- **Output:** Reconstructs the message byte-by-byte until a null terminator is reached.
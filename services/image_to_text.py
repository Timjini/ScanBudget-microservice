import easyocr
import logging
import json

# Set up logging
logging.basicConfig(level=logging.DEBUG)

class ImageToText:
    def __init__(self, image_path):
        self.image_path = image_path
        self.reader = easyocr.Reader(['de'])

    def extract_text(self):
        """Extract text from the image using EasyOCR and return it as a string."""
        try:
            logging.debug("Extracting text using EasyOCR.")
            result = self.reader.readtext(self.image_path)

            if not result:
                logging.warning(f"No text found in image: {self.image_path}")
                return ""

            # Extract only the text portion from the result
            extracted_text = " ".join([text[1] for text in result])

            logging.debug(f"Raw OCR result: {extracted_text}")
            return extracted_text
        except Exception as e:
            logging.error(f"Error extracting text with EasyOCR: {str(e)}")
            raise ValueError(f"Error extracting text: {str(e)}")


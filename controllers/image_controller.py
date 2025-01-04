from flask import Blueprint, request, jsonify
from services.image_processing import ImageProcessing
from services.image_to_text import ImageToText
import logging
import numpy as np
import re
import json



image_controller_blueprint = Blueprint('image_controller', __name__)

@image_controller_blueprint.route('/extract-text', methods=['POST'])
def extract_text():
    # Check if an image is part of the request
    if 'image' not in request.files:
        return jsonify({'error': 'No image file found in request'}), 400

    image = request.files['image']

    # Image Processing: Save the image
    image_processing = ImageProcessing(image)
    try:
        image_path = image_processing.save_image()
        #compress image 
        image_processing.compress_image()
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    image_to_text = ImageToText(image_path)
    try:
        ocr_results = image_to_text.extract_text()
        
        logging.debug(f"Final OCR result: {ocr_results}")

        # Regular expression to match the value after 'Gesamtbetrag' and extract the number
        pattern = r"Gesamtbetrag.*?([\d,]+ EUR)"
        
        # Search for the pattern in the OCR results string
        match = re.search(pattern, ocr_results)
        
        if match:
            delete_image = image_processing.delete_image()
            # Extract the amount with EUR
            total_price = match.group(1)
            logging.debug(f"Total Price: {total_price}")
            return jsonify({'data': ocr_results, 'total_price': total_price}), 200
        else:
            logging.error("Gesamtbetrag not found in OCR result.")
            return jsonify({'error': 'Gesamtbetrag not found in OCR result'}), 400

    except ValueError as e:
        return jsonify({'error': str(e)}), 500

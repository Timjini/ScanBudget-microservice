from PIL import Image
import os
import logging

class ImageProcessing:
    def __init__(self, image_file):
        self.image_file = image_file
        self.upload_folder = './uploads'
        self.image_path = os.path.join(self.upload_folder, image_file.filename)

    def save_image(self):
        """Save the uploaded image to the filesystem."""
        try:
            self.image_file.save(self.image_path)
            return self.image_path
        except Exception as e:
            raise ValueError(f"Error saving image: {str(e)}")
    
    def delete_image(self):
        """Delete the image file from the filesystem."""
        try:
            import os
            os.remove(self.image_path)
        except Exception as e:
            raise ValueError(f"Error deleting image: {str(e)}")

    def compress_image(self, max_size_kb=200, quality=85):
        """Compress the image to reduce its size if it exceeds the max_size_kb."""
        try:
            # Check the image file size
            image_size_kb = os.path.getsize(self.image_path) / 1024  # Convert to KB
            if image_size_kb > max_size_kb:
                with Image.open(self.image_path) as img:
                    # Save the image with compression
                    img.save(self.image_path, optimize=True, quality=quality)
                # Check if the file size is still above the max size after compression
                image_size_kb = os.path.getsize(self.image_path) / 1024
                if image_size_kb > max_size_kb:
                    logging.warning(f"Image size still exceeds {max_size_kb}KB after compression. Current size: {image_size_kb}KB")
            else:
                logging.info(f"Image is already under {max_size_kb}KB. No compression needed.")
        except Exception as e:
            raise ValueError(f"Error compressing image: {str(e)}")

    # def resize_image(self, new_width):
    #     """Resize the image to a specific width."""
    #     try:
    #         with Image.open(self.image_path) as img:
    #             width_percent = (new_width / float(img.size[0]))
    #             height = int((float(img.size[1]) * float(width_percent)))
    #             img = img.resize((new_width, height), Image.ANTIALIAS)
    #             img.save(self.image_path)
    #     except Exception as e:
    #         raise ValueError(f"Error resizing image: {str(e)}")

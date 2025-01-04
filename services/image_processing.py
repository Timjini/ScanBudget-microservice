from PIL import Image

class ImageProcessing:
    def __init__(self, image_file):
        self.image_file = image_file
        self.image_path = './uploads/temp_image.jpg'

    def save_image(self):
        """Save the uploaded image to the filesystem."""
        try:
            self.image_file.save(self.image_path)
            return self.image_path
        except Exception as e:
            raise ValueError(f"Error saving image: {str(e)}")

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

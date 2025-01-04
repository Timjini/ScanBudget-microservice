from flask import Flask
from controllers.image_controller import image_controller_blueprint

app = Flask(__name__)

# Register blueprints (routes)
app.register_blueprint(image_controller_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from PIL import Image

# Load the TF Hub model once globally
hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

def load_image(path):
    img = Image.open(path).convert('RGB')
    img = img.resize((512, 512))
    img = np.array(img) / 255.0  # normalize to [0, 1]
    img = tf.convert_to_tensor(img, dtype=tf.float32)
    img = tf.expand_dims(img, axis=0)
    return img

def save_image(tensor, output_path):
    img = tensor[0].numpy()
    img = np.clip(img, 0, 1)
    img = (img * 255).astype(np.uint8)
    Image.fromarray(img).save(output_path)

def run_style_transfer(content_path, style_path, output_path):
    # Load and preprocess
    content_image = load_image(content_path)
    style_image = load_image(style_path)

    # Stylize!
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]

    # Save result
    save_image(stylized_image, output_path)

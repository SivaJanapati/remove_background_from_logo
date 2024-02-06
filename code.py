from PIL import Image

def approximate_background_removal(image_path):
  """Approximates background removal using basic image processing techniques."""

  image = Image.open(image_path)
  pixels = image.load()
  width, height = image.size

  # Approximate background detection (modify for specific images):
  background_color = pixels[0, 0]  # Assuming top-left corner represents background
  threshold = 20  # Adjust as needed

  # Iterate through pixels, replacing background-like pixels with transparency
  for x in range(width):
    for y in range(height):
      current_pixel = pixels[x, y]
      if all(abs(channel - background_channel) <= threshold for channel, background_channel in zip(current_pixel, background_color)):
        pixels[x, y] = (0, 0, 0, 0)  # Set alpha to 0 for transparency

  image.save("image_without_background.png")

# Example usage:
approximate_background_removal("nameLogo.png")
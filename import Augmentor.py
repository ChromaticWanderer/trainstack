import Augmentor

# Create a pipeline for your image directory
p = Augmentor.Pipeline(r"C:\Users\jared\Documents\Files\BarcelosStack")

# Define the augmentation operations and probabilities

# Rotate images randomly between -5 and 5 degrees
p.rotate(probability=0.7, max_left_rotation=5, max_right_rotation=5)

# Add random brightness changes (20% brighter or darker)
p.random_brightness(probability=0.5, min_factor=0.8, max_factor=1.2)

# Add random contrast changes
p.random_contrast(probability=0.5, min_factor=0.8, max_factor=1.2)

# Add random zoom, zooming into 90% of the image area
p.zoom_random(probability=0.5, percentage_area=0.9)

# Add slight Gaussian distortion to simulate noise, but at low magnitude
p.gaussian_distortion(probability=0.5, grid_width=4, grid_height=4, magnitude=1, corner="bell", method="in")

# Output the augmented images
p.sample(100)  # Generates 100 augmented images
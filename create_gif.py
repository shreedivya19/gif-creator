from PIL import Image
import os

folder_path = '/Users/shreedivya/Documents/gif_images/'
output_path = '/Users/shreedivya/Documents/animated.gif'

# Get image files from folder
image_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
image_paths = [os.path.join(folder_path, f) for f in image_files]

# Check if enough images
if len(image_paths) < 2:
    print("❌ Not enough images to create a GIF. Add at least 2.")
    exit()

# Resize and collect images
images = []
for path in image_paths:
    try:
        img = Image.open(path).resize((300, 300))
        images.append(img)
    except Exception as e:
        print(f"⚠️ Skipped {path}: {e}")

# Check if valid images were added
if len(images) < 2:
    print("❌ Could not read enough valid images. Try with new ones.")
    exit()

# Save GIF
images[0].save(
    output_path,
    save_all=True,
    append_images=images[1:],
    duration=500,
    loop=0
)
print(f"✅ GIF created successfully at: {output_path}")



import os
from os.path import join
from PIL import Image
import pillow_heif

# Enable support for HEIF in Pillow
pillow_heif.register_heif_opener()

Global_path = r'C:\Users\joshu\OneDrive\Documents\LocalFiles'
winnie = "Unsorted lil bean"
colton = "unsorted colton"

# Get lists of files in the directories
w = os.listdir(join(Global_path, winnie))
c = os.listdir(join(Global_path, colton))

# Process files from both directories
for wPic, cPic in zip(w, c):
    # Handle winnie directory
    img_path = wPic.split(".")
    if len(img_path) < 2 or img_path[1].upper() == "AAE":  # Skip non-image or AAE files
        continue
    
    wPic_full = join(Global_path, winnie, wPic)
    output_path_w = join(Global_path, winnie, img_path[0] + ".jpg")
    
    try:
        with Image.open(wPic_full) as img:
            img.convert("RGB").save(output_path_w, "JPEG")
        print(f"Converted {wPic} to {output_path_w}")
    except Exception as e:
        print(f"Error processing {wPic}: {e}")
"""
Script to create placeholder images for existing watches
Run this after migrating to add sample images
"""

import os
import django
from PIL import Image, ImageDraw, ImageFont
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'watchhouse_project.settings')
django.setup()

from watches.models import Watch, WatchImage
from django.core.files.base import ContentFile
from io import BytesIO

def create_placeholder_image(watch_name, size=(800, 800), color=None):
    """Create a placeholder image for a watch"""
    if color is None:
        # Generate random dark colors
        colors = [
            (25, 30, 48),   # Dark blue
            (20, 25, 35),   # Darker blue
            (30, 25, 40),   # Purple tint
            (25, 35, 30),   # Green tint
            (35, 25, 25),   # Red tint
        ]
        color = random.choice(colors)
    
    # Create image
    img = Image.new('RGB', size, color=color)
    draw = ImageDraw.Draw(img)
    
    # Add gradient effect
    for i in range(size[1]):
        opacity = int(255 * (i / size[1]) * 0.3)
        draw.line([(0, i), (size[0], i)], fill=(color[0] + opacity//3, color[1] + opacity//3, color[2] + opacity//3))
    
    # Add watch emoji or text
    try:
        # Try to add text
        font_size = 200
        text = "⌚"
        
        # Draw text shadow
        shadow_offset = 5
        draw.text((size[0]//2 - 100 + shadow_offset, size[1]//2 - 100 + shadow_offset), 
                 text, fill=(0, 0, 0, 128))
        
        # Draw main text
        draw.text((size[0]//2 - 100, size[1]//2 - 100), text, fill=(255, 255, 255, 200))
        
    except Exception as e:
        print(f"Could not add text: {e}")
    
    # Save to bytes
    img_io = BytesIO()
    img.save(img_io, format='PNG', quality=95)
    img_io.seek(0)
    
    return img_io

# Get all watches without images
watches_without_images = Watch.objects.filter(images__isnull=True).distinct()

if watches_without_images.count() == 0:
    print("All watches already have images!")
else:
    print(f"Found {watches_without_images.count()} watches without images")
    
    for watch in watches_without_images:
        print(f"\nProcessing: {watch.brand} - {watch.name}")
        
        # Create 2-3 placeholder images per watch
        num_images = random.randint(2, 3)
        
        for i in range(num_images):
            img_data = create_placeholder_image(watch.name)
            
            # Create WatchImage
            watch_image = WatchImage(
                watch=watch,
                order=i
            )
            
            # Save image file
            filename = f"{watch.brand}_{watch.name}_{i+1}.png".replace(' ', '_')
            watch_image.image.save(filename, ContentFile(img_data.read()), save=True)
            
            print(f"  ✓ Created image {i+1}/{num_images}")

print("\n✅ All done! Placeholder images created.")
print("\nNote: You should now upload real watch images through the admin panel.")
print("Go to: http://127.0.0.1:8000/admin/watches/watch/")

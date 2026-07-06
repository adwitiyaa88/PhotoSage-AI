from services.apple_photos import get_original_photos

photos = get_original_photos()

print(f"\nFound {len(photos)} photos.\n")

for photo in photos[:20]:
    print(photo)
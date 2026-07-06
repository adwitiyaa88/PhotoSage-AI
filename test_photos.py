from services.services.photos_service import get_photos

try:
    photos = get_photos()

    print(f"\nFound {len(photos)} photos\n")

    for photo in photos[:5]:
        print(photo["filename"])

except Exception as e:
    import traceback
    traceback.print_exc()
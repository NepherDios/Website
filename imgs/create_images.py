import os
import shutil
import subprocess

BASE_DIR = "images"  # root folder where everything goes

def create_product_folder(product_name):
    folder = os.path.join(BASE_DIR, product_name)

    os.makedirs(folder, exist_ok=True)
    print(f"Created: {folder}")

    return folder


def add_images(folder, image_paths):
    for i, img_path in enumerate(image_paths, start=1):
        ext = os.path.splitext(img_path)[1] or ".jpg"
        dest = os.path.join(folder, f"{i}{ext}")

        shutil.copy(img_path, dest)
        print(f"Added: {dest}")

def git_push():
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "auto: add product images"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("GitHub updated ✔")
    except Exception as e:
        print("Git error:", e)

def main():
    print("=== Image Folder Creator ===")

    product = input("Product name (folder): ").strip().lower().replace(" ", "_")

    folder = create_product_folder(product)

    print("\nNow paste image paths (one per line). Empty line to finish:")

    images = []
    while True:
        path = input("> ").strip()
        if path == "":
            break
        if os.path.exists(path):
            images.append(path)
        else:
            print("File not found:", path)

    add_images(folder, images)
    git_push()

    print("\nDONE ✔")


if __name__ == "__main__":
    main()

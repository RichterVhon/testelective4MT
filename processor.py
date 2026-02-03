import cv2
import os

def process_images():
    # 1. Automatically detect image files in input directory
    input_dir = 'input/'
    output_dir = 'output/'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith((".jpg", ".png", ".jpeg")):
            img = cv2.imread(os.path.join(input_dir, filename))
            
            # 2. Chained Processing (Requirement #2)
            # Technique A: Grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Technique B: Edge Detection
            #edges = cv2.Canny(gray, 100, 200)
            edges = None #intentional error for testing

            # 3. Save processed images (Requirement #3)
            cv2.imwrite(os.path.join(output_dir, f"processed_{filename}"), edges)
            print(f"Successfully processed {filename}")

if __name__ == "__main__":
    process_images()
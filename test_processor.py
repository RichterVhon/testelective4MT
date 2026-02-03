import cv2
import os
import numpy as np
import pytest

def test_edge_quality():
    """Requirement #2: Check if Canny worked on a real image."""
    output_folder = "output"
    
    # Get all files, but EXCLUDE .gitkeep
    files = [f for f in os.listdir(output_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    if not files:
        pytest.fail(f"No image files found in {output_folder}. Found: {os.listdir(output_folder)}")
    
    img_path = os.path.join(output_folder, files[0])
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    
    # This is where your error was happening
    assert img is not None, f"OpenCV could not read the image at {img_path}"
    
    # Check if there's actual data (not just a black square)
    assert np.mean(img) > 0, "Image is completely black. Edge detection might have failed."
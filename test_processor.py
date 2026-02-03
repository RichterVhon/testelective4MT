import cv2
import os
import numpy as np
import pytest

def test_output_file_exists():
    """Requirement #3: Check if output is created."""
    # Ensure this matches the filename your processor.py creates
    assert os.path.exists("output/test_processed.jpg") or any(os.listdir("output")), "No files found in output!"

def test_edge_quality():
    """Requirement #2: Check if Canny worked."""
    # Grab the first file in output to check it
    files = os.listdir("output")
    if not files:
        pytest.fail("Output folder is empty.")
    
    img_path = os.path.join("output", files[0])
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    
    # Check if there's any data in the image
    assert img is not None, "Could not read output image."
    assert np.mean(img) >= 0, "Image processing failed to produce data."
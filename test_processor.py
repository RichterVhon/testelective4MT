import cv2
import os
import numpy as np
import pytest

def test_edge_quality():
    """Checks if the edge detection actually produced edges (white pixels)."""
    output_path = "output/test_processed.jpg" # Adjust to your filename
    
    if os.path.exists(output_path):
        img = cv2.imread(output_path, cv2.IMREAD_GRAYSCALE)
        # Requirement #2 & #3 check:
        # If Canny worked, there should be at least some white pixels (edges)
        white_pixels = np.sum(img == 255)
        assert white_pixels > 0, "Edge detection resulted in a blank image!"
    else:
        pytest.fail("Output file was never created.")
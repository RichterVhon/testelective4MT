import os
from processor import process_images

def test_pipeline_output():
    # Run the processor
    process_images()
    
    # Check if the output folder exists and has at least one file
    assert os.path.exists('output/')
    assert len(os.listdir('output/')) > 0
    print("Test Passed: Output generated!")
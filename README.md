# Repository Topic:
Topic Name: Image-Processing-Experiments
## Welcome!
Dive into the world of image processing with this collection of fun experiments! This repository demonstrates various techniques to transform and enhance images using Python. Whether you're a hobbyist, a learner, or a developer, you'll find inspiring examples and code to explore.
## Description:
"Explore a collection of fun and educational image processing experiments! This repository showcases various techniques to transform and enhance images, including adjusting intensity levels, applying smoothing filters, rotating images, and simulating resolution changes. Built with Python using OpenCV, NumPy, and Matplotlib, it includes sample code and visually stunning results. Perfect for hobbyists, students, or anyone curious about image manipulation—dive in, experiment, and contribute your own ideas!"
## Directory Structure
<pre>
Image-Processing-Experiments/
│
├── images/                  # Folder for all images
│   ├── original/            # Original image(s)
│   │   └── test4.jpg        # Renamed original image
│   ├── intensity/           # Intensity level outputs
│   │   ├── reduced_intensity_2.jpg
│   │   ├── reduced_intensity_4.jpg
│   │   ├── reduced_intensity_8.jpg
│   │   ├── reduced_intensity_16.jpg
│   │   ├── reduced_intensity_32.jpg
│   │   ├── reduced_intensity_64.jpg
│   │   ├── reduced_intensity_128.jpg
│   │   └── reduced_intensity_256.jpg
│   ├── averageing/           # Spatial averaging outputs
│   │   ├── averaged_3x3.jpg
│   │   ├── averaged_10x10.jpg
│   │   └── averaged_20x20.jpg
│   ├── rotation/            # Rotation outputs
│   │   ├── rotated_45_degrees.jpg
│   │   └── rotated_90_degrees.jpg
│   └── resolution/          # Resolution reduction outputs
│       ├── reduced_resolution_3x3.jpg
│       ├── reduced_resolution_5x5.jpg
│       └── reduced_resolution_7x7.jpg
│
├── code/                    # Folder for source code
│   └── image_processor.py   # Renamed Python script
│── test2                    # test original images
|── test3                    # test original images
└── README.md                # Main readme file
  </pre>


## Features
- **Intensity Adjustment**: Modify the number of intensity levels for unique visual effects.
- **Smoothing Filters**: Apply 3x3, 10x10, and 20x20 averaging to smooth images.
- **Image Rotation**: Rotate images by 45 and 90 degrees for creative angles.
- **Resolution Changes**: Simulate lower resolutions with 3x3, 5x5, and 7x7 block averaging.

## Files and Folders
- `images/`: Contains original and processed images organized by technique.
- `code/`: Includes the Python script (`image_processor.py`) with all implementations.

## How to Get Started
1. Clone the repository: `git clone https://github.com/ThisaruDissanayake/Image-Processing-Experiments.git`
2. Install dependencies: `pip install opencv-python numpy matplotlib`
3. Update the image path in `code/image_processor.py` to your local image.
4. Run the script: `python code/image_processor.py`

## Explore the Results
Check the `images/` folder to see the transformations applied to the sample test4 image!

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to reduce intensity levels
def reduce_intensity_levels(image, levels):
   
    if not (levels & (levels - 1) == 0 and levels != 0): 
        raise ValueError("Number of intensity levels must be a power of 2.")
    
   
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    factor = 256 // levels
    reduced_image = (image // factor) * factor
    return reduced_image

# Function to perform spatial averaging
def spatial_average(image, kernel_size):
   
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    
    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size * kernel_size)
    averaged_image = cv2.filter2D(image, -1, kernel)
    return averaged_image

# Function to rotate image
def rotate_image(image, angle):
   
    
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, M, (w, h))
    return rotated_image

# Function to reduce spatial resolution by block averaging
def reduce_spatial_resolution(image, block_size):
   
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    h, w = image.shape
    new_h, new_w = h // block_size, w // block_size
    reduced_image = np.zeros((new_h * block_size, new_w * block_size), dtype=np.uint8)
    
    # Process each block
    for i in range(0, h - block_size + 1, block_size):
        for j in range(0, w - block_size + 1, block_size):        
            block = image[i:i+block_size, j:j+block_size]          
            avg = np.mean(block).astype(np.uint8)
            reduced_image[i:i+block_size, j:j+block_size] = avg
    
    return reduced_image

def main():
    # Load an image 
    image = cv2.imread('D:/7 Semester/computer vision/Take Home1/test4.jpg')
    if image is None:
        print("Error: Could not load the image.")
        return
    
    
    intensity_levels = [2, 4, 8,16,32,64,128,256]  # Example: powers of 2
    for levels in intensity_levels:
        reduced_intensity = reduce_intensity_levels(image, levels)
        cv2.imwrite(f'reduced_intensity_{levels}.jpg', reduced_intensity)
        plt.imshow(reduced_intensity, cmap='gray')
        plt.title(f'Intensity Levels: {levels}')
        plt.show()
    
    
    kernel_sizes = [3, 10, 20]
    for size in kernel_sizes:
        averaged_image = spatial_average(image, size)
        cv2.imwrite(f'averaged_{size}x{size}.jpg', averaged_image)
        plt.imshow(averaged_image, cmap='gray')
        plt.title(f'Spatial Average: {size}x{size}')
        plt.show()
    
    
    angles = [45, 90]
    for angle in angles:
        rotated_image = rotate_image(image, angle)
        cv2.imwrite(f'rotated_{angle}_degrees.jpg', rotated_image)
        plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
        plt.title(f'Rotation: {angle} degrees')
        plt.show()
    
    
    block_sizes = [3, 5, 7]
    for size in block_sizes:
        reduced_resolution = reduce_spatial_resolution(image, size)
        cv2.imwrite(f'reduced_resolution_{size}x{size}.jpg', reduced_resolution)
        plt.imshow(reduced_resolution, cmap='gray')
        plt.title(f'Reduced Resolution: {size}x{size} blocks')
        plt.show()

if __name__ == "__main__":
    main()
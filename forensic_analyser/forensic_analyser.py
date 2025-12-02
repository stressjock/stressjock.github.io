import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# --- Configuration ---
INPUT_FILENAME = 'source.png' 
# IMPORTANT: Change 'source.png' to the name of the image you want to analyze.
# Example: INPUT_FILENAME = 'my_suspicious_photo.jpg'
# ---------------------

def analyze_fft(image_path, input_name):
    """
    Performs the full FFT analysis and saves the 3-panel figure (CHECK_source.png).
    This function uses a standard residual for plotting with Matplotlib's auto-scaling.
    """
    print(f"--- 1. Performing FFT Analysis on: {input_name} ---")

    # 1. Load and Convert to Grayscale
    img = cv2.imread(image_path, 0)
    
    if img is None:
        print(f"Error: Could not load image at {image_path}. Check the path.")
        return False

    # Convert the image to float32 for accurate subtraction
    img_float = np.float32(img)

    # 2. Extract the Noise Residual (High-Pass Filter)
    blurred = cv2.GaussianBlur(img_float, (5, 5), 0)
    residual = img_float - blurred # Standard residual subtraction
    
    # 3. Compute the 2D Fast Fourier Transform (FFT) of the Residual
    f = np.fft.fft2(residual)
    fshift = np.fft.fftshift(f) # Shift zero-frequency to the center

    # 4. Compute the Magnitude Spectrum (log scale for visualization)
    magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)
    
    # 5. Plot and Save the Results
    output_filename = f"CHECK_{os.path.basename(image_path).split('.')[0]}.png"
    plt.figure(figsize=(15, 6))

    # Plot 1: Original Image
    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap='gray')
    plt.title(f'Original Image ({input_name})')
    plt.axis('off')

    # Plot 2: Noise Residual
    plt.subplot(1, 3, 2)
    # Use Matplotlib to display the residual. The vmin/vmax range helps center the grayscale.
    plt.imshow(residual, cmap='gray', vmin=np.min(residual), vmax=np.max(residual) * 0.5) 
    plt.title('Noise Residual')
    plt.axis('off')

    # Plot 3: FFT Magnitude Spectrum
    plt.subplot(1, 3, 3)
    plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('FFT Magnitude Spectrum')
    plt.axis('off')

    plt.tight_layout()
    
    try:
        plt.savefig(output_filename, dpi=300, bbox_inches='tight')
        print(f"✅ FFT Plot saved to: {output_filename}")
        return True
    except Exception as e:
        print(f"❌ Error saving FFT plot file: {e}")
        return False


def save_high_contrast_residual(image_path, blur_kernel_size=5):
    """
    Extracts the high-contrast Noise Residual Map and saves it as a standalone image.
    This function uses normalization to ensure the noise is visible as white on black.
    """
    print(f"\n--- 2. Extracting High-Contrast Residual Map ---")

    try:
        # 1. Load the original image (in grayscale)
        original_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if original_img is None:
            print("Error: Could not read image.")
            return False

        # 2. Blur the image
        blurred_img = cv2.GaussianBlur(original_img, (blur_kernel_size, blur_kernel_size), 0)

        # 3. Calculate the Noise Residual (using absolute difference for high contrast)
        residual_map = np.abs(np.float32(original_img) - np.float32(blurred_img))

        # 4. Normalize and scale for visualization (0 to 255)
        # This is the key step to make the faint noise visible (white spots on black background)
        residual_map = np.uint8(cv2.normalize(residual_map, None, 0, 255, cv2.NORM_MINMAX))

        # 5. Save the Residual Map to a new file
        output_path = f"RESIDUAL_{os.path.basename(image_path).split('.')[0]}.png"
        cv2.imwrite(output_path, residual_map)

        print(f"✅ High-Contrast Residual Map saved to: {output_path}")
        return True

    except Exception as e:
        print(f"An unexpected error occurred during residual extraction: {e}")
        return False


# ----------------------------------------------------------------------
# Main Execution Block
# ----------------------------------------------------------------------

if __name__ == "__main__":
    if not os.path.exists(INPUT_FILENAME):
        print(f"\n❌ Error: Input file not found: '{INPUT_FILENAME}'.")
        print("Please ensure the image file is in the same folder and the 'INPUT_FILENAME' variable is correct.")
    else:
        print("==============================================")
        print(f"STARTING ANALYSIS for: {INPUT_FILENAME}")
        print("==============================================")
        
        # Run the two distinct analyses
        fft_success = analyze_fft(INPUT_FILENAME, INPUT_FILENAME)
        residual_success = save_high_contrast_residual(INPUT_FILENAME)

        print("\n==============================================")
        if fft_success and residual_success:
            print("✨ ALL ANALYSES COMPLETE ✨")
        else:
            print("🚨 ANALYSIS COMPLETED WITH ERRORS 🚨")
        print("==============================================")
        
        print("\n--- NEXT STEPS ---")
        print("1. Review the output files generated in this folder.")
        print("2. Consult the Interpretation Guide in your documentation for forensic conclusions.")
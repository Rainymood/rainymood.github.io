"""
# With mask (fills white areas only)
python generate_thumbnail.py --mask default-thumbnail.png --style both

# Standalone gradient (no mask)
python generate_thumbnail.py --style horizontal

# Custom output name
python generate_thumbnail.py --mask default-thumbnail.png --style diagonal --output my_thumbnail.png
"""
import numpy as np
from PIL import Image, ImageDraw
import colorsys
import argparse

def create_neon_gradient_stripes(width=1280, height=720, num_stripes=12):
    """
    Create an abstract neon gradient stripes background for YouTube thumbnail.
    
    Args:
        width: Image width in pixels (default 1280 for YouTube)
        height: Image height in pixels (default 720 for YouTube)
        num_stripes: Number of diagonal stripes
    """
    # Create image
    img = Image.new('RGB', (width, height), color='black')
    draw = ImageDraw.Draw(img)
    
    # Generate vibrant neon colors using HSV color space
    neon_colors = []
    for i in range(num_stripes):
        # Use full saturation and high value for neon effect
        hue = i / num_stripes
        rgb = colorsys.hsv_to_rgb(hue, 0.9, 1.0)
        neon_colors.append(tuple(int(c * 255) for c in rgb))
    
    # Calculate stripe width and angle
    diagonal = np.sqrt(width**2 + height**2)
    stripe_width = diagonal / num_stripes
    
    # Draw diagonal stripes
    for i in range(num_stripes * 2):
        color_idx = i % num_stripes
        
        # Create gradient within each stripe
        for j in range(int(stripe_width)):
            # Calculate gradient factor
            gradient_factor = j / stripe_width
            
            # Blend between current color and next color
            next_color_idx = (color_idx + 1) % num_stripes
            current_color = neon_colors[color_idx]
            next_color = neon_colors[next_color_idx]
            
            # Interpolate colors
            blended_color = tuple(
                int(current_color[k] * (1 - gradient_factor) + next_color[k] * gradient_factor)
                for k in range(3)
            )
            
            # Calculate stripe position (diagonal)
            offset = i * stripe_width + j - diagonal
            
            # Draw diagonal line
            x1 = offset
            y1 = 0
            x2 = offset + height * 1.5
            y2 = height
            
            draw.line([(x1, y1), (x2, y2)], fill=blended_color, width=2)
    
    return img

def create_smooth_gradient_stripes(width=1280, height=720):
    """
    Create smooth horizontal gradient stripes with neon colors.
    """
    img = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Define neon color palette
    neon_colors = [
        (255, 0, 128),    # Neon pink
        (0, 255, 255),    # Cyan
        (255, 0, 255),    # Magenta
        (0, 255, 0),      # Neon green
        (255, 255, 0),    # Yellow
        (128, 0, 255),    # Purple
        (255, 128, 0),    # Orange
    ]
    
    num_colors = len(neon_colors)
    stripe_height = height / num_colors
    
    for i in range(height):
        # Determine which color transition we're in
        color_idx = int(i / stripe_height)
        next_color_idx = (color_idx + 1) % num_colors
        
        # Calculate position within the stripe (0 to 1)
        position = (i % stripe_height) / stripe_height
        
        # Get current and next colors
        c1 = np.array(neon_colors[color_idx])
        c2 = np.array(neon_colors[next_color_idx])
        
        # Smooth interpolation using sine wave for more organic gradient
        smooth_position = (np.sin((position - 0.5) * np.pi) + 1) / 2
        
        # Interpolate
        color = c1 * (1 - smooth_position) + c2 * smooth_position
        
        # Add horizontal gradient variation for more depth
        for j in range(width):
            horizontal_factor = j / width
            brightness = 0.8 + 0.2 * np.sin(horizontal_factor * np.pi * 2)
            img[i, j] = (color * brightness).astype(np.uint8)
    
    return Image.fromarray(img)

def apply_gradient_to_mask(mask_image_path, gradient_image, white_threshold=240):
    """
    Apply gradient only to white areas of the mask image.
    
    Args:
        mask_image_path: Path to the mask/template image
        gradient_image: PIL Image with the gradient to apply
        white_threshold: RGB threshold to consider a pixel as white (default 240)
    
    Returns:
        PIL Image with gradient applied to white areas
    """
    # Load the mask image
    mask = Image.open(mask_image_path).convert('RGB')
    
    # Ensure gradient matches mask dimensions
    if gradient_image.size != mask.size:
        gradient_image = gradient_image.resize(mask.size, Image.Resampling.LANCZOS)
    
    # Convert to numpy arrays
    mask_array = np.array(mask)
    gradient_array = np.array(gradient_image)
    
    # Create a mask for white pixels (where all RGB values are above threshold)
    white_mask = np.all(mask_array >= white_threshold, axis=2)
    
    # Create output image starting with the original mask
    output_array = mask_array.copy()
    
    # Replace white pixels with gradient
    output_array[white_mask] = gradient_array[white_mask]
    
    return Image.fromarray(output_array)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate neon gradient stripe thumbnails')
    parser.add_argument('--mask', type=str, default=None,
                       help='Path to mask/template image (will fill white areas with gradient)')
    parser.add_argument('--style', type=str, default='horizontal', choices=['horizontal', 'diagonal', 'both'],
                       help='Gradient style: horizontal, diagonal, or both')
    parser.add_argument('--output', type=str, default='thumbnail.png',
                       help='Output filename')
    
    args = parser.parse_args()
    
    if args.mask:
        # Load mask to get dimensions
        mask_img = Image.open(args.mask)
        width, height = mask_img.size
        print(f"Using mask image: {args.mask} ({width}x{height})")
    else:
        width, height = 1280, 720
        print(f"Generating standalone thumbnail ({width}x{height})")
    
    if args.style in ['horizontal', 'both']:
        print("Generating horizontal gradient stripes...")
        thumbnail = create_smooth_gradient_stripes(width=width, height=height)
        
        if args.mask:
            print("Applying gradient to white areas of mask...")
            thumbnail = apply_gradient_to_mask(args.mask, thumbnail)
        
        output_path = args.output if args.style == 'horizontal' else 'thumbnail_horizontal.png'
        thumbnail.save(output_path, quality=95)
        print(f"Thumbnail saved to: {output_path}")
    
    if args.style in ['diagonal', 'both']:
        print("Generating diagonal gradient stripes...")
        diagonal_thumbnail = create_neon_gradient_stripes(width=width, height=height, num_stripes=15)
        
        if args.mask:
            print("Applying gradient to white areas of mask...")
            diagonal_thumbnail = apply_gradient_to_mask(args.mask, diagonal_thumbnail)
        
        diagonal_output_path = 'thumbnail_diagonal.png' if args.style == 'both' else args.output
        diagonal_thumbnail.save(diagonal_output_path, quality=95)
        print(f"Diagonal variant saved to: {diagonal_output_path}")

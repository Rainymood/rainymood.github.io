"""
Generate a thumbnail by fetching an image from DuckDuckGo based on blog post content
and compositing it into the white areas of the default thumbnail.

Usage:
    python generate_thumbnail.py --post ../../_posts/2026-03-31-how-to-decide.md --mask default-thumbnail.png
    python generate_thumbnail.py --post ../../_posts/2026-03-31-how-to-decide.md --mask default-thumbnail.png --query "decision making dice"

Requirements:
    pip install pillow numpy requests duckduckgo-search
"""
import numpy as np
from PIL import Image
import argparse
import re
import requests
from io import BytesIO
import os


def extract_blog_title_and_content(post_path):
    """
    Extract title and main content from a markdown blog post.
    
    Args:
        post_path: Path to the markdown blog post
        
    Returns:
        tuple: (title, content_snippet)
    """
    with open(post_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title from frontmatter
    title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else ""
    
    # Extract main content (after frontmatter)
    content_parts = content.split('---', 2)
    if len(content_parts) >= 3:
        main_content = content_parts[2].strip()
        # Get first few sentences, remove markdown
        main_content = re.sub(r'[#*`\[\]]', '', main_content)
        main_content = ' '.join(main_content.split()[:50])  # First 50 words
    else:
        main_content = ""
    
    return title, main_content


def fetch_image_from_duckduckgo(query, max_results=5):
    """
    Fetch an image from DuckDuckGo (free, no API key required).
    
    Args:
        query: Search query string
        max_results: Number of results to try (default 5)
        
    Returns:
        PIL Image or None if fetch fails
    """
    try:
        from duckduckgo_search import DDGS
        
        print(f"Searching DuckDuckGo for: {query}")
        
        with DDGS() as ddgs:
            results = list(ddgs.images(query, max_results=max_results))
            
            if not results:
                print("No images found in search results.")
                return create_placeholder_image()
            
            # Try to fetch images until one works
            for i, result in enumerate(results):
                try:
                    image_url = result.get('image')
                    if not image_url:
                        continue
                        
                    print(f"Attempting to fetch image {i+1}/{len(results)}: {image_url[:60]}...")
                    
                    img_response = requests.get(image_url, timeout=10, headers={
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                    })
                    img_response.raise_for_status()
                    
                    img = Image.open(BytesIO(img_response.content))
                    print(f"✓ Successfully fetched image ({img.size[0]}x{img.size[1]})")
                    return img.convert('RGB')
                    
                except Exception as e:
                    print(f"  Failed to fetch image {i+1}: {e}")
                    continue
            
            print("All image fetches failed, using placeholder.")
            return create_placeholder_image()
            
    except ImportError:
        print("Error: duckduckgo-search not installed. Install with: pip install duckduckgo-search")
        return create_placeholder_image()
    except Exception as e:
        print(f"Error searching DuckDuckGo: {e}")
        return create_placeholder_image()


def create_placeholder_image():
    """
    Create a placeholder gradient image when Google fetch fails.
    """
    width, height = 1280, 720
    img = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Create a simple gradient
    for i in range(height):
        for j in range(width):
            img[i, j] = [
                int(255 * (i / height)),
                int(255 * (j / width)),
                int(128)
            ]
    
    return Image.fromarray(img)


def apply_image_to_white_areas(mask_image_path, source_image, white_threshold=240):
    """
    Replace white areas in the mask with the source image.
    
    Args:
        mask_image_path: Path to the mask/template image
        source_image: PIL Image to composite into white areas
        white_threshold: RGB threshold to consider a pixel as white (default 240)
    
    Returns:
        PIL Image with source image applied to white areas
    """
    # Load the mask image
    mask = Image.open(mask_image_path).convert('RGB')
    
    # Ensure source image matches mask dimensions
    if source_image.size != mask.size:
        source_image = source_image.resize(mask.size, Image.Resampling.LANCZOS)
    
    # Convert to numpy arrays
    mask_array = np.array(mask)
    source_array = np.array(source_image)
    
    # Create a mask for white pixels (where all RGB values are above threshold)
    white_mask = np.all(mask_array >= white_threshold, axis=2)
    
    # Create output image starting with the original mask
    output_array = mask_array.copy()
    
    # Replace white pixels with source image
    output_array[white_mask] = source_array[white_mask]
    
    return Image.fromarray(output_array)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate thumbnail with Google image in white areas')
    parser.add_argument('--post', type=str, required=True,
                       help='Path to the blog post markdown file')
    parser.add_argument('--mask', type=str, required=True,
                       help='Path to mask/template image (will fill white areas)')
    parser.add_argument('--query', type=str, default=None,
                       help='Custom search query (if not provided, will use blog title)')
    parser.add_argument('--output', type=str, default='thumbnail.png',
                       help='Output filename (default: thumbnail.png)')
    parser.add_argument('--max-results', type=int, default=5,
                       help='Number of image results to try (default: 5)')
    
    args = parser.parse_args()
    
    # Extract blog post information
    print(f"Reading blog post: {args.post}")
    title, content = extract_blog_title_and_content(args.post)
    print(f"Blog title: {title}")
    
    # Determine search query
    search_query = args.query if args.query else title
    print(f"Search query: {search_query}")
    
    # Fetch image from DuckDuckGo (or create placeholder)
    print("Fetching image...")
    fetched_image = fetch_image_from_duckduckgo(
        search_query,
        max_results=args.max_results
    )
    
    if fetched_image is None:
        print("Failed to fetch image, using placeholder")
        fetched_image = create_placeholder_image()
    
    # Apply image to white areas of mask
    print(f"Applying image to white areas of mask: {args.mask}")
    thumbnail = apply_image_to_white_areas(args.mask, fetched_image)
    
    # Save output
    thumbnail.save(args.output, quality=95)
    print(f"\n✓ Thumbnail saved to: {args.output}")

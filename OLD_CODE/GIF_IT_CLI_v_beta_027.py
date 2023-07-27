import os
import argparse
import subprocess
from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm
import numpy as np
import imageio

#Set class for dither and resample
class DitherAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values.split(','))

class ResampleAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if isinstance(values, list):
            setattr(namespace, self.dest, values)
        else:
            setattr(namespace, self.dest, values.split(','))

def create_gif_with_dithering(args, watermark_text):
    # Get a list of image file names in the folder
    image_files = [f for f in os.listdir(args.folder_path) if os.path.isfile(os.path.join(args.folder_path, f))]

    # Sort the image files alphabetically or by date if specified
    if args.date:
        image_files.sort(key=lambda x: os.path.getmtime(os.path.join(args.folder_path, x)))
    else:
        image_files.sort()

    # Create a list to store the images with different dithering options
    images = []

    # Open and process each image with a progress bar
    for image_file in tqdm(image_files, desc='Processing images'):

        # Open the image
        image_path = os.path.join(args.folder_path, image_file)
        image = Image.open(image_path)

        # Create a copy of the image to work on
        image_copy = image.copy()

        # Convert the image to RGBA mode if it's not already
        if image_copy.mode != 'RGBA':
            image_copy = image_copy.convert('RGBA')

        # Create a new image with alpha transparency for the watermark
        watermark_image = Image.new('RGBA', image_copy.size, (0, 0, 0, 0))

        # Create a drawing context
        draw = ImageDraw.Draw(watermark_image)

        # Define the text and font properties
        text = watermark_text
        font = ImageFont.truetype('C:/Windows/Fonts/impact.ttf', args.size)
        text_color = (255, 255, 255, 185)  # RGBA color with transparency
        outline_color = (0, 0, 0, 255)  # RGBA black color for outline

        # Calculate the position to place the watermark (centered on top)
        bbox = draw.textbbox((0, 0), text, font=font)
        if args.location == 'TOP':
            watermark_y_offset = 0
        elif args.location == 'CENTER':
            watermark_y_offset = (image_copy.height - bbox[3]) // 2
        else:  # args.location == 'BOTTOM'
            watermark_y_offset = image_copy.height - bbox[3] - 10
        watermark_position = ((image_copy.width - bbox[2]) // 2, watermark_y_offset)
        
        # Draw the text multiple times for black outlines
        for adj in [-2, -1, 0, 1, 2]:  # Adjusting pixel positions for outline
            # Draw the text on the watermark image for outline
            draw.text((watermark_position[0]+adj, watermark_position[1]), text, font=font, fill=outline_color)
            draw.text((watermark_position[0], watermark_position[1]+adj), text, font=font, fill=outline_color)
            draw.text((watermark_position[0]+adj, watermark_position[1]+adj), text, font=font, fill=outline_color)

        # Draw the original text on top of outlines
        draw.text(watermark_position, text, font=font, fill=text_color)

        # Composite the watermark image onto the original image
        image_copy = Image.alpha_composite(image_copy, watermark_image)

        # Resample the image if specified
        for scale in args.resample:
            # Calculate the new size based on the scale factor
            new_size = (int(image.width * float(scale)), int(image.height * float(scale)))
            # Resample the image
            image_copy = image_copy.resize(new_size, resample=Image.BOX)

        # Apply dithering for each option
        if args.dither:
            for dither_option in args.dither:
                # Copy the image to avoid modifying the original
                dithered_image = image_copy.copy()  # Changed from image.copy()
                # Map the dither option string to the corresponding PIL constant
                dither_constant = getattr(Image, dither_option.upper())
                # Apply the dithering option
                dithered_image = dithered_image.convert('P', dither=dither_constant)
                # Limit the number of colors if the -colors option is provided
                if args.colors is not None:
                    dithered_image = dithered_image.quantize(colors=args.colors)
                # Convert the image back to 'RGBA' mode
                dithered_image = dithered_image.convert('RGBA')
                # Append the image with applied dithering and color limit to the list
                images.append(dithered_image)
        else:
            # If no dither option is provided, add the original image_copy to the list
            images.append(image_copy)
    print('Processing GIF now...')        

    # Determine the output GIF path
    gif_path = os.path.join(args.folder_path, args.output_name + '.gif')

    # Create a list to store the dissolved frames
    dissolved_frames = []

    # Iterate over the frames and add dissolve effect
    for i, image in enumerate(images):
        dissolved_frames.append(image)
        # Add dissolve effect for all frames except the last one
    if i < len(images) - 1 and args.dissolve is not None:
        dissolve_frames = args.dissolve  # Number of dissolve frames defined directly
        # Apply alpha blending to the next frames
        for j in range(dissolve_frames):
            # Calculate the alpha blending ratio
            alpha = j / dissolve_frames
            # Blend images[i] and images[i+1] according to alpha
            blend = Image.blend(images[i], images[i+1], alpha)
            # Append the blended image to dissolved_frames
            dissolved_frames.append(blend)

    # Save the dissolved frames as a GIF file
    dissolved_frames[0].save(gif_path, save_all=True, append_images=dissolved_frames[1:], duration=args.speed, loop=0, transparency=0)

    # Open the GIF file immediately with -open flag
    if args.open:
        if os.name == 'nt':  # Windows
            os.startfile(gif_path)
        elif os.name == 'posix':  # macOS and Linux
            subprocess.run(['open', gif_path])
        print('GIF created successfully! Opening now...')
    else:
        print('GIF created successfully!')

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Create a GIF from a folder of images')

    # Required arguments
    parser.add_argument('folder_path', type=str, help='Path to the folder containing the images')
    parser.add_argument('output_name', type=str, help='Name of the output GIF file')

    # Optional arguments
    parser.add_argument('-speed', type=int, default=100, help='Speed of the GIF animation (default: 100)')
    parser.add_argument('-dissolve', type=int, default=10, help='The number of frames to use for the dissolve effect between each image.')
    parser.add_argument('-optimize', action='store_true', help='Optimize the GIF file')
    parser.add_argument('-quality', type=int, default=75, help='Image quality (only applicable when optimizing)')
    parser.add_argument('-resample', nargs='+', action=ResampleAction, default=[], help='Resampling options')
    parser.add_argument('-date', action='store_true', help='Sort images by date')
    parser.add_argument('-open', action='store_true', help='Open the GIF file after creation')
    parser.add_argument('-colors', type=int, default=None, help='Limit the number of colors in the GIF up to 256')
    parser.add_argument('-watermark', type=str, default='', help='Text watermark to add to the GIF')
    # parser.add_argument('-font', type=str, default='impact.ttf', help='Path to the font file.')
    parser.add_argument('-size', type=int, default=36, help='Font size.')
    parser.add_argument('-location', choices=['TOP', 'CENTER', 'BOTTOM'], default='BOTTOM',
                        help='Location of the watermark.')
    parser.add_argument('-dither', type=str, action=DitherAction, default=[], metavar='DITHER1,DITHER2,...',
                        help='Dithering options to apply to the image. ORDERED, RASTERIZE, FLOYDSTIENBERG, & NONE(8-Bit conversion)')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Validate the folder path
    if not os.path.isdir(args.folder_path):
        print(f'Error: Invalid folder path: {args.folder_path}')
        return
    
    # Create the GIF from the images with dithering
    watermark_text = args.watermark
    create_gif_with_dithering(args, watermark_text)

if __name__ == "__main__":
    main()

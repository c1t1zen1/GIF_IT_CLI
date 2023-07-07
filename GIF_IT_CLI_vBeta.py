import os
import argparse
from PIL import Image
import subprocess
from tqdm import tqdm

class DitherAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values.split(','))

class ResampleAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if isinstance(values, list):
            setattr(namespace, self.dest, values)
        else:
            setattr(namespace, self.dest, values.split(','))

def create_gif_with_dithering(args):
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

        # Resample the image if specified
        if args.resample:
            for scale in args.resample:
                # Calculate the new size based on the scale factor
                new_size = (int(image.width * float(scale)), int(image.height * float(scale)))
                # Resample the image
                image = image.resize(new_size, resample=Image.BOX)

        # Apply dithering for each option
        for dither_option in args.dither:
            # Copy the image to avoid modifying the original
            image_copy = image.copy()
            # Map the dither option string to the corresponding PIL constant
            dither_constant = getattr(Image, dither_option.upper())
            # Apply the dithering option
            image_copy = image_copy.convert('P', dither=dither_constant)
            # Append the image with applied dithering to the list
            images.append(image_copy)
    # Determine the output GIF path
    gif_path = os.path.join(args.folder_path, args.output_name + '.gif')
    # Save the images as a GIF file
    images[0].save(gif_path, save_all=True, append_images=images[1:], duration=args.speed, optimize=args.optimize, quality=args.quality, loop=0)
    # Open the GIF file if the -o or --open flag is provided
    if args.open:
        if os.name == 'nt':  # Windows
            os.startfile(gif_path)
        elif os.name == 'posix':  # macOS and Linux
            subprocess.run(['open', gif_path])
    print('GIF created successfully!')
def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Create a GIF from a folder of images')
    # Add the required arguments
    parser.add_argument('folder_path', type=str, help='Path to the folder containing the images')
    parser.add_argument('output_name', type=str, help='Name of the output GIF file')
    # Add the optional arguments
    parser.add_argument('-speed', type=int, default=100, help='Speed of the GIF animation (default: 100)')
    parser.add_argument('-optimize', action='store_true', help='Optimize the GIF file')
    parser.add_argument('-quality', type=int, default=75, help='Image quality (only applicable when optimizing)')
    parser.add_argument('-resample', nargs='+', action=ResampleAction, default=[], help='Resampling options')
    parser.add_argument('-date', action='store_true', help='Sort images by date')
    parser.add_argument('-open', '--open', action='store_true', help='Open the GIF file after creation')
    parser.add_argument('-dither', type=str, action=DitherAction, default=[], metavar='DITHER1,DITHER2,...',
                        help='Dithering options to apply to the image')
    # Parse the command-line arguments
    args = parser.parse_args()
    # Validate the folder path
    if not os.path.isdir(args.folder_path):
        print(f'Error: Invalid folder path: {args.folder_path}')
        return
    # Create the GIF from the images with dithering
    create_gif_with_dithering(args)
if __name__ == "__main__":
    main()

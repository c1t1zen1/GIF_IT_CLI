
# GIF IT CLI
 A more advanced GIF IT with command line super powers!

                            !!! BETA RELEASE - GIF IT !!!

GIF IT CLI - code by C1t1zen with CodeGPT in VSCode on Windows 10 - July 13 2023

THIS IS A BETA RELEASE USE WITH CAUTION ALWAYS MAKE BACKUPS OF YOUR IMAGES FIRST 

                            !!!! BETA RELEASE - GIF IT !!!	

# ABOUT: 

GIF IT CLI will allow you to easily create a GIF animation from a folder of JPEG's or PNG files.
Folder preperations before using GIF IT CLI appplication:
Name all image files sequentially i.e. "MyGIF_001.jpg, MyGIF_002.jpg, MyGIF_003.jpg, ...etc" 

Make sure you have the image files with the acceptable extensions (PNG, JPG, or JPEG) in one folder for the conversion to work correctly. 
The images should all be the same dimension.

- This CLI (Command Line Interface) version has added options listed below.

                                              
# USAGE:

    GIF_IT_CLI_v_028.exe [-h] [-speed SPEED] [-dissolve DISSOLVE] [-optimize] [-quality QUALITY]
                            [-resample RESAMPLE [RESAMPLE ...]] [-date] [-open] [-colors COLORS]
                            [-watermark WATERMARK] [-font FONT] [-size SIZE] [-location {TOP,CENTER,BOTTOM}]
                            [-dither DITHER1,DITHER2,...]
                            folder_path output_name
                      

# Example command line:

            "python.exe" GIF_IT_CLI_vBeta.py folder_path output_name -speed=200 -dissolve=10 -watermark "c1t1zen" -date -font "arial.ttf" -size=72 -location=TOP -dither FLOYDSTEINBERG,ORDERED,RASTERIZE -colors=64 -optimize -quality=25 -resample 0.8 -open

# Mandatory Commands:

            folder_path           Path to the folder containing the images
            output_name           Name of the output GIF file

# Options:

- Speed: 1000ms = 1sec. Default is 100ms
- Optimize: Optimze the GIF file.  Default is 75

        With optimize on you can choose Quality from 1 to 100

- Resample: Resize your final output scale from 0.1 to 10+ times
- Dissolve: Create dissolve frames between imported images with alpha blend.
- Colors: Limit the number of colors. 1 through 256
- Watermark: Add any text as a watermark. 
- Font: Use your own .ttf font files. Default is impact.ttf NO comic sans!*
- Size: Change font size. Default is 36
- Location: Place watermark TOP, CENTER, or BOTTOM. Default bottom centered.
- Dither option: NONE, RASTERIZE, FLOYDSTEINBERG, & ORDERED. Multiple dithers OK.
- Date: You can order the images based on date created 
- Open: This command will open the gif with the default viewer when created
- Help: 

            -h, --help            show this help message and exit
			-speed SPEED          Speed of the GIF animation (default: 100)		
			-dissolve DISSOLVE    The number of frames to use for the dissolve effect between each image.
			-optimize             Optimize the GIF file
			-quality QUALITY      Image quality (only applicable when optimizing)
			-resample RESAMPLE [RESAMPLE ...]
                        Resampling options
			-date                 Sort images by date
			-open                 Open the GIF file after creation
			-colors COLORS        Limit the number of colors in the GIF up to 256
			-watermark WATERMARK  Text watermark to add to the GIF
			-font FONT            C:/Windows/Fonts/
			-size SIZE            Font size.
			-location {TOP,CENTER,BOTTOM}
                        Location of the watermark.
            -dither DITHER1,DITHER2,...
                        Dithering options to apply to the image. ORDERED, RASTERIZE, FLOYDSTIENBERG, & NONE(8-Bit
                        conversion)

You will see a progress bar and then "GIF created successfully!"

Please report any issues thanks!

                        !!! BETA RELEASE - GIF IT !!!

THIS IS A BETA RELEASE USE WITH CAUTION ALWAYS MAKE BACKUPS OF YOUR IMAGES FIRST !
- https://c1t1zen.com/
GIF IT CLI - code by C1t1zen with CodeGPT in VSCode on Windows 10 - Beta V 023 - July 13 2023

                            !!! BETA RELEASE - GIF IT !!!

BUG NOTE: If the name is not changed it will overwrite the old file without notice.

'*' Comic Sans only allowed in certain circumstances. (Teachers, Emergency Bulletins, & Garfield Memes)



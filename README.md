
# GIF IT CLI
 A more advanced GIF IT with command line super powers!

                            !!! BETA RELEASE - GIF IT !!!

GIF IT CLI - code by C1t1zen with CodeGPT in VSCode on Windows 10 - June 27 2023

THIS IS A BETA RELEASE USE WITH CAUTION ALWAYS MAKE BACKUPS OF YOUR IMAGES FIRST 

                            !!!! BETA RELEASE - GIF IT !!!	

# ABOUT: 

GIF IT CLI will allow you to easily create a GIF animation from a folder of JPEG's or PNG files.
Folder preperations before using GIF IT CLI appplication:
Name all image files sequentially i.e. "MyGIF_001.jpg, MyGIF_002.jpg, MyGIF_003.jpg, ...etc" 

Make sure you have the image files with the acceptable extensions (PNG, JPG, or JPEG) in the one folder for the conversion to work correctly. 
The images should all be the same dimension.

- This CLI (Command Line Interface) version has added options listed below.

                                              
# USAGE:

    GIF_IT_CLI_vBeta.py folder_path output_name 
                      [-h] [-speed SPEED] [-optimize] [-quality QUALITY]
                      [-resample RESAMPLE [RESAMPLE ...]] [-date] [-open]
                      [-dither DITHER1,DITHER2,...]
                      

# Example command line:

            "python.exe" GIF_IT_CLI_vBeta.py folder_path output_name -speed=200 -dither FLOYDSTEINBERG,ORDERED,RASTERIZE -open -optimize -quality=2 -resample 0.8

# Mandatory Commands:

            folder_path           Path to the folder containing the images
            output_name           Name of the output GIF file

# Options:

- Speed: 1000ms = 1sec default 100
- Optimize: Optimze the GIF file

        With optimize on you can use Quality from 1 to 100

- Resample: resize your final output scale from 0.1 to 10+ times 
- Dither option: NONE, RASTERIZE, FLOYDSTEINBERG, & ORDERED

        You can run a few of these at the same time. 

- Date: You can order the images based on date created 
- Open: This command will open the gif with the default viewer when created
- Help: 

            -h, --help            show this help message and exit
            -speed SPEED          Speed of the GIF animation (default: 100)
            -optimize             Optimize the GIF file
            -quality QUALITY      Image quality (only applicable when optimizing)
            -resample RESAMPLE [RESAMPLE ...]
                        Resampling options
            -date                 Sort images by date
            -open, --open         Open the GIF file after creation
            -dither DITHER1,DITHER2,...
                        Dithering options to apply to the image

You will see a progress bar and then "GIF created successfully!"

Please report any issues thanks!

                        !!! BETA RELEASE - GIF IT !!!

THIS IS A BETA RELEASE USE WITH CAUTION ALWAYS MAKE BACKUPS OF YOUR IMAGES FIRST !
- https://c1t1zen.com/
GIF IT CLI - code by C1t1zen with CodeGPT in VSCode on Windows 10 - Beta V 001 - June 28 2023

                            !!! BETA RELEASE - GIF IT !!!

BUG NOTE: If the name is not changed it will overwrite the old file without notice.





import argparse

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to create and define these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with the default value 'pet_images'
      2. CNN Model Architecture as --arch with the default value 'vgg'
      3. Text File with Dog Names as --dogfile with the default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    """
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser()

    # Create 3 command line arguments
    parser.add_argument('--dir', type = str, default = 'pet_images/', 
                        help = 'path to the folder of images')
    parser.add_argument('--arch', type = str, default = 'vgg', 
                        help = 'CNN model architecture to use for image classification')
    parser.add_argument('--dogfile', type = str, default = 'dognames.txt', 
                        help = 'text file that contains all the valid dog names')

    # Parse the command line arguments
    return parser.parse_args()

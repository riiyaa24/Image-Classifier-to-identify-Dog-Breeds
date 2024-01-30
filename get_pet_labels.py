from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as the image filename and 'value' as a 
      List. The list contains the following item:
         index 0 = pet image label (string)
    """
    filename_list = listdir(image_dir)
    results_dic = dict()
    for idx in range(0, len(filename_list), 1):
        if filename_list[idx][0] != ".":
            pet_label = ""
            low_pet_image = filename_list[idx].lower()
            word_list_pet_image = low_pet_image.split("_")
            for word in word_list_pet_image:
                if word.isalpha():
                    pet_label += word + " "
            pet_label = pet_label.strip()
            if filename_list[idx] not in results_dic:
                results_dic[filename_list[idx]] = [pet_label]
            else:
                print("** Warning: Key=", filename_list[idx], 
                      "already exists in results_dic with value =", 
                      results_dic[filename_list[idx]])
    return results_dic

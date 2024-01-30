def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if the classifier correctly 
    classified images 'as a dog' or 'not a dog', even when it is not a match. 
    Demonstrates if the model architecture correctly classifies dog images even if
    it gets the dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as an image filename and 'value' as a 
                    List. The list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int) where 1 = match between pet image
                    and classifier labels, and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int) where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int) where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line. Dog names are all in lowercase with 
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (e.g., maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is a mutable data type, so no return is needed.
    """  
def adjust_results4_isadog(results_dic, dogfile):
    dognames_dic = {}

    with open(dogfile, "r") as infile:
        line = infile.readline()

        while line != "":
            line = line.strip()
            if line not in dognames_dic:
                dognames_dic[line] = 1
            line = infile.readline()

    # Check if items in results_dic are dogs
    for key in results_dic:
        pet_label_is_dog = results_dic[key][0] in dognames_dic
        classifier_label_is_dog = results_dic[key][1] in dognames_dic

        results_dic[key].extend((pet_label_is_dog, classifier_label_is_dog))


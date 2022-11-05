

# The accuracy depends on the clarity of image, orientation, light exposure.

#‌ Worst case scenarios:
#   The contour fails to detect the license plate correctly
#        a) we have to again relay on Machine learning.
#        b) improve the quality of the picture.


if __name__ == "__main__":

    import os

    from license_plate_detection import (clear_image, read_image, get_contours,
                                         find_approximate_contours, roi, show_image)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SRC_PATH = os.path.join(BASE_DIR, "Plate_Licenses/plate_license_K.jpg")

    os.chdir("Plate_Licenses/")
    current_path = os.getcwd()
    dir_list_path = [os.path.join(current_path, file_name) for file_name in os.listdir(current_path)]
    
    if SRC_PATH in dir_list_path:
        img = read_image(SRC_PATH)
        cleared_image = clear_image(img)
        sorted_contours = get_contours(cleared_image)
        approx_cnt = find_approximate_contours(sorted_contours)


        if approx_cnt is None:
            print("\nNo contour detected\n")
        else:
            roi_img = roi(approx_cnt, img)

            show_image(roi_img)
    else:
        raise FileNotFoundError(f"File not found at {current_path}")

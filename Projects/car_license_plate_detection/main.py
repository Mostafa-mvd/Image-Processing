


# Methods for finding plate licenses:
#   a) Machine Learning
#   b) Haar Cascades Method
#   c) Manually Method (Contours)


#‌ Worst case scenarios:
#   The contour fails to detect the license plate correctly
#        a) we have to again relay on Machine learning.
#        b) improve the quality of the picture.


# The accuracy depends on the clarity of image, orientation, light exposure.


if __name__ == "__main__":

    from config import Config
    from errors import ContoursNotFoundError

    from license_plate_detection import (clear_image, read_image, get_contours,
                                         approximate_contours, roi, show_image)

    conf = Config()

    BASE_DIR_PATH = conf.BASE_DIR_PATH
    IMG_FILE_PATH = conf.SRC_FILE_PATH
    PLATE_LICENSES_ITEMS = conf.SRC_LIST_DIR

    if IMG_FILE_PATH in PLATE_LICENSES_ITEMS:
        img = read_image(IMG_FILE_PATH)
        cleared_image = clear_image(img)
        sorted_contours = get_contours(cleared_image)
        approx_cnt = approximate_contours(sorted_contours)

        if approx_cnt is None:
            raise ContoursNotFoundError("No contours detected")
            
        roi_img = roi(approx_cnt, img)
        show_image(roi_img)
    else:
        raise FileNotFoundError(f"File not found at {BASE_DIR_PATH}")

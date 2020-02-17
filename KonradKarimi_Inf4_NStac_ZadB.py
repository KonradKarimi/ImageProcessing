from absl import app, flags, logging

import scipy.io
import numpy as np
import operator
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

FLAGS = flags.FLAGS
flags.DEFINE_string("path_to_image", None, "Path to image file location")
flags.DEFINE_integer("brightness", None,
                     "How many times to increase brightnes")
flags.mark_flag_as_required("path_to_image")
flags.mark_flag_as_required("brightness")


def loadImage(path_to_image):
    logging.info("Loading image from: %s", path_to_image)
    img = mpimg.imread(path_to_image)
    # Color sheme RGBA probably?? - so we need to remove Alpha to not mess calculation in the future
    # img = img[:, :, :3]
    return img.astype(np.int_)


def increaseBrightness(img, brightness):
    logging.info("Increasing brightness %s times", brightness)
    new_img = img
    new_img = np.where(new_img < 255, new_img*brightness, new_img)
    new_img = np.where(new_img > 255, 255, new_img)
    return new_img


def displayImg(img):
    logging.info("Displaying image")
    plt.imshow(img)
    plt.axis("off")
    plt.show()


def getImgInfo(img, original: bool):
    if original is True:
        logging.info(
            "\n\nDisplaying propersies for original image (BEFORE BRIGHTENING)")
    else:
        logging.info(
            "\n\nDisplaying enhanced image properties (AFRER BRIGHTENING)")

    print(f'''
    Minimum brightness value: {np.min(img)}
    Maximum brightness value: {np.max(img)}
    Average brightness value: {np.average(img)}
        ''')

    return np.min(img), np.max(img), np.average(img)


def correction(pxl, pxl_min, pxl_max):
    r = 255.0/(pxl_max-pxl_min+2)
    corrected_image = np.round(
        r*np.where(pxl >= pxl_min, pxl - pxl_max+1, 0)).clip(max=255)
    return corrected_image.astype(np.int_)


def saveNewImage(img):
    mpimg.imsave("new_file_out.GIF", img.astype(np.uint8))


def main(argv):
    del argv  # Unused.

    orginal_img = loadImage(FLAGS.path_to_image)
    enhanced_img = increaseBrightness(orginal_img, FLAGS.brightness)
    orginal_min, orginal_max, orginal_avg = getImgInfo(orginal_img, True)
    enhanced_min, enhanced_max, enhanced_avg = getImgInfo(enhanced_img, False)

    new = enhanced_img
    displayImg(new)
    new = correction(enhanced_img, enhanced_min, enhanced_max)
    displayImg(new)

    saveNewImage(new)


if __name__ == '__main__':
    app.run(main)

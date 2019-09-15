import numpy as np
from skimage.transform import rescale
from skimage.feature import hog, local_binary_pattern
from skimage.exposure import histogram

def genearte_HOG_descriptor(image):
    '''
    Generate Histogram of gradients
    :param image: Input image of Hand (1200 * 1600)
    :return: feature_descriptor(9576), HOG_image(120*160)
    '''
    image_rescaled = rescale(image, 0.1, anti_aliasing=True)
    return hog(image_rescaled, orientations=9,
                    pixels_per_cell=(8, 8),
                    cells_per_block=(2, 2),
                    visualize=True,
                    multichannel= False,
                    block_norm='L2-Hys')


#function for genear
def generate_LBP_descriptor(image):
    '''
    Generate Local_binary_pattern histogram for 100*100 window and concatinate to single image
    :param image: Input image of Hand (1200 * 1600)
    :return: feature_descriptor(49152(12*16*256)), LBP_image(1200*1600)
    '''
    n_points = 8
    radius = 2
    METHOD = "default"
    LBP_image = np.ndarray(shape=(1200,1600), dtype=float)
    LBP_hist = np.ndarray(shape = (12 * 16 * 256), dtype=float)
    k = 0

    for i in range(0,1200,100):
        for j in range(0,1600,100):
            lbp = local_binary_pattern(image[i:(i+100),j:(j+100)], n_points, radius, METHOD)
            LBP_image[i:(i+100),j:(j+100)] = lbp
            LBP_hist[k:k+256],_ = histogram(lbp, nbins=256)
            k = k + 256
    return LBP_hist, LBP_image



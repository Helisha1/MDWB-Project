import model
import feature_descriptor as fd
import math
import sys


def find_k_similar_HOG(image, k):
    '''
    Retrive HOG_image_descriptors from database and compare it with given image and find k similar images
    :param image: Input image of Hand (1200 * 1600)
    :param k: number of similar image you want
    :return: List of ksimilarimages (imagename,similarity_value)
    '''
    result =  model.getAllHOGDescriptors()
    ksimilarimages = [["",0] for i in range(k)]

    q_descriptor,q_image = fd.genearte_HOG_descriptor(image)
    q_descriptor = q_descriptor.tolist()
    for i in result:
        imageName = i['imageName']
        HOG_descriptor = i['HOG']
        for j in range(0,k):
            similarity = similarity_of_HOG(HOG_descriptor,q_descriptor)
            if(similarity>ksimilarimages[j][1]):
                ksimilarimages.insert(j,[imageName,similarity])
                ksimilarimages = ksimilarimages[0:k]
                break

    return ksimilarimages


def find_k_similar_LBP(image, k):
    '''
    Retrive LBP_image_descriptors from database and compare it with given image and find k similar images
    :param image: Input image of Hand (1200 * 1600)
    :param k: number of similar image you want
    :return: List of ksimilarimages (imagename,distance_major)
    '''
    result =  model.getAllLBPDescriptors()
    ksimilarimages = [["",sys.float_info.max] for i in range(k)]

    q_descriptor,q_image = fd.generate_LBP_descriptor(image)

    q_descriptor = q_descriptor.tolist()
    for i in result:
        imageName = i['imageName']
        LBP_descriptor = i['LBP']
        for j in range(0,k):
            distance = distance_of_LBP(LBP_descriptor,q_descriptor)
            if(distance<ksimilarimages[j][1]):
                ksimilarimages.insert(j,[imageName,distance])
                ksimilarimages = ksimilarimages[0:k]
                break

    return ksimilarimages


def cos_sim(a, b):
    '''
     Function for finding cosine-similarity
    :param a: list1
    :param b: list2
    :return: similarity value [0:1]
    '''
    dot = 0
    moda = 0
    modb = 0
    for i in range(len(a)) :
        dot += a[i] * b[i]
        moda += a[i] * a[i]
        modb += b[i] * b[i]
    return dot/(math.sqrt(moda)*math.sqrt(modb))


def similarity_of_HOG(HOG1,HOG2):
    '''
    Returns similarity value
    :param HOG1: HOG of first image
    :param HOG2: HOG of second image
    :return: similarity value [0:1]
    '''
    return cos_sim(HOG1,HOG2)

#function for chi square_distance
def euclidian_distance(a, b):
    '''
    Find the euclidian distance
    :param a: list1
    :param b: list2
    :return: distance
    '''
    sum = 0
    for i in range(0,len(a)):
        x =(a-b)
        sum += x*x
    return math.sqrt(sum)

def distance_of_LBP(LBP1,LBP2):
    '''
    Return euclidian distance
    :param LBP1: LBP of first image
    :param LBP2: LBP of second image
    :return: distance value
    '''
    return euclidian_distance(LBP1,LBP2)


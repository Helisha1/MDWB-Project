from pymongo import MongoClient
from skimage import io

#connection
client = MongoClient("mongodb://localhost:27017")
db = client.MWDBProject


#HandInfo
def insert_imageName(imageName):
    '''
    insert imageName in collection HandInfo
    '''
    return db.HandInfo.insert_one({"imageName" : imageName})

def getAllImages() :
    '''
    get all imageNmaes from database
    '''
    return db.HandInfo.find({},{"imageName" : 1})

#HOG
def insertHOGDescriptor(imageName,HOGdescriptor) :
    '''
    Insert HOG of particular image to collection HOG
    '''
    HOGdescriptor = HOGdescriptor.tolist()
    success =db.HOG.insert_one({ "imageName" : imageName, "HOG" : HOGdescriptor })
    return success

def getHOGDescriptor(imageName):
    '''
    get HOG_descriptor of particular image from database
    '''
    HOG_Descriptor = db.HOG.find({"imageName" : imageName})

def getAllHOGDescriptors():
    '''
    get all images with HOG descriptor
    '''
    return db.HOG.find({},{"imageName" :1 ,"HOG" : 1})





#LBP
def insertLBPDescriptor(imageName,LBPdescriptor) :
    '''
    Insert LBP of particular image to collection LBP
    '''
    LBPdescriptor = LBPdescriptor.tolist()
    success =db.LBP.insert_one({ "imageName" : imageName, "LBP" : LBPdescriptor })
    return success


def getLBPDescriptor(imageName):
    '''
    get LBP_descriptor of particular image from database
    '''
    LBP_Descriptor = db.LBP.find({"imageName" : imageName})


def getAllLBPDescriptors():
    '''
    get all images with LBP descriptor
    '''
    return db.LBP.find({},{"imageName" :1 ,"LBP" : 1})


#io
def getImage(imageName):
    '''
    get image from the folder by imagename
    :param imageName: path + imageName
    :return: image
    '''
    return io.imread(imageName, as_gray=True)


def get_image_by_path(path):
    '''
    get image from the path you give
    :param path: folder path where image is stored
    :return: image
    '''
    return io.imread(path, as_gray=True)



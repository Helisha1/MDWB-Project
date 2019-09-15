import tkinter
from tkinter.filedialog import askopenfilename,askdirectory
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import glob

import model
import feature_descriptor as fd
import similarity

top = tkinter.Tk()
C1 = tkinter.Canvas(top)

def buttonClick1():
    '''
    Executed when button1("Generate HOG and LBP discriptors") is clicked.
    1. select image option (Browse image)
    2. Generate HOG descriptor
    3. Generate LBP descriptor
    4. Plot selected image, HOG_image, LBP_image on canvas
    :return:
    '''
    filename = askopenfilename(title = "Select file",   filetypes = [("jpeg files","*.jpg")])
    image = model.get_image_by_path(filename)
    HOG_feature_descriptor,HOG_image = fd.genearte_HOG_descriptor(image)
    LBP_feature_descriptor,LBP_image = fd.generate_LBP_descriptor(image)

    fig, axes = plt.subplots(nrows=1, ncols=3)
    ax = axes.ravel()
    ax[0].imshow(image,cmap="gray")
    ax[0].set_title("Original image")
    ax[1].imshow(HOG_image, cmap="gray")
    ax[1].set_title("HOG image")
    ax[2].imshow(LBP_image,cmap="gray")
    ax[2].set_title("LBP image")
    C1 = FigureCanvasTkAgg(fig, master=top)
    C1.draw()
    C1.get_tk_widget().grid(row = 4,columnspan = 4)

B1 = tkinter.Button(top, text ="Generate HOG and LBP discriptors", command = buttonClick1, relief="raised" , bd = 5,bg = "lightgray", fg = "black" , height = 3, width = 100, font = 40 )
B1.grid(padx = 220,pady = 2 ,row = 1,columnspan = 4)




def buttonClick2() :
    '''
    Executed when button2("Enter image folder for generating HOG and LBP discriptors") is clicked.
    1. select folder option (Browse folder where images are stored for learning)
    2. Generate HOG descriptor and LBP descriptor for all images in the folder.
    3. All HOG_descriptor are stored in database as (imageName , HOG_Desriptor)
    4. All LBP_descriptor are stored in database as (imageName , LBP_Desriptor)
    :return:
    '''
    folderpath = askdirectory(title = "Select folder")
    folderpath = folderpath + '/*.jpg'
    for filename in glob.glob(folderpath):
        model.insert_imageName(filename)
        image = model.get_image_by_path(filename)
        HOG_feature_descriptor,HOG_image = fd.genearte_HOG_descriptor(image)
        LBP_feature_descriptor,LBP_image = fd.generate_LBP_descriptor(image)
        model.insertHOGDescriptor(filename,HOG_feature_descriptor)
        model.insertLBPDescriptor(filename,LBP_feature_descriptor)
    print("success")

B2 = tkinter.Button(top, text ="Enter image folder for generating HOG and LBP discriptors", command = buttonClick2, relief="raised", bd = 5, bg = "lightgray", fg = "black" , height = 3, width = 100, font = 40 )
B2.grid(padx = 220,pady = 10,row = 2,columnspan = 4)




label = tkinter.Label(top, text= "value of K : ")
label.grid(column=0,row = 3,padx=0)

textbox = tkinter.Text(top ,height=1,width = 25)
textbox.grid(column = 1,row = 3,padx =0)

def buttonClickHOG():
    '''
    Executed when button3("Enter image to find k similar images by HOG") is clicked.
    1. select image option (Browse image)
    2. get value of K from textbox, if value is not given or value is 0 than set k as 10
    3. find k similar images
    4. plot k images on canvas
    :return:
    '''
    filename = askopenfilename(title = "Select file",   filetypes = [("jpeg files","*.jpg")])
    image = model.get_image_by_path(filename)
    input = textbox.get("1.0","end-1c")
    if input.isnumeric() and int(input) != 0 :
        k =  int(input)
    else :
        k = 10
    ksimilarimages = similarity.find_k_similar_HOG(image,k)
    col  = 4
    row = int(k/col)
    if k%col != 0 :
        row +=1
    fig, axes = plt.subplots(nrows = row, ncols=col)
    ax = axes.ravel()
    for i in range(0,k):
        image = model.getImage(ksimilarimages[i][0])
        ax[i].imshow(image,cmap="gray")
        name = ksimilarimages[i][0]
        name  = name[len(name)-13:len(name)]
        ax[i].set_title("" + name + "\n(" + str(ksimilarimages[i][1]) + ")",fontsize = 6)
        ax[i].xaxis.set_visible(False)
        ax[i].yaxis.set_visible(False)
    for i in range(i,row*col):
        ax[i].xaxis.set_visible(False)
        ax[i].yaxis.set_visible(False)

    C1 = FigureCanvasTkAgg(fig, master=top)
    C1.draw()
    C1.get_tk_widget().grid(row = 4,columnspan = 4)

B3 = tkinter.Button(top, text ="Enter image to find k similar images by HOG", command = buttonClickHOG, relief="raised", bd = 5, bg = "lightgray", fg = "black" , height = 3, width = 60, font = 40 )
B3.grid(padx = 30,column = 2,row = 3)




def buttonClickLBP():
    '''
    Executed when button4("Enter image to find k similar images by LBP") is clicked.
    1. select image option (Browse image)
    2. get value of K from textbox, if value is not given or value is 0 than set k as 10
    3. find k similar images
    4. plot k images on canvas
    :return:
    '''
    filename = askopenfilename(title = "Select file",   filetypes = [("jpeg files","*.jpg")])
    image = model.get_image_by_path(filename)
    input = textbox.get("1.0","end-1c")
    if input.isnumeric() and int(input) != 0 :
        k =  int(input)
    else :
        k = 10
    ksimilarimages = similarity.find_k_similar_LBP(image,k)
    col = 4
    row = int(k/col)
    if k%col != 0 :
        row +=1
    fig, axes = plt.subplots(nrows = row, ncols=col)
    ax = axes.ravel()
    for i in range(0,k):
        image = model.getImage(ksimilarimages[i][0])
        ax[i].imshow(image,cmap="gray")
        name = ksimilarimages[i][0]
        name  = name[len(name)-13:len(name)]
        ax[i].set_title("" + name + "\n(" + str(ksimilarimages[i][1]) + ")",fontsize = 6)
        ax[i].xaxis.set_visible(False)
        ax[i].yaxis.set_visible(False)
    for i in range(i,row*col):
        ax[i].xaxis.set_visible(False)
        ax[i].yaxis.set_visible(False)


    C1 = FigureCanvasTkAgg(fig, master=top)
    C1.draw()
    C1.get_tk_widget().grid(row = 4,columnspan = 4)

B4 = tkinter.Button(top, text ="Enter image to find k similar images by LBP", command = buttonClickLBP, relief="raised", bd = 5,bg = "lightgray", fg = "black" , height = 3, width = 60, font = 40 )
B4.grid(row = 3,column = 3,padx =30)

top.mainloop()

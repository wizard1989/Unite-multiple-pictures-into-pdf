import glob
import os
import re

from reportlab.lib import utils
from reportlab.pdfgen import canvas



#----------------------------------------------------------------------
def sorted_nicely( l ):
    """ 
    # http://stackoverflow.com/questions/2669059/how-to-sort-alpha-numeric-set-in-python
 
    Sort the given iterable in the way that humans expect.
    """ 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)





#----------------------------------------------------------------------
def unite_pictures_into_pdf(outputPdfName, pathToSavePdfTo, pathToPictures, splitType, numberOfEntitiesInOnePdf, listWithImagesExtensions, picturesAreInRootFolder, nameOfPart):
    
    if numberOfEntitiesInOnePdf < 1:
        print("Wrong value of numberOfEntitiesInOnePdf.")
        return
    if len(listWithImagesExtensions) == 0:
        print("listWithImagesExtensions is empty.")
        return
    
    
    if picturesAreInRootFolder == False:
        foldersInsideFolderWithPictures = sorted_nicely(glob.glob(pathToPictures + "\\*\\"))
        if len(foldersInsideFolderWithPictures) != 0:
            picturesPathsForEachFolder = []
            for iFolder in foldersInsideFolderWithPictures:
                picturePathsInFolder = []
                for jExtension in listWithImagesExtensions:
                    picturePathsInFolder.extend(glob.glob(iFolder + "*." + jExtension))
                picturesPathsForEachFolder.append(sorted_nicely(picturePathsInFolder))
            if splitType == "folder":
                numberOfFoldersAdded = 0;
                for iFolder in picturesPathsForEachFolder:
                    if (numberOfFoldersAdded % numberOfEntitiesInOnePdf) == 0:
                        endNumber = numberOfFoldersAdded + numberOfEntitiesInOnePdf
                        if endNumber > len(picturesPathsForEachFolder):
                            endNumber = len(picturesPathsForEachFolder)
                        filename = []
                        if numberOfEntitiesInOnePdf > 1:
                            filename = os.path.join(pathToSavePdfTo, outputPdfName + "_" + nameOfPart + "_" + str(numberOfFoldersAdded + 1) + '-' + str(endNumber) + "_of_" + str(len(picturesPathsForEachFolder)) + ".pdf")
                        elif numberOfEntitiesInOnePdf == 1:
                            filename = os.path.join(pathToSavePdfTo, outputPdfName + "_" + nameOfPart + "_" + str(numberOfFoldersAdded + 1) + "_of_" + str(len(picturesPathsForEachFolder)) + ".pdf")
                        c = canvas.Canvas(filename)
                    for jPicture in iFolder:
                        img = utils.ImageReader(jPicture)
                        imagesize = img.getSize()
                        c.setPageSize(imagesize)
                        c.drawImage(jPicture, 0, 0)
                        c.showPage()
                    numberOfFoldersAdded += 1
                    if (numberOfFoldersAdded % numberOfEntitiesInOnePdf) == 0:
                        c.save()
                        print("created", filename)
                if (numberOfFoldersAdded % numberOfEntitiesInOnePdf) != 0:
                        c.save()
                        print("created", filename)
            elif splitType == "picture":
                numberOfPicturesAdded = 0;
                totalNumberOfPictures = 0;
                for iFolder in picturesPathsForEachFolder:
                    totalNumberOfPictures += len(iFolder)
                for iFolder in picturesPathsForEachFolder:
                    for jPicture in iFolder:
                        if (numberOfPicturesAdded % numberOfEntitiesInOnePdf) == 0:
                            endNumber = numberOfPicturesAdded + numberOfEntitiesInOnePdf
                            if endNumber > totalNumberOfPictures:
                                endNumber = totalNumberOfPictures
                            filename = []
                            if numberOfEntitiesInOnePdf > 1:
                                filename = os.path.join(pathToSavePdfTo, outputPdfName + "_" + nameOfPart + "_" + str(numberOfPicturesAdded + 1) + '-' + str(endNumber) + "_of_" + str(totalNumberOfPictures) + ".pdf")
                            elif numberOfEntitiesInOnePdf == 1:
                                filename = os.path.join(pathToSavePdfTo, outputPdfName + "_" + nameOfPart + "_" + str(numberOfPicturesAdded + 1) + "_of_" + str(totalNumberOfPictures) + ".pdf")
                            c = canvas.Canvas(filename)
                        img = utils.ImageReader(jPicture)
                        imagesize = img.getSize()
                        c.setPageSize(imagesize)
                        c.drawImage(jPicture, 0, 0)
                        c.showPage()
                        numberOfPicturesAdded += 1
                        if (numberOfPicturesAdded % numberOfEntitiesInOnePdf) == 0:
                            c.save()
                            print("created", filename)
                if (numberOfPicturesAdded % numberOfEntitiesInOnePdf) != 0:
                        c.save()
                        print("created", filename)
            elif splitType == "none":
                filename = os.path.join(pathToSavePdfTo, outputPdfName + ".pdf")
                c = canvas.Canvas(filename)
                for iFolder in picturesPathsForEachFolder:
                    for jPicture in iFolder:
                        img = utils.ImageReader(jPicture)
                        imagesize = img.getSize()
                        c.setPageSize(imagesize)
                        c.drawImage(jPicture, 0, 0)
                        c.showPage()
                c.save()
                print("created", filename)
            else:
                print("Wrong splitType value")
        else:
            print("No pictures found.")
        return
        
    if picturesAreInRootFolder == True:
        picturesInsideFolderWithPictures = []
        for iExtension in listWithImagesExtensions:
            picturesInsideFolderWithPictures.extend(glob.glob(pathToPictures + "\\*." + iExtension))
        picturesInsideFolderWithPictures = sorted_nicely(picturesInsideFolderWithPictures)
        if len(picturesInsideFolderWithPictures) != 0:
            if splitType == "picture":
                numberOfPicturesAdded = 0
                totalNumberOfPictures = len(picturesInsideFolderWithPictures)
                for iPicture in picturesInsideFolderWithPictures:
                    if (numberOfPicturesAdded % numberOfEntitiesInOnePdf) == 0:
                        endNumber = numberOfPicturesAdded + numberOfEntitiesInOnePdf
                        if endNumber > totalNumberOfPictures:
                            endNumber = totalNumberOfPictures
                        filename = []
                        if numberOfEntitiesInOnePdf > 1:
                            filename = os.path.join(pathToSavePdfTo, outputPdfName + "_" + nameOfPart + "_" + str(numberOfPicturesAdded + 1) + '-' + str(endNumber) + "_of_" + str(totalNumberOfPictures) + ".pdf")
                        elif numberOfEntitiesInOnePdf == 1:
                            filename = os.path.join(pathToSavePdfTo, outputPdfName + "_" + nameOfPart + "_" + str(numberOfPicturesAdded + 1) + "_of_" + str(totalNumberOfPictures) + ".pdf")
                        c = canvas.Canvas(filename)
                    img = utils.ImageReader(iPicture)
                    imagesize = img.getSize()
                    c.setPageSize(imagesize)
                    c.drawImage(iPicture, 0, 0)
                    c.showPage()
                    numberOfPicturesAdded += 1
                    if (numberOfPicturesAdded % numberOfEntitiesInOnePdf) == 0:
                        c.save()
                        print("created", filename)
                if (numberOfPicturesAdded % numberOfEntitiesInOnePdf) != 0:
                    c.save()
                    print("created", filename)
            elif splitType == "none":
                filename = os.path.join(pathToSavePdfTo, outputPdfName + ".pdf")
                c = canvas.Canvas(filename)
                for iPicture in picturesInsideFolderWithPictures:
                    img = utils.ImageReader(iPicture)
                    imagesize = img.getSize()
                    c.setPageSize(imagesize)
                    c.drawImage(iPicture, 0, 0)
                    c.showPage()
                c.save()
                print("created", filename)
            else:
                print("Wrong splitType value")
        else:
            print("No pictures found.")
        return
        
        
    
#----------------------------------------------------------------------
if __name__ == "__main__":
   
    outputPdfName = "pdf_with_pictures"
    pathToSavePdfTo = "D:\\pictures"
    pathToPictures = "D:\\pictures"
    splitType = "picture"
    numberOfEntitiesInOnePdf = 1
    listWithImagesExtensions = ["png", "jpg"]
    picturesAreInRootFolder = False
    nameOfPart = "volume"
    
    unite_pictures_into_pdf(outputPdfName, pathToSavePdfTo, pathToPictures, splitType, numberOfEntitiesInOnePdf, listWithImagesExtensions, picturesAreInRootFolder, nameOfPart)
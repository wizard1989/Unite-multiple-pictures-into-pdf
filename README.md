# Unite-multiple-pictures-into-pdf
This python script unites multiple pictures into pdf.

# How to use it
Function unite_pictures_into_pdf has 8 input paramaters:
  1. outputPdfName - name of resulting pdf file without pdf extension. For example, outputPdfName = "pdf_with_pictures". It will be appended, if pdf split is chosen.
  2. pathToSavePdfTo - name of path to save pdf file to without trailing slash. For example, pathToSavePdfTo = "D:\\pictures".
  3. pathToPictures - name of path with pictures without trainling slash. For example, pathToPictures = "D:\\pictures". This path should contain pictures and/or folders with pictures.
  4. splitType - how to split resulting pdf. splitType can be one of those: "folder", "picture", "none". For example, we have in pathToPictures multiple folders with pictures. Folders are named vol001, vol002 and so on. Using "folder" split we can create multiple pdfs, containing, for example, pictures from folder 1-3, 4-6, 7-9, 10-12. "picture" split do this based on number of pictures in one pdf. "none" split means no split. We create one whole pdf.
  5. numberOfEntitiesInOnePdf - the maximum number of folders or pictures in one partial pdf. numberOfEntitiesInOnePdf should be an integer larger than 0.
  6. listWithImagesExtensions - list, containing extensions of images to search. For example, listWithImagesExtensions = ["png", "jpg"].
  7. picturesAreInRootFolder - boolean, indicating whether pictures are in root folder (it equals to True) or should we search them in subfolders (it equals to False). Values should be boolean True or False. For example, picturesAreInRootFolder = True.
  8. nameOfPart


outputPdfName = "pdf_with_pictures"
pathToSavePdfTo = "D:\\pictures"
pathToPictures = "D:\\pictures"
splitType = "picture"
numberOfEntitiesInOnePdf = 1
listWithImagesExtensions = ["png", "jpg"]
picturesAreInRootFolder = False
nameOfPart = "volume"
    
unite_pictures_into_pdf(outputPdfName, pathToSavePdfTo, pathToPictures, splitType, numberOfEntitiesInOnePdf, listWithImagesExtensions, picturesAreInRootFolder, nameOfPart)












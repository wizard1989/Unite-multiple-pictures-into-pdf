# Unite-multiple-pictures-into-pdf
This python script unites multiple pictures into pdf.

# How to use it
Function unite_pictures_into_pdf has 8 input paramaters:
  1. outputPdfName - name of resulting pdf file without pdf extension. For example, outputPdfName = "pdf_with_pictures". It will be appended, if pdf split is chosen.
  2. pathToSavePdfTo


outputPdfName = "pdf_with_pictures"
pathToSavePdfTo = "D:\\pictures"
pathToPictures = "D:\\pictures"
splitType = "picture"
numberOfEntitiesInOnePdf = 1
listWithImagesExtensions = ["png", "jpg"]
picturesAreInRootFolder = False
nameOfPart = "volume"
    
unite_pictures_into_pdf(outputPdfName, pathToSavePdfTo, pathToPictures, splitType, numberOfEntitiesInOnePdf, listWithImagesExtensions, picturesAreInRootFolder, nameOfPart)












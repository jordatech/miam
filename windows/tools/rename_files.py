#https://stackoverflow.com/questions/2759067/rename-multiple-files-in-a-directory-in-python
import os
baseDir = r'F:\Multimedia_Projects\2022'
if not(os.path.isdir(baseDir)):
     print("***********["+baseDir+"] is not a valid directory ***********")
else:
    #Create list of folders to iterate over
    folderNamesArray = os.listdir(baseDir)
    #Choose to only rename files in video folders
    fullPathArray = [baseDir+os.path.sep+folderName + r'\Videos' for folderName in folderNamesArray]
    
    # fullPathArray = [r'D:\Test2022\2022-03-09-Roadtrip-McLeod-Ganj-to-Tashi-Jong-TB-Monastary\Videos'] #Test

    # fullPathArray = [
    #     r'F:\Multimedia_Projects\2022\2022-03-08-McLeod-Ganj-A-and-L-Home',
    #     r'F:\Multimedia_Projects\2022\2022-03-09-Roadtrip-McLeod-Ganj-to-Tashi-Jong-TB-Monastary',
    #     r'F:\Multimedia_Projects\2022\2022-03-10-Roadtrip-Tashi-Jong-TB-Monastary-to-Manali-Suburb-Solang',
    #     r'']

    #For List of Folders containing Video files
    for folderDir in fullPathArray:
        if not(os.path.isdir(folderDir)):
            print("***********["+folderDir+"] is not a valid directory ***********")
        else:
            # Goto current working directory
            os.chdir(folderDir)
            # Get 2nd Parent Name with date information for each folder... to help in re-naming
            parent2FolderName = folderDir.split(os.path.sep)[-2]
            # Re-name Video, Photo and XML info files in folder
            fileNames = os.listdir()
            for fileName in fileNames:
                # For every Photo and Video and Audio file...
                if not(os.path.isfile(fileName)):
                    print("!!!!!!!!!!["+fileName+"] is not a file and was not renamed !!!!!!!!!!")
                elif fileName.__contains__(parent2FolderName):
                    print("!!!!!!!!!!["+fileName+"] contains "+parent2FolderName+" and was not renamed !!!!!!!!!!")
                elif fileName.lower().endswith(('.png', '.jpg', '.jpeg', '.arw', '.cr2', '.orf', '.mp4', '.mov', '.mp3', '.wav')):
                    # Rename with Date attributes as a suffex to the fileName
                    fileNameWithoutExt = fileName.split('.')[-2]
                    fileNameExt = '.'+fileName.split('.')[-1]
                    newFileName = fileNameWithoutExt+"-"+parent2FolderName+fileNameExt
                    os.rename(fileName, newFileName)
                    print("["+fileName+"] was renamed to ["+newFileName+"]")
                # Fix XML data files *M01.xml that go with sony MP4 files
                elif fileName.upper().endswith(('M01.XML')):
                    # Re-name xml files
                    fileNameWithoutExt = fileName.upper().replace("M01.XML","")
                    fileNameExt = "M01.XML"
                    newFileName = fileNameWithoutExt+"-"+parent2FolderName+fileNameExt
                    os.rename(fileName, newFileName)
                    print("["+fileName+"] was renamed to ["+newFileName+"]")
                else:
                    print("!!!!!!!!!!["+fileName+"] was not a recognized video, photo or audio file and was NOT renamed !!!!!!!!!!")
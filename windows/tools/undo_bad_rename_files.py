# #https://stackoverflow.com/questions/2759067/rename-multiple-files-in-a-directory-in-python
# import os
# fullPathArray = [r'F:\Multimedia_Projects\2022\2022-03-21-Roadtrip-Manali-to-Dheradun-Night-Driving\Videos'] #Test

# #For List of Folders containing Video files
# for folderDir in fullPathArray:
#     if not(os.path.isdir(folderDir)):
#         print("***********["+folderDir+"] is not a valid directory ***********")
#     else:
#         # Goto current working directory
#         os.chdir(folderDir)
#         # Get 2nd Parent Name with date information for each folder... to help in re-naming
#         parent2FolderName = folderDir.split(os.path.sep)[-2]
#         # Re-name Video, Photo and XML info files in folder
#         fileNames = os.listdir()
#         for fileName in fileNames:
#             # For every Photo and Video and Audio file...
#             if not(os.path.isfile(fileName)):
#                 print("!!!!!!!!!!["+fileName+"] is not a file and was not renamed !!!!!!!!!!")
#             elif fileName.__contains__(parent2FolderName):
#                 newFileName = fileName.replace("-"+parent2FolderName,"")+"M01.XML" # Undo bad naming
#                 os.rename(fileName, newFileName)
#                 print("["+fileName+"] was renamed to ["+newFileName+"]")
#             #     print("!!!!!!!!!!["+fileName+"] contains "+parent2FolderName+" and was not renamed !!!!!!!!!!")
#             elif fileName.lower().endswith(('.png', '.jpg', '.jpeg', '.arw', '.cr2', '.orf', '.mp4', '.mov', '.mp3', '.wav')):
#                 # Rename with Date attributes as a suffex to the fileName
#                 fileNameWithoutExt = fileName.split('.')[-2]
#                 fileNameExt = '.'+fileName.split('.')[-1]
#                 # newFileName = fileNameWithoutExt+"-"+parent2FolderName+fileNameExt
#                 newFileName = fileName.replace("-"+parent2FolderName,"")
#                 os.rename(fileName, newFileName)
#                 print("["+fileName+"] was renamed to ["+newFileName+"]")
#             # Fix XML data files *M01.xml that go with sony MP4 files
#             # elif fileName.upper().endswith(('M01.XML')):
#             elif os.path.getsize(fileName)<1000000:
#                 # Re-name xml files
#                 fileNameWithoutExt = fileName.replace("M01.XML","")
#                 fileNameExt = "M01.XML"
#                 # newFileName = fileNameWithoutExt+"-"+parent2FolderName+fileNameExt
#                 newFileName = fileName.replace("-"+parent2FolderName.upper(),"") # Undo bad naming
#                 newFileName = newFileName.replace(".mp4","M01.XML") # Undo bad naming
#                 os.rename(fileName, newFileName)
#                 print("["+fileName+"] was renamed to ["+newFileName+"]")
#             else:
#                 fileNameWithoutExt = fileName
#                 fileNameExt = '.mp4'
#                 newFileName = fileNameWithoutExt+"-"+parent2FolderName+fileNameExt
#                 os.rename(fileName, newFileName)
#                 print("["+fileName+"] was renamed to ["+newFileName+"]")
#                 # print("!!!!!!!!!!["+fileName+"] was not a recognized video, photo or audio file and was NOT renamed !!!!!!!!!!")

#https://stackoverflow.com/questions/2759067/rename-multiple-files-in-a-directory-in-python
import os
fullPathArray = [r'F:\Multimedia_Projects\2022\2022-03-21-Roadtrip-Manali-to-Dheradun-Night-Driving\Videos'] #Test

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
            # For every file...
            newFileName = fileName.replace("Dheradun","Dehradun") # Undo bad naming
            os.rename(fileName, newFileName)
            print("["+fileName+"] was renamed to ["+newFileName+"]")
            # if os.path.getsize(fileName)>1000000:
            #     # Re-name mp4 files
            #     fileNameWithoutExt = fileName.replace("M01.XML","").replace(".mp4","").replace("-"+parent2FolderName.upper(),"")
            #     fileNameExt = ".mp4"
            #     newFileName = fileNameWithoutExt+"-"+parent2FolderName+fileNameExt
            #     newFileName = fileName.replace("-"+parent2FolderName.upper(),"") # Undo bad naming
            #     # newFileName = newFileName.replace(".mp4","M01.XML") # Undo bad naming
            #     os.rename(fileName, newFileName)
            #     print("["+fileName+"] was renamed to ["+newFileName+"]")
            # elif os.path.getsize(fileName)<1000000:
            #     # Re-name xml files
            #     fileNameWithoutExt = fileName.replace("M01.XML","").replace(".mp4","").replace("-"+parent2FolderName.upper(),"")
            #     fileNameExt = "M01.XML"
            #     newFileName = fileNameWithoutExt+"-"+parent2FolderName+fileNameExt
            #     newFileName = fileName.replace("Dheradun","Dheradun") # Undo bad naming
            #     # newFileName = newFileName.replace(".mp4","M01.XML") # Undo bad naming
            #     os.rename(fileName, newFileName)
            #     print("["+fileName+"] was renamed to ["+newFileName+"]")
            # else:
            #     print("!!!!!!!!!!["+fileName+"] was not a recognized video, photo or audio file and was NOT renamed !!!!!!!!!!")
from fileinput import filename
import dropbox
import os
from dropbox.file import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            locals_path=os.path.join(root,filename)
            relative_path=os.path.relpath(locals_path,file_from)
            dropbox_path = os.path.join(file_to,relative_path)
            with open(locals_path,'rb') as f:
                dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BMA7dQbXlXPvssfvCQO9uDo2kezT3A5Ck4T8G8R-qYGE_8K1ROkzHaYkGwbAtUt7FY8qLHIx97SmWX6NIquFvLsOdnuNPeFcKofMYGOIl35XptQW9y1ok5w--iaqSYPEVl8hlg4RBRzM'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
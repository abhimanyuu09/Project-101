import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        for root, dirs, files in os.walk(file_from):

            for filename in files:

                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.A_5KMiu05r2cSwqJFDuDyYzNR-BZnEezIzbZtA2o5lPcWV6vLt4tze_TscjwYcdLR2PNiYbZ215IimmQSq-f_-Pq_K_PnWNpYp153fbIUx0AjP-o81ErdTow20I9kSEYl76Wtbg'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path\n"))
    file_to = input("Enter the full path to upload\n")

    transferData.upload_file(file_from,file_to)
    print("The File has been uploaded")

main()

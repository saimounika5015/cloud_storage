import dropbox


class TransferData:
    def __init__(self,accesstoken):
        self.access_token=accesstoken

    def uploadFiles(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = "iuXscf5hZAAAAAAAAAAAAWuLU6_31RukQBj7rE1VAaBetdKrTa9I1CtAZLvJI89v"
    transferData = TransferData(access_token)
    file_from = input("enter file to be uploaded...........")
    file_to = input("Enter full path to upload in DropBox .........")

    transferData.uploadFiles(file_from, file_to)
    print("Files has been moved")

main()
import dropbox
import os


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path,
                                     mode=dropbox.files.WriteMode.overwrite)

        # for root, dirs, files in os.walk(file_from):
        #    relative_path = os.path.relpath(file_from, os.curdir)
        #    dropbox_path = os.path.join(file_to, relative_path)
        #    with open(file_from, 'rb') as f:
        #        dbx.files_upload(f.read(), dropbox_path,
        #                         mode=dropbox.files.WriteMode.overwrite)
        # if os.path.exists(file_from):
        #    for currentPath, directories, files in os.walk(file_from):
        #        for i in directories:
        #            folderPath = os.path.join(currentPath, i)
        #
        #                shutil.rmtree(folderPath)
        #        for j in files:
        #            filePath = os.path.join(currentPath, j)
        #
        #                os.remove(filePath)

        # else:
        #    print("This path is not found!")


def main():
    access_token = 'sl.Ax6Syey0GgVHvdic7pkW4ZOjCPVjR8UK3cubcKFFfqeh5CwAqahnStlZW1pXt3BsK5KYR7G08K3G4TGxQvzak_7iIeZMEYz-YxUF3eKisxqzu54x1oIG5jVpYSV_qUyWN5eo9crFqUc'
    transferData = TransferData(access_token)

    file_from = input("Enter the path of the file to upload: ")
    file_to = input("Enter the path of the dropbox repository: ")
    transferData.upload_file(file_from, file_to)


if __name__ == '__main__':
    main()

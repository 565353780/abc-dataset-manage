import os
import py7zr


def unzip7ZFile(zipped_file_path: str, unzipped_folder_path: str) -> bool:
    if not os.path.exists(zipped_file_path):
        print("[ERROR][io::unzip7ZFile]")
        print("\t zipped file not exist!")
        print("\t zipped_file_path:", zipped_file_path)
        return False

    print("[INFO][unzip::unzip7ZFile]")
    print("\t start unzip :", zipped_file_path, "...")
    with py7zr.SevenZipFile(zipped_file_path, mode="r") as archive:
        archive.extractall(path=unzipped_folder_path)
    return True

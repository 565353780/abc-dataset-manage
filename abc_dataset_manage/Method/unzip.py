import os
import py7zr
import shutil
from tqdm import tqdm

from abc_dataset_manage.Method.path import createFileFolder


def unzip7ZFile(zipped_file_path: str, unzipped_folder_path: str) -> bool:
    if not os.path.exists(zipped_file_path):
        print("[ERROR][io::unzip7ZFile]")
        print("\t zipped file not exist!")
        print("\t zipped_file_path:", zipped_file_path)
        return False

    tmp_unzipped_folder_path = unzipped_folder_path[:-1] + "_tmp/"

    with py7zr.SevenZipFile(zipped_file_path, mode="r") as archive:
        all_files = archive.getnames()
        with tqdm(total=len(all_files), desc="Unzip", unit="file") as pbar:
            for rel_path in all_files:
                unzipped_file_path = os.path.join(unzipped_folder_path, rel_path)
                if os.path.exists(unzipped_file_path):
                    pbar.update(1)
                    continue

                archive.extract(targets=[rel_path], path=tmp_unzipped_folder_path)

                tmp_unzipped_file_path = os.path.join(
                    tmp_unzipped_folder_path, rel_path
                )
                if os.path.exists(tmp_unzipped_file_path):
                    if os.path.isfile(tmp_unzipped_file_path):
                        createFileFolder(unzipped_file_path)
                        shutil.move(tmp_unzipped_file_path, unzipped_file_path)
                    else:
                        os.makedirs(unzipped_file_path, exist_ok=True)

                pbar.update(1)
    return True

import os
from typing import Union

from abc_dataset_manage.Method.unzip import unzip7ZFile


class Unzipper(object):
    def __init__(
        self,
        dataset_root_folder_path: str,
    ) -> None:
        self.dataset_root_folder_path = dataset_root_folder_path
        if self.dataset_root_folder_path[-1] != "/":
            self.dataset_root_folder_path += "/"

        assert self.update()
        return

    def update(self) -> bool:
        if not os.path.exists(self.dataset_root_folder_path):
            print("[ERROR][Unzipper::update]")
            print("\t dataset not found!")
            print("\t dataset_root_folder_path:", self.dataset_root_folder_path)
            return False

        all_data_folder_path = self.dataset_root_folder_path + "all/"
        if not os.path.exists(all_data_folder_path):
            print("[ERROR][Unzipper::update]")
            print("\t all data not found!")
            print("\t all_data_folder_path:", all_data_folder_path)
            return False

        self.all_data_folder_path = all_data_folder_path
        return True

    def getZippedFilePath(self, tag: str, data_idx: int) -> Union[str, None]:
        zipped_file_path = (
            self.all_data_folder_path
            + "abc_"
            + str(data_idx).zfill(4)
            + "_"
            + tag
            + "_v00.7z"
        )

        if not os.path.exists(zipped_file_path):
            print("[ERROR][Unzipper::getZippedFilePath]")
            print("\t zipped file not exist!")
            print("\t zipped_file_path:", zipped_file_path)
            return None

        return zipped_file_path

    def unzip(self, tag: str, data_idx: int) -> bool:
        zipped_file_path = self.getZippedFilePath(tag, data_idx)
        if zipped_file_path is None:
            print("[ERROR][Unzipper::unzip]")
            print("\t getZippedFilePath failed!")
            return False

        unzipped_folder_path = self.dataset_root_folder_path + "unzipped/" + tag + "/"

        unzip7ZFile(zipped_file_path, unzipped_folder_path)
        return True

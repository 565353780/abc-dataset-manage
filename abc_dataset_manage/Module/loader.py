import os
import yaml
import open3d as o3d
from typing import Union


class Loader(object):
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
            print("[ERROR][Loader::update]")
            print("\t dataset not found!")
            print("\t dataset_root_folder_path:", self.dataset_root_folder_path)
            return False

        unzipped_folder_path = self.dataset_root_folder_path + "unzipped/"
        if not os.path.exists(unzipped_folder_path):
            print("[ERROR][Loader::update]")
            print("\t unzipped data not found!")
            print("\t unzipped_folder_path:", unzipped_folder_path)
            return False

        self.unzipped_folder_path = unzipped_folder_path
        return True

    def getUnzippedFilePath(self, tag: str, data_idx: int) -> Union[str, None]:
        data_folder_path = (
            self.unzipped_folder_path + tag + "/" + str(data_idx).zfill(8) + "/"
        )

        if not os.path.exists(data_folder_path):
            print("[ERROR][Loader::getUnzippedFilePath]")
            print("\t data folder not exist!")
            print("\t data_folder_path:", data_folder_path)
            return None

        data_filename_list = os.listdir(data_folder_path)
        if len(data_filename_list) == 0:
            return None

        unzipped_file_path = data_folder_path + data_filename_list[0]
        return unzipped_file_path

    def loadObj(self, data_idx: int) -> o3d.geometry.TriangleMesh:
        obj_file_path = self.getUnzippedFilePath("obj", data_idx)
        if obj_file_path is None:
            print("[ERROR][Loader::loadObj]")
            print("\t getUnzippedFilePath failed!")
            return False

        mesh = o3d.io.read_triangle_mesh(obj_file_path)
        return mesh

    def loadFeat(self, data_idx: int) -> Union[dict, None]:
        feat_file_path = self.getUnzippedFilePath("feat", data_idx)
        if feat_file_path is None:
            print("[ERROR][Loader::loadFeat]")
            print("\t getUnzippedFilePath failed!")
            return None

        with open(feat_file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return data

    def load(
        self, tag: str, data_idx: int
    ) -> Union[o3d.geometry.TriangleMesh, dict, None]:
        if tag == "feat":
            return self.loadFeat(data_idx)
        if tag == "obj":
            return self.loadObj(data_idx)

        print("[ERROR][Loader::load]")
        print("\t loading algo for [", tag, "] not defined!")
        return None

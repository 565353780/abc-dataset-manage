from abc_dataset_manage.Module.unzipper import Unzipper


def demo():
    dataset_root_folder_path = "/home/chli/chLi/Dataset/ABC/"

    unzipper = Unzipper(dataset_root_folder_path)

    unzipper.unzip("obj", 0)
    unzipper.unzip("feat", 0)

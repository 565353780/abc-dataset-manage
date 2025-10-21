from abc_dataset_manage.Module.loader import Loader


def demo():
    dataset_root_folder_path = "/home/chli/chLi/Dataset/ABC/"

    loader = Loader(dataset_root_folder_path)

    mesh = loader.load("obj", 2)
    feat = loader.load("feat", 2)

    print(mesh)
    print(feat)

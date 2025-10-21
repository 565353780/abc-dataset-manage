import open3d as o3d

from abc_dataset_manage.Method.render import getLabeledSurfacesMesh
from abc_dataset_manage.Module.loader import Loader


def demo():
    dataset_root_folder_path = "/home/chli/chLi/Dataset/ABC/"

    loader = Loader(dataset_root_folder_path)

    mesh = loader.load("obj", 2)
    feat_dict = loader.load("feat", 2)
    assert feat_dict is not None

    labeled_surface_mesh = getLabeledSurfacesMesh(mesh, feat_dict)

    print(mesh)

    o3d.visualization.draw_geometries([labeled_surface_mesh])

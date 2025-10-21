import numpy as np
import open3d as o3d

from abc_dataset_manage.Method.feat import getSurfaceTrianglesList


def toColoredTriangleSoup(
    mesh: o3d.geometry.TriangleMesh, colors: np.ndarray
) -> o3d.geometry.TriangleMesh:
    """
    将 mesh 转成 triangle soup，使每个三角面片都能独立染色
    :param mesh: 原始 TriangleMesh
    :param colors: (num_triangles, 3) 每个三角面的颜色，RGB 0~1
    :return: 新的 TriangleMesh，每个三角面片独立顶点
    """
    assert colors.shape[0] == len(mesh.triangles), "颜色数量必须和三角面片数量一致"

    triangles = np.asarray(mesh.triangles)
    vertices = np.asarray(mesh.vertices)

    new_vertices = []
    new_triangles = []
    new_colors = []

    for i, tri in enumerate(triangles):
        # tri 是顶点索引 [v0, v1, v2]
        v0, v1, v2 = vertices[tri[0]], vertices[tri[1]], vertices[tri[2]]

        # 添加到新顶点列表
        idx0 = len(new_vertices)
        new_vertices.append(v0)
        new_vertices.append(v1)
        new_vertices.append(v2)

        # 三角索引
        new_triangles.append([idx0, idx0 + 1, idx0 + 2])

        # 对应颜色
        c = colors[i]
        new_colors.extend([c, c, c])

    # 构建新的 mesh
    new_mesh = o3d.geometry.TriangleMesh()
    new_mesh.vertices = o3d.utility.Vector3dVector(np.array(new_vertices))
    new_mesh.triangles = o3d.utility.Vector3iVector(np.array(new_triangles))
    new_mesh.vertex_colors = o3d.utility.Vector3dVector(np.array(new_colors))

    return new_mesh


def getLabeledSurfacesMesh(
    mesh: o3d.geometry.TriangleMesh,
    feat_dict: dict,
) -> bool:
    triangle_num = len(mesh.triangles)

    surface_triangles_list = getSurfaceTrianglesList(feat_dict)
    label_num = len(surface_triangles_list)
    random_colors = np.random.rand(label_num + 1, 3)
    random_colors[0, :] = 0

    triangle_labels = np.zeros(triangle_num, dtype=np.int64)

    for i, surfaec_triangles in enumerate(surface_triangles_list):
        triangle_labels[surfaec_triangles] = i + 1

    triangle_colors = random_colors[triangle_labels]

    labeled_surfaces_mesh = toColoredTriangleSoup(mesh, triangle_colors)
    return labeled_surfaces_mesh

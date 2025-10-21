def getSurfaceTrianglesList(feat_dict: dict) -> list:
    surface_triangles_list = []

    surfaces = feat_dict["surfaces"]

    for surface in surfaces:
        surface_triangles = surface["face_indices"]

        surface_triangles_list.append(surface_triangles)

    return surface_triangles_list

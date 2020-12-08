import os
import numpy as np
import cv2
from libs.plyClassVer2 import Ply

# mesh1とmesh2_1を作成
# mesh1の透明度を上げる
# mesh1とmesh2_1を統合

sameMin = []
sameMax = []


def flatten(list):
    flattenArray = np.ravel(np.array(list))
    return flattenArray


def setMinMax(array):  # 最初のmeshの最大最小を覚えておくという関数
    global sameMax, sameMin
    for i in range(3):
        if len(sameMax) < 4:
            sameMax.append(np.max(array[:, i]))
            sameMin.append(np.min(array[:, i]))


def mmNormal(array):
    setMinMax(array)
    scale = 0.5
    dst = np.zeros(array.shape)
    for i in range(3):
        for line in range(array.shape[0]):
            dst[line][i] = (
                scale
                * float(array[line][i] - sameMin[i])
                / float(sameMax[i] - sameMin[i])
                - scale / 2.0
            )
    return dst


def setVerts(mesh_fi):
    mesh = Ply(mesh_fi=mesh_fi)
    mesh.setInfos()
    mesh.changeAlpha(alpha=255)
    verts_np = mesh.verts_np
    colors_np = mesh.colors_np
    verts_np = mmNormal(verts_np)
    vertices = flatten(verts_np)
    colors = flatten(colors_np / 255.0)
    return colors, vertices


if __name__ == "__main__":
    mesh_fi = "./mesh/IMG_4652.ply"
    setVerts(mesh_fi)

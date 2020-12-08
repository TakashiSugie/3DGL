from libs.plyClassVer2 import Ply

mesh_fi = "./mesh/IMG_4653.ply"
# mesh_fi = "./mesh/moon.ply"

if __name__ == "__main__":
    mesh = Ply(mesh_fi=mesh_fi)
    print(mesh.setAlpha)
    print(mesh.colors_np.shape)
    mesh.changeAlpha(alpha=128)
    print(mesh.colors_np[0:10])
    # print("sdas")

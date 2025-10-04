#

## geant4 安装

### 从源码构建

目录机构为
```
geant4
    build
    install
```

cd ~/Software/geant4/build

cmake -DGEANT4_USE_GDML=ON \
      -DGEANT4_USE_OPENGL_X11=ON \
      -DGEANT4_USE_RAYTRACER_X11=ON \
      -DGEANT4_INSTALL_DATA=ON \
      -DGEANT4_BUILD_MULTITHREADED=ON \
      -DCMAKE_INSTALL_PREFIX=~/Software/geant4/install \
      -DXERCESC_ROOT_DIR=~/Software/geant4/xerces-c-3.2.4 \
      ~/Software/geant4/geant4-v11.1.2

make -j$(nproc)
make install



## root安装


### 从源码构建

有预编译版本 直接下载压缩包解压即可。
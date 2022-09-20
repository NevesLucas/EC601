## Project 1

# Photogrammetry
## Lucas Neves

### Problem

Photogrammetry is the process of reconstructing a three-dimensional scene form two dimensional image data. It is a very computational and data intensive process that requires multiple images of the scene with varying perspectives in order to establish a depth map for the scene. It has a variety of applications from ground surveying, cartography, archeology, civil engineering, art, game asset acquisition, visual effects, etc.
The photogrammetry pipeline is a multi-step process, encompassing [1]:
1.	Image feature extraction 
2.	Image matching (find images that look at the same area of a scene)
3.	Feature matching
4.	Structure from Motion 
5.	Depth map estimation
6.	Camera localization.
7.	Meshing
8.	Texturing

The traditional photogrammetry pipeline is a computationally intensive and delicate process, requiring substantial amounts of clean, sharp source images. This makes data collection time intensive, as potentially thousands of images must be captured to allow for reliable, accurate scene reconstruction.cTotal runtime is dependent on the number of images captured, requiring large amounts of available memory to handle the matching of thousands of source images[2].


### Solutions

The most popular open source photogrammetric tool is the AliceVision[1] framework, which provies all the phases of the reconstruction pipeline, and is reasonably accelerated through CUDA. The next most popular photogrammetric tool is COLMAP[3], which implements the majority of the pipeline, except the meshing and texturing phases, and is also CUDA accelerated. Unfortunately, CUDA is not a portable framework for GPU acceleration, and so this greatly restricts the userbase that can use these tools effectively. Some efforts have been made to increase their portability[4], however no truly portable open source implementation currently exists.

### Current Research

To reduce the computation costs with the traditional photogrammetry pipeline, Nekrasov et al[5] proposes a deep learning based approach that uses prior knowledge of known object classes to infer the depth map of a scene from a semantically segmented image. This technique replaces the need to capture images from multiple angles to reconstruct an object, leveraging prior knowledge of how an object _should_ look to remove the need to do an exhaustive pointcloud reconstruction.

Mildenhall et al[6] proposes a novel technique for representing scenes using Deep learning, replacing the majority of the photogrammetry pipeline, with the exception of the feature extration and image matching phase. From these registered, localized images, the Neural network not only represents the 3d data of a scene, but also its _density_ allowing for accurate reconstruction of the lighting conditions of a captured scene, handling reflections and transparencies accurately through a combination of raytracing with deep learning approach, something traditional photogrammetry struggles with.

### References

- [1] https://alicevision.org
- [2] González-Aguilera, D., et al. "Development of an all-purpose free photogrammetric tool." The International Archives of Photogrammetry, Remote Sensing and Spatial Information Sciences 41 (2016): 31.
- [3] https://colmap.github.io/
- [4] https://github.com/alicevision/Meshroom/issues/595

- [5] Nekrasov, Vladimir, et al. "Real-time joint semantic segmentation and depth estimation using asymmetric annotations." 2019 International Conference on Robotics and Automation (ICRA). IEEE, 2019.
- [6] Mildenhall, Ben, et al. "Nerf: Representing scenes as neural radiance fields for view synthesis." Communications of the ACM 65.1 (2021): 99-106. https://arxiv.org/abs/2003.08934
# deepstream-example

A brief description of how to use deepstream 6.1 with Yolo V5.
This repo based on multiple blogposts:
- [NVIDIA Deepstream Quickstart](https://blog.ml6.eu/nvidia-deepstream-quickstart-9147dd49a15d)
- [Getting started with custom NVIDIA Deepstream 6.0 pipelines in Python](https://blog.ml6.eu/getting-started-with-custom-nvidia-deepstream-6-0-pipelines-in-python-935154dd9237)

Here implemented two pipelines - with and without tiling. Both pipeline process video files and produce resulting videos with detections. Also, the pipeline use different trackers:
- NvDCF - python based pipeline with tiling
- DeepSORT - C++ based pipeline without tiling

## Configs
The config files placed in `deepstream-example/configs`
- Detector: `yolov5.txt`
- Trackers
    * NvDCF: `nvdcf.txt`, `tracker_config.yml`
    * DeepSORT: `DeepSORT_config.yml`
- Preprocess(tiler): `preprocess.txt`
- Whole pipeline: `pipeline.txt`


## Steps
0. Clone the repo and init submodules
```
git clone https://github.com/klymya/deepstream-example.git && cd deepstream-example && git git submodule init
```

1. Download and convert yolov5 weights. The instruction and script for this are [here](https://github.com/marcoslucianops/DeepStream-Yolo/blob/master/docs/YOLOv5.md). Put the conversion artifats(`.cfg` and `.wts` files) to `deepstream-example/weights`.

2. Build the docker image with required environment
```
docker build . -t deepstream-example
```

3. Run the docker container
```
docker run -it --rm --gpus all -v ${PWD}:/app -w /app deepstream-example bash
```

4. Run examples
    1. Python pipeline with tiling
    ```
    export PYTHONPATH=/app/code/boilerplate/deepstream && python3 code/main.py
    ```
    2. C++ pipeline
    ```
    deepstream-app -c configs/pipeline.txt
    ```
Tiling links:
- https://developer.nvidia.com/blog/applying-inference-over-specific-frame-regions-with-nvidia-deepstream/
- https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_plugin_gst-nvdspreprocess.html


Other useful links:
- https://github.com/marcoslucianops/DeepStream-Yolo
- https://github.com/ml6team/deepstream-python
- https://github.com/NVIDIA-AI-IOT/deepstream_python_apps



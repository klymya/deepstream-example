import argparse

from pipeline import PipelineWithTiling

INPUT_PATH = 'file:/opt/nvidia/deepstream/deepstream/samples/streams/sample_720p.h264'
OUTPUT_PATH = 'out_tiling.mp4'
PGIE_PATH = '/app/configs/yolov5.txt'
TRACKER_PATH = '/app/configs/nvdcf.txt'
PREPROCESS_PATH = '/app/configs/preprocess.txt'
INPUT_SIZE = '1920,1088'


def main():
    parser = argparse.ArgumentParser(description='Deepstream pipeline')
    parser.add_argument(
        '--input', '-i', type=str,
        help=f'Url to input video, e.g. file:/.... Default={INPUT_PATH}',
        default=INPUT_PATH
    )
    parser.add_argument(
        '--output', '-o', type=str,
        help=f'Path to resulting video. Default={OUTPUT_PATH}',
        default=OUTPUT_PATH
    )
    parser.add_argument(
        '--pgie', type=str,
        help=f'Path to pgie plugin confi file. Default={PGIE_PATH}',
        default=PGIE_PATH
    )
    parser.add_argument(
        '--tracker', type=str,
        help=f'Path to tracker plugin confi file. Default={TRACKER_PATH}',
        default=TRACKER_PATH
    )
    parser.add_argument(
        '--preprocess', type=str,
        help=f'Path to preprocess plugin confi file. Default={PREPROCESS_PATH}',
        default=PREPROCESS_PATH
    )
    parser.add_argument(
        '--imgz', type=str,
        help=f'Input image size W,H. Default={INPUT_SIZE}',
        default=INPUT_SIZE
    )
    args = parser.parse_args()

    pipeline = PipelineWithTiling(
        video_uri=args.input,
        output_video_path=args.output,
        pgie_config_path=args.pgie,
        tracker_config_path=args.tracker,
        preprocess_config_path=args.preprocess,
        input_shape=tuple(int(i) for i in args.imgz.split(','))
    )
    pipeline.run()


if __name__ == "__main__":
    main()

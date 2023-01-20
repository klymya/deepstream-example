import gi

gi.require_version('Gst', '1.0')
from gi.repository import Gst

from boilerplate.deepstream.app.pipeline import Pipeline


class PipelineWithTiling(Pipeline):
    def __init__(
        self, video_uri, output_video_path, pgie_config_path,
        tracker_config_path, preprocess_config_path, *args, **kwargs
    ):
        self.preprocess_config_path = preprocess_config_path

        super().__init__(
            video_uri=video_uri,
            output_video_path=output_video_path,
            pgie_config_path=pgie_config_path,
            tracker_config_path=tracker_config_path,
            *args, **kwargs
        )

    def _create_elements(self):
        super()._create_elements()
        self.pgie.set_property("input-tensor-meta", True)

        element_names = [elm.name for elm in self.elements]
        streammux_idx = element_names.index(self.streammux.name)

        self.preprocess = \
            Gst.ElementFactory.make("nvdspreprocess", "preprocess-plugin")
        self.preprocess.set_property(
            "config-file", self.preprocess_config_path)
        self._add_element(self.preprocess, streammux_idx + 1)

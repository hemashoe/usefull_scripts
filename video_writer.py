from threading import Thread
import cv2


class RTSPVideoWriterObject(object):
    def __init__(self, src=""):
        self.capture = cv2.VideoCapture(src)
        self.frame_width = int(self.capture.get(3))
        self.frame_height = int(self.capture.get(4))
        self.codec = cv2.VideoWriter_fourcc("M", "J", "P", "G")
        self.output_video = cv2.VideoWriter("output3.mp4", self.codec, 25, (
                self.frame_width, self.frame_height))
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()

    def show_frame(self):
        if self.status:
            cv2.imshow('frame', self.frame)

        key = cv2.waitKey(1)
        if key == ord("q"):
            self.capture.release()
            self.output_video.release()
            cv2.destroyAllWindows()
            exit(1)

    def save_frame(self):
        self.output_video.write(self.frame)


if __name__ == '__main__':
    rtsp_stream_link = ("Video")  # URL pf RTSP stream, or *.mp4* file
    video_stream_widget = RTSPVideoWriterObject(rtsp_stream_link)
    while True:
        try:
            video_stream_widget.show_frame()
            video_stream_widget.save_frame()
        except AttributeError:
            pass

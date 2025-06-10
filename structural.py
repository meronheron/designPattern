#proxy
#define class which represents the real object responsible for streaming videos
class VideoStreamer:
    def stream_video(self, video_name):
        # simulate streaming a video
        return f"Streaming '{video_name}' in high quality!"
# Proxy that controls access to the video streamer
class VideoStreamerProxy:
    def __init__(self, is_premium_user): # whether the user is a premium subscrption
        self.is_premium_user = is_premium_user
        # Create the real video streamer
        self.video_streamer = VideoStreamer()
    def stream_video(self, video_name):
        # check if the user is a premium subscriber
        if not self.is_premium_user:
            return "Error: You need a premium subscription to stream videos!"
        # if it's premium, delegate to the real streamer
        return self.video_streamer.stream_video(video_name)
if __name__ == "__main__":
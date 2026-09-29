import os
from trackers import Tracker
from utils import read_video, save_video, get_video_fps

VIDEO_PATH = 'input_videos/cobaia.mp4'

os.makedirs('stubs', exist_ok=True)

video_name = os.path.splitext(os.path.basename(VIDEO_PATH))[0]

# extrair frames do vídeo
video_frames = read_video(VIDEO_PATH)


tracker = Tracker('models/best.pt')

tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path=f'stubs/track_stubs_{video_name}.pkl')

os.makedirs('output_videos', exist_ok=True)

output_video_frames = tracker.draw_tracks(video_frames, tracks)

# salvar vídeo
save_video(output_video_frames, 
           f'output_videos/tracking_{video_name}.mp4', 
           fps=get_video_fps(VIDEO_PATH),
           show=True
        )
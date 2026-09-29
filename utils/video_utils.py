import os
import time
import cv2


def read_video(video_path, max_frames=None):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frames.append(frame)
        if max_frames is not None and len(frames) >= max_frames:
            break
    cap.release()
    return frames



def get_video_fps(video_path, default=0.25):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()
    return fps if fps and fps > 0 else default

def _window_is_open(window_name):
    try:
        return cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) >= 1
    except cv2.error:
        return False

def save_video(output_video_frames, output_video_path, fps=25, show=False, window_name="Football Analysis"):
    if not output_video_frames:
        return

    codec = 'mp4v' if os.path.splitext(output_video_path)[1].lower() == '.mp4' else 'XVID'
    fourcc = cv2.VideoWriter_fourcc(*codec)
    height, width = output_video_frames[0].shape[:2]
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    if not out.isOpened:
        raise RuntimeError(f"Não foi possível fravar em {output_video_path} (codec {codec})")

    showing = show

    if showing:
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(window_name, width, height)

    start = time.perf_counter()

    try:

        for frame_num, frame in enumerate(output_video_frames):
            out.write(frame)

            if not showing: 
                continue

            cv2.imshow(window_name, frame)

            remaining_ms = int(((frame_num + 1) / fps - (time.perf_counter() - start)) * 1000)

            key = cv2.waitKey(max(1, remaining_ms)) & 0xFF

            if key == ord(' '):
                while True:
                    key = cv2.waitKey(50) & 0xFF
                    if key in (ord(' '), ord('q'), 27) or not _window_is_open(window_name):
                        break
                start = time.perf_counter() - (frame_num + 1) / fps

            if key in (ord('q'), 27) or not _window_is_open(window_name):
                showing = False
                cv2.destroyAllWindows(window_name)
                cv2.waitKey(1)
    finally:
        out.release()
        if show:
            cv2.destroyAllWindows()
            cv2.waitKey(1)





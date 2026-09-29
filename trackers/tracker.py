from ultralytics import YOLO
from supervision import sv
import pickle
import os
import cv2

class Tracker:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.tracker = sv.ByteTrack()

    def detect_frames(self, frames):
        batch_size = 20
        detections = []
        for i in range(0, len(frames), batch_size):
            detections_batch = self.model.predict(frames[i:i+batch_size], conf=0.1)
            detections += detections_batch
        return detections

    def get_object_tracks(self, frames, read_from_stub=False, stub_path=None):
        if read_from_stub and stub_path is not None and os.path.exists(stub_path):
            with open(stub_path, 'rb') as f:
                tracks = pickle.load(f)

            return tracks

        detections = self.detect_frames(frames)

        tracks = {
            "players": [],
            "referees": [],
            "ball": []
        }

        for frame_num, detection in enumerate(detections):
            cls_names = detection.names
            cls_names_inv = {v: k for k, v in cls_names.items()}


            detection_supervision = sv.Detections.from_ultralytics(detection)

            for object_ind, class_id in enumerate(detection_supervision.class_id):
                if cls_names[class_id] == "goalkeeper":
                    detection_supervision.class_id[object_ind] = cls_names_inv["player"]

            # rastreando objetos
            detection_with_tracks = self.tracker.update_with_detections(detection_supervision)

            tracks["players"].append({})
            tracks["referees"].append({})
            tracks["ball"].append({})

            for frame_detection in detection_with_tracks:
                bbox = frame_detection[0].tolist()
                cls_id = frame_detection[3]
                track_id = frame_detection[4]

                if cls_id == cls_names_inv["player"]:
                    tracks["players"][frame_num][track_id] = {
                        "bbox": bbox,
                    }

                if cls_id == cls_names_inv["referee"]:
                    tracks["referees"][frame_num][track_id] = {
                        "bbox": bbox,
                    }


            for frame_detection in detection_supervision:
                bbox = frame_detection[0].tolist()
                cls_id = frame_detection[3]

                if cls_id == cls_names_inv["ball"]:
                    tracks["ball"][frame_num][1] = {
                        "bbox": bbox
                    }

        if stub_path is not None:
            with open(stub_path, 'wb') as f:
                pickle.dump(tracks, f)

        return tracks


    def draw_box(self, frame, bbox, color, label=None, thickness=2):
        x1, y1, x2, y2 = [int(v) for v in bbox]

        cv2.rectangle(frame, (x1, y1), (x2, y2), color, thickness)

        if label is not None:
            cv2.putText(frame, label, (x1, y1 - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        return frame

    def draw_tracks(self, video_frames, tracks):
        output_video_frames = []
        for frame_num, frame in enumerate(video_frames):
            frame = frame.copy()
            for track_id, player in tracks["players"][frame_num].items():
                self.draw_box(frame, player["bbox"], (0, 0, 255), str(track_id))

            for track_id, referee in tracks["referees"][frame_num].items():
                self.draw_box(frame, referee["bbox"], (0, 255, 255), str(track_id), str(track_id))

            for _, ball in tracks["ball"][frame_num].items():
                self.draw_box(frame, ball["bbox"], (0, 255, 0))

            hud = f"frame {frame_num} jogadores {len(tracks["players"][frame_num])}"
            cv2.putText(frame, hud, (20, 44), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)

            output_video_frames.append(frame)

        return output_video_frames

            


    
   





    
from sahi import AutoDetectionModel
from sahi.predict import get_sliced_prediction
from sahi.utils.cv import read_image

# Load YOLO model
detection_model = AutoDetectionModel.from_pretrained(
    model_type="ultralytics",
    model_path="best.pt",
    confidence_threshold=0.3,
    device="cuda",
    image_size=2030,
)

# Perform detection with adjusted slicing parameters
# Using larger slices (e.g., 512x512) and a greater overlap
result = get_sliced_prediction(
    image="img/img1.jpg",
    detection_model=detection_model,
    slice_height=512,  # Increased slice height
    slice_width=512,   # Increased slice width
    overlap_height_ratio=0.3, # Increased overlap
    overlap_width_ratio=0.3,  # Increased overlap
)

# Export the results
result.export_visuals(export_dir="demo_data/")
print("Kết quả đã lưu tại: demo_data/prediction_visual.png")
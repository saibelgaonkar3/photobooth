# Personal Photobooth with Face Filter Overlay

This is a fun personal photobooth app built using Python, OpenCV, and cvzone. It detects a face using the webcam, overlays a transparent PNG image (like glasses or hats), and allows users to take a snapshot with a countdown timer.

## Features

* Real-time webcam feed with face detection
* Automatically overlays a PNG filter (e.g., sunglasses) over the eyes
* 3-second countdown before taking a snapshot
* Saves the snapshot as a JPG file with a timestamped filename
* Press `s` to start the countdown, `q` to quit

## Requirements

Install the following Python libraries:

```bash
pip install opencv-python cvzone
```

## Project Structure

```
├── photobooth.py           # Main application script
├── glasses.png             # Overlay image (transparent PNG)
├── snapshots/              # Saved snapshots (auto-created)
```

## How to Run

1. Place your transparent PNG (like `glasses.png`) in the project folder.
2. Run the script:

```bash
python photobooth.py
```

3. Press `s` to take a snapshot (3-second countdown).
4. Press `q` to quit.

## Notes

* You can replace `glasses.png` with any transparent PNG image.
* Snapshots are saved in the same directory with filenames like `snapshot_1722091711.jpg`.

## Future Ideas

* Add multiple overlays (e.g., hats, masks)
* Use filters (like grayscale, sepia)
* Add GUI controls using Tkinter or PyQt

import cv2
import cvzone
import time

# Load overlay image (PNG with transparency)
overlay_img = cv2.imread("C:\Users\Sai\Downloads\glasses.png", cv2.IMREAD_UNCHANGED)

# Initialize camera
cap = cv2.VideoCapture(0)
detector = cvzone.FaceMeshDetector(maxFaces=1)

countdown = 0
snapshot_taken = False

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]
        left_eye = face[145]
        right_eye = face[374]

        # Calculate width of overlay
        overlay_width = int(abs(right_eye[0] - left_eye[0]) * 2)
        overlay_height = int(overlay_width * overlay_img.shape[0] / overlay_img.shape[1])
        center_x = (left_eye[0] + right_eye[0]) // 2
        center_y = (left_eye[1] + right_eye[1]) // 2

        top_left = (int(center_x - overlay_width // 2), int(center_y - overlay_height // 2))

        img = cvzone.overlayPNG(img, overlay_img, top_left, scale=overlay_width / overlay_img.shape[1])

    # Display countdown if needed
    if countdown > 0:
        cv2.putText(img, str(countdown), (300, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 5)
        time.sleep(1)
        countdown -= 1
        if countdown == 0:
            snapshot_taken = True

    # Save snapshot
    if snapshot_taken:
        filename = f"snapshot_{int(time.time())}.jpg"
        cv2.imwrite(filename, img)
        print(f"Saved: {filename}")
        snapshot_taken = False

    cv2.imshow("Snapchat Photobooth", img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('s'):  # Start snapshot with countdown
        countdown = 3

cap.release()
cv2.destroyAllWindows()

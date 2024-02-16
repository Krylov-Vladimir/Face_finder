import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video = cv2.VideoCapture('test_video.mp4')

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter('output_video.mp4' , fourcc, 30.0, (int(video.get(3)), int(video.get(4))))

while video.is0pend():
    ret, frame = video.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor: 1.3, minNeighbors: 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+ h), (255, 0, 0), 2)
    output_video.write(frame)
    cv2.imshow(winname 'Video', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    video.release()
    output_video.release()
    cv2.destroyAllWindows()    

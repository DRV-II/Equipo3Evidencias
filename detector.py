
# Diego
def detectar_cara():
    haar_file = 'haarcascade_frontalface_default.xml'

    face_cascade = cv2.CascadeClassifier(haar_file)
    webcam = cv2.VideoCapture(0)

    while True:
        (_, im) = webcam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x,y), (x+w, y+h), (163, 17, 6), 4)
        cv2.putText(im,'Face detected',(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
        cv2.imshow('OpenCV', im)
        
        key = cv2.waitKey(10)
        if key == 27:
            break
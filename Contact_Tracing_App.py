import cv2
from pyzbar import pyzbar

def decode_qrcode(frame):
    qrcodes = pyzbar.decode(frame)
    for code in qrcodes:
        x, y , w, h = code.rect
        qrcode_data = code.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)

        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, qrcode_data, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        with open("contact_tracing.txt", mode ='w') as file:
            file.write("DATA RETRIEVED:\n\n" + qrcode_data)
    return frame


def detect_qrcode():
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    while ret:
        ret, frame = camera.read()
        frame = decode_qrcode(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    detect_qrcode()

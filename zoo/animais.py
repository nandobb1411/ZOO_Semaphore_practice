import threading

import numpy
import time
import cv2 as cv

leao = cv.VideoCapture('/home/fernandobellelis/PycharmProjects/zoo/Videos_Animais/leão.mp4')
elefante = cv.VideoCapture('/home/fernandobellelis/PycharmProjects/zoo/Videos_Animais/elefante.mp4')

zooCap = [leao,
          elefante,
          "mico leão dourado",
          "tigre",
          "girafa",
          "orangotango",
          "canguru",
          "tartaruga",
          "cavalo",
          "cachorro caramelo",
          "penguin"
          ]
zooStr = [
    "leao",
    "elefante",
    "mico leão dourado",
    "tigre",
    "girafa",
    "orangotango",
    "canguru",
    "tartaruga",
    "cavalo",
    "cachorro caramelo",
    "penguin"
]


def alimentar(animalCap, animalStr):
    print("alimentando o " + animalStr)
    time.sleep(5)
    while True:
        isTrue, frame = animalCap.read()
        cv.imshow('Video', frame)

        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    animalCap.release()
    cv.destroyAllWindows()
    time.sleep(9)
    print(animalStr + " alimentado com sucesso")


alimentar(zooCap[1], zooStr[1])


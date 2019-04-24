#Criado por Vinicius Figueiredo 
#Em: 24/04/2019
#http://repositoriodebits.wordpress.com

import cv2
import imutils

#Inicializa a sua webcam.
#VideoCaputure precisa receber um índice, no caso 0 para a única webcam instalada no computador
#Caso tenha uma segunda webcam, mude o índice de 0 para 1. 
cap = cv2.VideoCapture(0)

while True:
    #fazendo a captura do fame da camera
    _, frame = cap.read()
    #redimensionando o frame 
    frame = imutils.resize(frame, width=420)
    #exibindo a imagem em uma janela
    cv2.imshow('Janela', frame)

    #pega da tecla que foi pressionada por 30ms
    key = cv2.waitKey(30)
    #Se a tecla pressionada for ESC, sai do while
    if key == 27:
        break

#Camera é liberada e não será mais usada.
cap.release()
#Todas as janelas serão encerradas.
cv2.destroyAllWindows()
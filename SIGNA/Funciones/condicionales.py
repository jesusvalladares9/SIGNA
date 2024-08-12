import cv2

def condicionalesLetras(dedos, frame):
    font = cv2.FONT_HERSHEY_SIMPLEX
    # A
    if dedos == [1, 1, 0, 0, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'A', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("A")
    # B
    elif dedos == [0, 0, 1, 1, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'B', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("B")
    # C
    elif dedos == [0, 1, 1, 0, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'C', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("C")
    # D
    elif dedos == [0, 0, 0, 0, 0, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'D', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("D")
    # E
    elif dedos == [1, 0, 0, 0, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'E', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("E")
    # F
    elif dedos == [1, 1, 1, 1, 1, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'F', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("F")
    # G
    elif dedos == [0, 1, 0, 0, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'G', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("G")
    # H
    elif dedos == [0, 1, 1, 0, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'H', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("H")
    # I
    elif dedos == [0, 0, 1, 0, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'I', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("I")
    # J
    elif dedos == [0, 0, 0, 1, 1, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'J', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("J")
    # K
    elif dedos == [0, 0, 0, 1, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'K', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("K")
    # L
    elif dedos == [1, 0, 1, 0, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'L', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("L")
    # M
    elif dedos == [0, 1, 1, 1, 1, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'M', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("M")
    # N
    elif dedos == [1, 1, 1, 1, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'N', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("N")
    # O
    elif dedos == [1, 0, 1, 1, 1, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'O', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("O")
    # P
    elif dedos == [0, 1, 1, 1, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'P', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("P")
    # Q
    elif dedos == [0, 1, 0, 0, 0, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'Q', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("Q")
    # R
    elif dedos == [0, 1, 1, 1, 0, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'R', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("R")
    # S
    elif dedos == [0, 0, 0, 0, 0, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'S', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("S")
    # T
    elif dedos == [0, 1, 1, 0, 0, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'T', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("T")
    # U
    elif dedos == [1, 1, 0, 1, 1, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'U', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("U")
    # V
    elif dedos == [0, 0, 1, 1, 0, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'V', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("V")
    # W
    #elif dedos == [1, 1, 1, 1, 1, 1]:
        #cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        #cv2.putText(frame, 'W', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        #print("W")
    # X
    elif dedos == [0, 1, 0, 0, 1, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'X', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("X")
    # Y
    elif dedos == [1, 0, 0, 0, 1, 0]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'Y', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("Y")
    # Z
    elif dedos == [1, 1, 1, 0, 0, 1]:
        cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
        cv2.putText(frame, 'Z', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
        print("Z")


    return dedos

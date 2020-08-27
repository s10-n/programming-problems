def clockAngle(hour,minute):
    angle = ((hour * 5) - minute) * 6
    if angle < 0:
       angle *= -1
    if angle > 180:
        angle = 360 - angle
    print('Angle: ' + str(angle) + ' degrees')
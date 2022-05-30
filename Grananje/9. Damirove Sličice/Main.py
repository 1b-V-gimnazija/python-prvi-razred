brojSlicica = int(input('? Broj Sličica: '))

if brojSlicica % 5 == 0:
    print(0)
elif brojSlicica == 1:
    print(4)
elif brojSlicica == 2:
    print(3)
elif brojSlicica % 5 == 1:
    print(-1)
elif brojSlicica % 5 == 2:
    print(-2)
elif brojSlicica % 5 == 3:
    print(2)
elif brojSlicica % 5 == 4:
    print(1)

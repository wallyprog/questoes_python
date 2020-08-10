# 1117
# while(True):
#     nota1 = float(input())
#     if nota1 < 0 or nota1 >10:
#         print("nota invalida")
#         continue
#     else:
#         while(1):
#             nota2 = float(input())
#             if nota2 < 0 or nota2 > 10:
#               print("nota invalida")
#             else:
#                 break
#     break
# media = (nota1+nota2)/2
# print("media = "+'{0:.2f}'.format(media))
# 1118
while(True):
    nota1 = float(input())
    if nota1 < 0 or nota1 > 10:
        print("nota invalida")
        continue
    else:
        while(1):
            nota2 = float(input())
            if nota2 < 0 or nota2 > 10:
                print("nota invalida")
            else:
                break
    media = (nota1+nota2)/2
    print("media = "+'{0:.2f}'.format(media))
    while(1):
        x = int(input("novo calculo (1-sim 2-nao)\n"))
        if x < 1 or x > 2:
            continue
        elif x == 1 or x == 2:
            break
    if x == 2:
        break

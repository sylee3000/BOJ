CY, SD = 100, 100
n = int(input())
for _ in range(n):
    cy_dice, sd_dice = map(int, input().split())
    if cy_dice < sd_dice:
        CY -= sd_dice
    elif cy_dice > sd_dice:
        SD -= cy_dice
print(CY)
print(SD)
word = "20260610_Deta_1459"

date = word[0:8]
deta = word[14:18]

deta_value = int(word[14:18])

new_deta = int(word[14:18]) * 2

print("日付：", date, "処理後データ：", new_deta)
print("abcdef".isalpha())
# output ➜ True, karena abcdef adalah alfabet


# --- source PDF text line 1577 ---
print("abc123".isalpha())
# output ➜ False, karena ada karakter 123 yang bukan merupakan alfabet


# --- source PDF text line 1581 ---
print("‫"موز‬.isalpha())
# output ➜ True, karena ‫ موز‬adalah abjad arabic


# --- source PDF text line 1585 ---
print("⯑⯑⯑".isalpha())
# output ➜ True, karena ⯑⯑⯑ adalah karakter jepang


# --- source PDF text line 1595 ---
print("123456".isdigit())
# output ➜ True, karena 123456 adalah digit


# --- source PDF text line 1599 ---
print("123abc".isdigit())
# output ➜ False, karena ada karakter abc yang bukan merupakan digit


# --- source PDF text line 1603 ---
print('2⅓'.isdigit())
# output ➜ False, karena bilangan pecahan memiliki karakter `/` yang
tidak termasuk dalam kategori digit


# --- source PDF text line 1608 ---
print('4²'.isdigit())
# output ➜ True, karena 4² adalah bilangan pangkat


# --- source PDF text line 1612 ---
print('٢٨'.isdigit())
# output ➜ True, karena ٢٨ adalah digit arabic


# --- source PDF text line 1616 ---
print('𝟜'.isdigit())
# output ➜ True, karena 𝟜 adalah digit


# --- source PDF text line 1627 ---
print("123456".isdecimal())
# output ➜ True, karena 123456 adalah angka desimal


# --- source PDF text line 1631 ---
print("123abc".isdecimal())
# output ➜ False, karena ada karakter abc yang bukan merupakan angka
desimal


# --- source PDF text line 1636 ---
print('2⅓'.isdecimal())
# output ➜ False, karena bilangan pecahan memiliki karakter `/` yang
tidak termasuk dalam kategori angka desimal


# --- source PDF text line 1641 ---
print('4²'.isdecimal())
# output ➜ False, karena bilangan pangkat yang tidak termasuk dalam
kategori angka desimal


# --- source PDF text line 1646 ---
print('٢٨'.isdecimal())
# output ➜ True, karena ٢٨ adalah angka desimal arabic


# --- source PDF text line 1650 ---
print('𝟜'.isdecimal())
# output ➜ True, karena 𝟜 adalah angka desimal


# --- source PDF text line 1661 ---
print("123456".isnumeric())
# output ➜ True, karena 123456 adalah angka numerik


# --- source PDF text line 1665 ---
print("123abc".isnumeric())
# output ➜ False, karena ada karakter abc yang bukan merupakan numerik


# --- source PDF text line 1674 ---
print("123abc".isalnum())
# output ➜ True, karena 123 adalah digit dan abc adalah alfabet


# --- source PDF text line 1678 ---
print("12345⅓".isalnum())
# output ➜ True, karena 12345⅓ adalah digit


# --- source PDF text line 1682 ---
print("abcdef".isalnum())
# output ➜ True, karena abcdef adalah alfabet


# --- source PDF text line 1686 ---
print("abc 12".isalnum())
# output ➜ False, karena ada karakter spasi yang bukan merupakan
karakter digit ataupun alfabet


# --- source PDF text line 1691 ---
print("‫"موز‬.isalnum())
# output ➜ True, karena ‫ موز‬adalah abjad arabic


# --- source PDF text line 1695 ---
print("⯑⯑⯑".isalnum())
# output ➜ True, karena ⯑⯑⯑ adalah karakter jepang

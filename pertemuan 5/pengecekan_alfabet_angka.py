print("abcdef".isalpha())
# output ➜ True, karena abcdef adalah alfabet

print("abc123".isalpha())
# output ➜ False, karena ada karakter 123 yang bukan merupakan alfabet

print("‫"موز‬.isalpha())
# output ➜ True, karena ‫ موز‬adalah abjad arabic

print("⯑⯑⯑".isalpha())
# output ➜ True, karena ⯑⯑⯑ adalah karakter jepang

print("123456".isdigit())
# output ➜ True, karena 123456 adalah digit

print("123abc".isdigit())
# output ➜ False, karena ada karakter abc yang bukan merupakan digit

print('2⅓'.isdigit())
# output ➜ False, karena bilangan pecahan memiliki karakter `/` yang tidak termasuk dalam kategori digit

print('4²'.isdigit())
# output ➜ True, karena 4² adalah bilangan pangkat

print('٢٨'.isdigit())
# output ➜ True, karena ٢٨ adalah digit arabic

print('𝟜'.isdigit())
# output ➜ True, karena 𝟜 adalah digit

print("123456".isdecimal())
# output ➜ True, karena 123456 adalah angka desimal

print("123abc".isdecimal())
# output ➜ False, karena ada karakter abc yang bukan merupakan angka desimal

print('2⅓'.isdecimal())
# output ➜ False, karena bilangan pecahan memiliki karakter `/` yang tidak termasuk dalam kategori angka desimal

print('4²'.isdecimal())
# output ➜ False, karena bilangan pangkat yang tidak termasuk dalam kategori angka desimal

print('٢٨'.isdecimal())
# output ➜ True, karena ٢٨ adalah angka desimal arabic

print('𝟜'.isdecimal())
# output ➜ True, karena 𝟜 adalah angka desimal

print("123456".isnumeric())
# output ➜ True, karena 123456 adalah angka numerik

print("123abc".isnumeric())
# output ➜ False, karena ada karakter abc yang bukan merupakan numerik

print("123abc".isalnum())
# output ➜ True, karena 123 adalah digit dan abc adalah alfabet

print("12345⅓".isalnum())
# output ➜ True, karena 12345⅓ adalah digit

print("abcdef".isalnum())
# output ➜ True, karena abcdef adalah alfabet

print("abc 12".isalnum())
# output ➜ False, karena ada karakter spasi yang bukan merupakan karakter digit ataupun alfabet

print("‫"موز‬.isalnum())
# output ➜ True, karena ‫ موز‬adalah abjad arabic

print("⯑⯑⯑".isalnum())
# output ➜ True, karena ⯑⯑⯑ adalah karakter jepang

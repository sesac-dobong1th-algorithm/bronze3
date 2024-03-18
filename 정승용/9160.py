# Dissatisfied with the loud and constant pronouncements of his alleged misdeeds
# by a trio of indefatigable minstrels,
# the brave knight Sir Robin wishes to exercise his authority by modifying their lyrics.
# The minstrels were happy to provide printed transcripts of their songs,
# and cheerfully announced that they would not change a word of them.

# Undaunted, the brave (and crafty) Sir Robin scrutinized the documents and
# noticed that their loudest inflections were indicated by capital letters and
# realized that he could at least lower their voices. This, he reasoned,
# could be accomplished by replacing upper case letters with lower case letters
# (“Case correction”, from his perspective).
# These modifications could be forced upon the singers by
# insistence upon proper usage of the King’s English.
# Not all letters can be lower case, however,
# as the King’s English mandates some letters must be upper case.

# Strangely hesitant about performing “case correction” personally,
# the brave, crafty (and managerially capable) Sir Robin humbly requests you
# write a program to perform a first pass of case correction for the songs.
# There will still be some corrections required after this program is used.

# As your program reads the file, it must force to upper case all alphabetic characters
# that follow terminal punctuation marks (period, question mark, and exclamation point)
# with only white space or parentheses characters following.
# All other alphabetic characters are to be forced to lower case.
# Note that decimal numbers are not to be followed by an upper case character unless the number
# itself is followed by a terminal punctuation mark.

# 입력
# The input file contains the text that you are converting.
# Your conversions should be based on the rules given by Brave Sir Robin above.

# 출력
# The output is to be the converted text. All characters are transferred to the output.
# Some will have cAsE cOrReCtiOn, others will be directly copied.

import re
import sys

new = ""

a = sys.stdin.readlines()  # 여러 문자열 라인 받기 위함
# print(a)
flag_cap = False  # 케이스 분리
for i in range(len(a)):
    a[i] = a[i].lower()  # 일단 싹 소문자로
    # print(a[i][:])

    if flag_cap == True:  # flag_cap이 True일 때
        a[i] = a[i].capitalize()  # 첫문자 대문자로
        # print(a[i])
        new += re.sub(  # 아래 조건에 포함된 단어 대문자로
            r"([.!?()]\s*(\w)|[.!?()](\w))",
            lambda n: n.group().upper(),
            a[i],
        )
        flag_cap = False  # flag_cap False로 초기화
    else:  # flag_cap False일 때
        new += re.sub(
            r"([.!?()]\s*(\w)|[.!?()](\w))",
            lambda n: n.group().upper(),
            a[i],
        )
        if re.search(r"[.!?()](\n)", a[i]):  # .!?()다음 \n가 바로 올때
            flag_cap = True  # flag_cap을 True로
        else:
            flag_cap = False


new = new.replace("\n", " ")
print(new)

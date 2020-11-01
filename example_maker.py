from pathlib import Path
from random import choice

STR_BANK = 'QWERTASDFGZXCVBUIOPJKLM1234567890'
TEMPLATE1 = 'sony_{}.jpg'
TEMPLATE2 = 'cannon_{}_12November2010.jpg'


# First example is taming files from pictures that may have a default naming convention
target1 = Path('testdir/jpg_example')
for index in range(0, 20):
    name_id = ''.join(choice(STR_BANK)for i in range(13))
    file_name = TEMPLATE1.format(name_id)
    (target1 / file_name).touch()

for index in range(0, 20):
    name_id = ''.join(choice(STR_BANK) for i in range(5))
    file_name = TEMPLATE2.format(name_id)
    (target1 / file_name).touch()



from pathlib import Path
from random import choice

STR_BANK = 'QWERTASDFGZXCVBUIOPJKLM1234567890'
TEMPLATE1 = 'sony_{}.jpg'


# First example is taming files from pictures that may have a default naming convention
target1 = Path('testdir/jpg_example')
for index in range(0, 100):
    name_id = ''.join(choice(STR_BANK)for i in range(13))
    file_name = TEMPLATE1.format(name_id)
    (target1 / file_name).touch()



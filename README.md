# Bulker
Bulk file rename

# Scenarios
### Scenario 1
You have a bunch of picture file names with a prefix of the same word such a sony and you 
want to get rid of the word sony on each file
```bash
 python bulker.py testdir --split sony_ --index 1
```
```
--append= | --prefix | --index=0 | --stitch=split | --exclude= | --include=
To execute your changes, add --execute=True

                    [Files included in the changes](4/4)
sony_0AFQVDWZLD97G.jpg > 0AFQVDWZLD97G.jpg
sony_1DC72FP20QL2U.jpg > 1DC72FP20QL2U.jpg
sony_1L79UPJ4OXWOO.jpg > 1L79UPJ4OXWOO.jpg
sony_2G1IVBM4WVAXL.jpg > 2G1IVBM4WVAXL.jpg
```

### Scenario 2
You want to remove the word sony and replace it with another string like a date
```bash
python bulker.py testdir --split sony_ --index 1 --prefix 20201031_
```
```
sony_0AFQVDWZLD97G.jpg > 20201031_0AFQVDWZLD97G.jpg
sony_1DC72FP20QL2U.jpg > 20201031_1DC72FP20QL2U.jpg
sony_1L79UPJ4OXWOO.jpg > 20201031_1L79UPJ4OXWOO.jpg
sony_2G1IVBM4WVAXL.jpg > 20201031_2G1IVBM4WVAXL.jpg
```
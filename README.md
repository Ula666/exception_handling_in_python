## Exception handling in Python
### `try`, `except`, `raise`, and `finally` as code blocks to handle the error or an exceptions

### To understand the concept easily:
- Each block of code works as an if, elif, else block


```python
# Dealing with files and error/exception handling
# There is a built in method in Python called open("") it takes a string
# file = open("orders.text") # looks for the file called orders.txt

try:
    file = open("orders.text")
    print("File was found")
except FileNotFoundError as errmsg:
    print(f"the above block of code wasn't executed {errmsg}")
    # raise
finally:
    print("Your task is to read the data and display as a list")
```

- Please ensure to create an orders.text if does not exists

```
| Mode |Description|
| :----: |:---- |
|'r' |This is the default mode. It Opens file for reading. |
|'w' |This Mode Opens file for writing. If file does not exist, it creates a new file. If file exists it truncates the file.|
|'x' |Creates a new file. If file already exists, the operation fails.|
|'a' |Open file in append mode. If file does not exist, it creates a new file.|
|'t' |This is the default mode. It opens in text mode.|
|'b' |This opens in binary mode.
|'+' |This will open a file for reading and writing (updating)|


It is worth noting that the `+` operator can be used with
```

# Python for Data Analysis

**Python for Data Analysis: Data Wrangling with Pandas, numPy and Jupyter** by Wes McKinney
[book](https://wesmckinney.com/book/)

- Python is an interpreted language
- The Python interpreter runs a program by executing one statement at a time.

```py
print("Hello world")
```

- execute above code by running

```sh
python filename.py
```

### Language Sematics

- The Python language design is distinguished by its emphasis on readability, simplicity, and explicitness.

#### Indentation, not braces

- Python uses whitespace (tabs or spaces) to structure code

Consider a `for loop` from a sorting algorithm:

```py
for x in array:
  if x < pivot:
    less.append(x)
  else:
    greater.append(x)
```

<em> A colon denotes the start of an indented code block after which all of the code must be indented by the same amount until the end of the block. </em>

from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *
from node_functions import *
from block_functions import *

def main():

    md = """
# Heading

## Heading

### Heading

#### Heading

##### Heading

###### Heading

## Two-line
Header

####### Heading

###

```print("Hello, world!")```

```
print("hello, world!")
##comment
i = 1
```

`````` 

>I am legend!
>I am inevitable!

>When the day calls,
I know what you do

I know what you did last summer
>You know what is another

>Thi is serious!
I know what you did last summer
>You know what is another

- eggs
- milk
- water

eggs
- milk
- water

- eggs
- milk
water

-eggs
- milk
- water

1. wash bathroom
2. wash kitchen
3. wash living room
4. wash bedroom

This is where we start the paragraph
"""

    headings = """
# Heading

## Heading

### Heading

#### Heading

##### Heading

###### Heading

## Two-line
Header

# Dirty#Heading

####### Heading

###"""

    codes = """
```print("Hello, world!")```

```
print("hello, world!")
##comment
i = 1
```

print("hello")
```

```
print("hello")

```print("hello")
```string```
```

``````"""

    quotes = """
>I am legend!
>I am inevitable!

>When the day calls,
I know what you do

I know what you did last summer
>You know what is another

>Thi is serious!
I know what you did last summer
>You know what is another"""

    ulist = """
- eggs
- milk
- water

eggs
- milk
- water

- eggs
- milk
water

-eggs
- milk
- water"""

    olist = """"""

    blocks = BlockFunc.markdown_to_blocks(quotes)
    
    #print(blocks)

    for block in blocks:
        print(block + "\n")

    print("")

    for block in blocks:
        print(f"This block is {BlockFunc.block_to_block_type(block)}")

main()
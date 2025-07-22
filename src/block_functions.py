import re

from block import *
from textnode import *

class BlockFunc():

    def markdown_to_blocks(markdown):

        prelim_block_split = markdown.split("\n\n")

        for i in range(0, len(prelim_block_split)):
            prelim_block_split[i] = prelim_block_split[i].strip()

        block_split = []

        for block in prelim_block_split:
            if block != "" and block != "\n":
                block_split.append(block)

        return block_split

    def block_to_block_type(block):
        
        if re.match(r"^#{1,6}\s[^#]+$", block, re.DOTALL):
            return BlockType.HEAD
        elif re.match(r"^```.+```$", block, re.DOTALL):
            return BlockType.CODE
        elif re.match(r"^(?:>).*$(?:\n(?:>).*$)*", block, re.MULTILINE):
            return BlockType.QUOTE
        elif re.match(r"(- .*){1,}", block, re.DOTALL):
            ulist_split = block.split("\n")
            '''for ulist in ulist_split:
                if ulist[0:2] != "- ":
                    return BlockType.PARA'''
            return BlockType.ULIST
        elif re.match(r"1. .*", block):
            curr_num = 0
            olist_split = block.split("\n")
            '''for olist in olist_split:
                if olist[0] == curr_num + 1:
                    curr_num = int(olist[0])
                else:
                    return BlockType.PARA'''
            return BlockType.OLIST
        return BlockType.PARA
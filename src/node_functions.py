import re

from textnode import *

class NodeFunc():

    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []
        for node in old_nodes:
            if node.text_type == TextType.TEXT and delimiter in node.text:
                node_split = node.text.split(delimiter)
                for i in range(0, len(node_split)):
                    if node_split[i] == "":
                        pass
                    elif i % 2 != 0:
                        new_nodes.append(TextNode(node_split[i],text_type))
                    else:
                        new_nodes.append(TextNode(node_split[i], TextType.TEXT))
            else:
                new_nodes.append(node)
        return new_nodes

    def extract_markdown_images(text):
        alt_texts = re.findall(r"!\[([\w ]*)\]\(([^\(\)]*)\)", text)
        return alt_texts
    
    def extract_markdown_links(text):
        alt_texts = re.findall(r"(?<!!)\[([\w ]*)\]\(([^\(\)]*)\)", text)
        return alt_texts
    
    def split_nodes_image(old_nodes):
        new_nodes = []
        for node in old_nodes:
            if node.text_type != TextType.TEXT:
                new_nodes.append(node)
            else:
                begin_pivot = 0
                for i in range(begin_pivot, len(node.text)):
                    if node.text[i] == "!" or node.text[i] == "\n":
                        new_nodes.append(TextNode(node.text[begin_pivot:i], TextType.TEXT))
                        begin_pivot = i
                    elif node.text[i] == ")" and node.text[begin_pivot] == "!":
                        alt, url = NodeFunc.extract_markdown_images(node.text[begin_pivot:i + 1]).pop()
                        new_nodes.append(TextNode(alt, TextType.IMAGE, url))
                        begin_pivot = i + 1
        return new_nodes

    def split_nodes_link(old_nodes):
        new_nodes = []
        for node in old_nodes:
            if node.text_type != TextType.TEXT:
                new_nodes.append(node)
            else:
                begin_pivot = 0
                for i in range(begin_pivot, len(node.text)):
                    if node.text[i] == "[" or node.text[i] == "\n":
                        new_nodes.append(TextNode(node.text[begin_pivot:i], TextType.TEXT))
                        begin_pivot = i
                    elif node.text[i] == ")" and node.text[begin_pivot] == "[":
                        alt, url = NodeFunc.extract_markdown_links(node.text[begin_pivot:i + 1]).pop()
                        new_nodes.append(TextNode(alt, TextType.LINK, url))
                        begin_pivot = i + 1
        return new_nodes
    
    def text_to_textnodes(text):
        node = TextNode(text, TextType.TEXT)
        nodes = [node]
        nodes = NodeFunc.split_nodes_delimiter(nodes, "**", TextType.BOLD)
        nodes = NodeFunc.split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        nodes = NodeFunc.split_nodes_delimiter(nodes, "`", TextType.CODE)
        nodes = NodeFunc.split_nodes_image(nodes)
        nodes = NodeFunc.split_nodes_link(nodes)
        return nodes
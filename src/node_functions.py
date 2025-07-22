import re

from textnode import *

class NodeFunc():

    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []
        for node in old_nodes:
            if node.text_type == TextType.TEXT and delimiter in node.text:
                node_split = node.text.split(delimiter)
                first_split = 0
                if node_split[0] == "":
                    first_split += 1
                last_split = len(node_split)
                if node_split[-1] == "":
                    last_split -= 1
                if len(node_split) % 2 == 0:
                    raise Exception(f"Missing terminating delimiter {delimiter}")
                for i in range(first_split, last_split):
                    if i % 2 != 0:
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
                images = NodeFunc.extract_markdown_images(node.text)
                if len(images) == 0:
                    new_nodes.append(node)
                else:
                    text_partition = node.text
                    for image in images:
                        split_text = text_partition.split(f"![{image[0]}]({image[1]})", 1)
                        if len(split_text) == 1:
                            new_text_node = TextNode(split_text[0], TextType.TEXT)
                        else:
                            prefix_text = split_text[0]
                            text_partition = split_text[1]
                            if prefix_text != "":
                                new_text_node = TextNode(prefix_text, TextType.TEXT)
                                new_nodes.append(new_text_node)
                            new_image_node = TextNode(image[0],TextType.IMAGE,image[1])
                            new_nodes.append(new_image_node)
                    if text_partition != "":
                        tail_node = TextNode(text_partition, TextType.TEXT)
                        new_nodes.append(tail_node)
        return new_nodes

    def split_nodes_link(old_nodes):
        new_nodes = []
        for node in old_nodes:
            if node.text_type != TextType.TEXT:
                 new_nodes.append(node)
            else:
                links = NodeFunc.extract_markdown_links(node.text)
                if len(links) == 0:
                    new_nodes.append(node)
                else:
                    text_partition = node.text
                    for link in links:
                        split_text = text_partition.split(f"[{link[0]}]({link[1]})", 1)
                        if len(split_text) == 1:
                            new_text_node = TextNode(split_text[0], TextType.TEXT)
                        else:
                            prefix_text = split_text[0]
                            text_partition = split_text[1]
                            if prefix_text != "":
                                new_text_node = TextNode(prefix_text, TextType.TEXT)
                                new_nodes.append(new_text_node)
                            new_link_node = TextNode(link[0],TextType.LINK,link[1])
                            new_nodes.append(new_link_node)
                    if text_partition != "":
                        tail_node = TextNode(text_partition, TextType.TEXT)
                        new_nodes.append(tail_node)
        return new_nodes
    
    def text_to_textnodes(text):
        if text == "":
            return []
        node = TextNode(text, TextType.TEXT)
        nodes = [node]
        nodes = NodeFunc.split_nodes_delimiter(nodes, "**", TextType.BOLD)
        nodes = NodeFunc.split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        nodes = NodeFunc.split_nodes_delimiter(nodes, "`", TextType.CODE)
        nodes = NodeFunc.split_nodes_image(nodes)
        nodes = NodeFunc.split_nodes_link(nodes)
        return nodes
import unittest

from textnode import *
from htmlnode import HTMLNode
from node_functions import NodeFunc


class TestNodeFunctions(unittest.TestCase):
        
    def test_base_bold_case(self):
        node_base_bold_case = TextNode(
            "This is text with a **bolded phrase** in the middle", 
            TextType.TEXT
        )
        print(node_base_bold_case)
        node_base_bold_case_delimited = NodeFunc.split_nodes_delimiter(
            [node_base_bold_case], "**", TextType.BOLD
        )
        print(node_base_bold_case_delimited)
        print("")
        self.assertTrue(node_base_bold_case_delimited[1].text_type == TextType.BOLD)

    def test_node_base_italic_case(self):
        node_base_italic_case = TextNode(
            "This is text with a _italic phrase_ in the middle", 
            TextType.TEXT
        )
        print(node_base_italic_case)
        node_base_italic_case_delimited = NodeFunc.split_nodes_delimiter(
            [node_base_italic_case], "_", TextType.ITALIC
        )
        print(node_base_italic_case_delimited)
        print("")
        self.assertTrue(node_base_italic_case_delimited[1].text_type == TextType.ITALIC)

    def test_node_base_code_case(self):
        node_base_code_case = TextNode(
            "This is text with a `code phrase` in the middle", 
            TextType.TEXT
        )
        print(node_base_code_case)
        node_base_code_case_delimited = NodeFunc.split_nodes_delimiter(
            [node_base_code_case], "`", TextType.CODE
        )
        print(node_base_code_case_delimited)
        print("")
        self.assertTrue(node_base_code_case_delimited[1].text_type == TextType.CODE)

    def test_node_comingled_case1(self):
        node_comingled_case1 = TextNode(
        "This text has **comingled** _text_!",
            TextType.TEXT
        )
        print(node_comingled_case1)
        node_comingled_case1_delimited = NodeFunc.split_nodes_delimiter(
            [node_comingled_case1], "**", TextType.BOLD
        )
        print(node_comingled_case1_delimited)
        print("")
        self.assertTrue(node_comingled_case1_delimited[1].text_type == TextType.BOLD)

    def test_node_italic_delimited_first(self):
        node_italic_delimited_first = TextNode(
        "This text has _comingled_ **text**!",
            TextType.TEXT
        )
        print(node_italic_delimited_first)
        node_italic_delimited_first_delimited = NodeFunc.split_nodes_delimiter(
            [node_italic_delimited_first], "_", TextType.ITALIC
        )
        print(node_italic_delimited_first_delimited)
        print("")
        self.assertTrue(node_italic_delimited_first_delimited[1].text_type == TextType.ITALIC)

    def test_node_no_terminating_bold_delimiter(self):
        node_no_terminating_bold_delimiter= TextNode(
            "This text has a missing **bold delimiter terminator",
            TextType.TEXT
        )
        print(node_no_terminating_bold_delimiter)
        with self.assertRaises(Exception):
            node_no_terminating_bold_delimiter_delimited = NodeFunc.split_nodes_delimiter(
                [node_no_terminating_bold_delimiter], "**", TextType.TEXT
            )
        print("")
    
    def test_node_no_terminating_italic_delimiter(self):
        node_no_terminating_italic_delimiter = TextNode(
            "This text has a missing _italic delimiter terminator",
            TextType.TEXT
        )
        print(node_no_terminating_italic_delimiter)
        with self.assertRaises(Exception):
            node_no_terminating_italic_delimiter_delimited = NodeFunc.split_nodes_delimiter(
                [node_no_terminating_italic_delimiter], "_", TextType.ITALIC
            )
        print("")

    def test_node_no_terminating_code_delimiter(self):    
        node_no_terminating_code_delimiter = TextNode(
            "This text has a missing `delimiter terminator",
            TextType.TEXT
        )
        print(node_no_terminating_code_delimiter)
        with self.assertRaises(Exception):
             node_no_terminating_code_delimiter_delimited = NodeFunc.split_nodes_delimiter(
                [node_no_terminating_code_delimiter], "`", TextType.CODE
            )
        print("")
    
    def test_node_starting_delimiter(self):
        node_starting_delimiter = TextNode(
            "_This_ text starts with a delimiter",
            TextType.TEXT
        )
        print(node_starting_delimiter)
        node_starting_delimiter_delimited = NodeFunc.split_nodes_delimiter(
            [node_starting_delimiter], "_", TextType.ITALIC
        )
        self.assertTrue(node_starting_delimiter_delimited[0].text_type == TextType.ITALIC)
        print(node_starting_delimiter_delimited)
        print("")
    
    def test_node_ending_delimiter(self):
        node_ending_delimiter = TextNode(
                "This text ends with _delimiter_",
                TextType.TEXT
            )
        print(node_ending_delimiter)
        node_ending_delimiter_delimited = NodeFunc.split_nodes_delimiter(
            [node_ending_delimiter], "_", TextType.ITALIC
        )
        self.assertTrue(node_ending_delimiter_delimited[-1].text_type == TextType.ITALIC)
        print(node_ending_delimiter_delimited)
        print("")

    def test_extract_image_text(self):
        extract_image_text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_images = NodeFunc.extract_markdown_images(extract_image_text)
        self.assertEqual(extracted_images[0], ('rick roll', 'https://i.imgur.com/aKaOqIh.gif'))
        print(extracted_images)
        print("")

    def test_extract_link_text(self):
        extract_link_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted_links = NodeFunc.extract_markdown_links(extract_link_text)
        self.assertEqual(extracted_links[0], ('to boot dev', 'https://www.boot.dev'))
        print(extracted_links)
        print("")

    def test_comingled_extract_image_text(self):
        comingled_extract_image_text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_images = NodeFunc.extract_markdown_images(comingled_extract_image_text)
        self.assertEqual(len(extracted_images), 1)
        self.assertEqual(extracted_images[0], ('rick roll', 'https://i.imgur.com/aKaOqIh.gif'))
        print(extracted_images)
        print("")

    def test_comingled_extract_link_text(self):
        comingled_extract_link_text = "This is text with a link ![to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted_links = NodeFunc.extract_markdown_links(comingled_extract_link_text)
        self.assertEqual(len(extracted_links), 1)
        self.assertEqual(extracted_links[0], ('to youtube', 'https://www.youtube.com/@bootdotdev'))
        print(extracted_links)
        print("")

    def test_extract_image_text_from_start(self):
        extract_image_text_from_start = "![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_images = NodeFunc.extract_markdown_images(extract_image_text_from_start)
        self.assertEqual(extracted_images[0], ('rick roll', 'https://i.imgur.com/aKaOqIh.gif'))
        print(extracted_images)
        print("")

    def test_extract_link_text_from_start(self):
        extract_link_text_from_start = "[to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted_links = NodeFunc.extract_markdown_links(extract_link_text_from_start)
        self.assertEqual(extracted_links[0], ('to boot dev', 'https://www.boot.dev'))
        print(extracted_links)
        print("")

    def test_extract_image_text_from_end(self):
        extract_image_text_from_end = "This and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_images = NodeFunc.extract_markdown_images(extract_image_text_from_end)
        self.assertEqual(extracted_images[-1], ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg'))
        print(extracted_images)
        print("")

    def test_extract_link_text_from_end(self):
        extract_link_text_from_end = "This and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted_links = NodeFunc.extract_markdown_links(extract_link_text_from_end)
        self.assertEqual(extracted_links[-1], ('to youtube', 'https://www.youtube.com/@bootdotdev'))
        print(extracted_links)
        print("")

    def test_split_with_image_text(self):
        split_with_image_text = "This is text with an image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev) thank you!"
        node1 = TextNode(
            split_with_image_text,
            TextType.TEXT
        )
        new_nodes1 = NodeFunc.split_nodes_image([node1])
        self.assertEqual(new_nodes1[1], TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"))
        print(new_nodes1)
        print("")

    def test_split_with_link_text(self):
        split_with_link_text= "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) thank you!"
        node2 = TextNode(
            split_with_link_text,
            TextType.TEXT
        )
        new_nodes2 = NodeFunc.split_nodes_link([node2])
        self.assertEqual(new_nodes2[1], TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"))
        print(new_nodes2)
        print("")

    def test_split_with_link_and_image_text1(self):
        split_with_link_and_image_text1 = "This is text with a link ![This is text with a link ](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) thank you!"
        node3 = TextNode(
            split_with_link_and_image_text1,
            TextType.TEXT
        )
        new_nodes3 = NodeFunc.split_nodes_image([node3])
        self.assertEqual(new_nodes3[1], TextNode("This is text with a link ", TextType.IMAGE, "https://www.boot.dev"))
        self.assertEqual(new_nodes3[2], TextNode(" and [to youtube](https://www.youtube.com/@bootdotdev) thank you!", TextType.TEXT, None))
        print(new_nodes3)
        print("")

    def test_split_with_link_and_image_text2(self):
        split_with_link_and_image_text2 = "This is text with a link ![to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) thank you!"
        node4 = TextNode(
            split_with_link_and_image_text2,
            TextType.TEXT
        )
        new_nodes4 = NodeFunc.split_nodes_link([node4])
        self.assertEqual(new_nodes4[0], TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ", TextType.TEXT, None))
        self.assertEqual(new_nodes4[1], TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"))
        print(new_nodes4)
        print("")
    
    def test_text_to_textnodes_all_node_types(self):
        text_to_nodes_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"    
        text_to_textnodes = NodeFunc.text_to_textnodes(text_to_nodes_text)
        self.assertEqual(len(text_to_textnodes), 10)
        self.assertEqual(text_to_textnodes[0].text_type, TextType.TEXT)
        self.assertEqual(text_to_textnodes[9].text_type, TextType.LINK)
        print(text_to_textnodes)
        print("")

    def test_text_to_textnodes_empty_arg(self):
        text_to_nodes_text = ""    
        text_to_textnodes = NodeFunc.text_to_textnodes(text_to_nodes_text)
        self.assertEqual(len(text_to_textnodes), 0)
        print(text_to_textnodes)
        print("")
    
    def test_text_to_textnodes_multiple_non_link_types(self):
        text_to_nodes_text = "This is **text** with an _italic_ word"    
        text_to_textnodes = NodeFunc.text_to_textnodes(text_to_nodes_text)
        self.assertEqual(text_to_textnodes[1].text_type, TextType.BOLD)
        self.assertEqual(text_to_textnodes[3].text_type, TextType.ITALIC)
        self.assertEqual(text_to_textnodes[4].text_type, TextType.TEXT)
        print(text_to_textnodes)
        print("")

    def test_text_to_textnodes_one_non_link_type(self):
        text_to_nodes_text = "This is **text**"    
        text_to_textnodes = NodeFunc.text_to_textnodes(text_to_nodes_text)
        self.assertEqual(len(text_to_textnodes), 2)
        self.assertEqual(text_to_textnodes[1].text_type, TextType.BOLD)
        print(text_to_textnodes)
        print("")

    def test_text_to_textnodes_just_non_link_type(self):
        text_to_nodes_text = "**text**"    
        text_to_textnodes = NodeFunc.text_to_textnodes(text_to_nodes_text)
        self.assertEqual(len(text_to_textnodes), 1)
        self.assertEqual(text_to_textnodes[0].text_type, TextType.BOLD)
        print(text_to_textnodes)
        print("")

    def test_text_to_textnodes_link_types(self):
        text_to_nodes_text = "A ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"    
        text_to_textnodes = NodeFunc.text_to_textnodes(text_to_nodes_text)
        self.assertEqual(text_to_textnodes[1].text_type, TextType.IMAGE)
        self.assertEqual(text_to_textnodes[0].text_type, TextType.TEXT)
        self.assertEqual(text_to_textnodes[3].text_type, TextType.LINK)
        print(text_to_textnodes)
        print("")

    def test_text_to_textnodes_link_type(self):
        text_to_nodes_text = "A [link](https://boot.dev)"    
        text_to_textnodes = NodeFunc.text_to_textnodes(text_to_nodes_text)
        self.assertEqual(len(text_to_textnodes), 2)
        self.assertEqual(text_to_textnodes[1].text_type, TextType.LINK)
        print(text_to_textnodes)
        print("")

    def test_text_to_textnodes_just_link(self):
        text_to_nodes_text = "[link](https://boot.dev)"    
        text_to_textnodes = NodeFunc.text_to_textnodes(text_to_nodes_text)
        self.assertEqual(len(text_to_textnodes), 1)
        self.assertEqual(text_to_textnodes[0].text_type, TextType.LINK)
        print(text_to_textnodes)
        print("")

    def test_text_to_textnodes_just_text(self):
        text_to_nodes_text = "This is"    
        text_to_textnodes = NodeFunc.text_to_textnodes(text_to_nodes_text)
        self.assertEqual(len(text_to_textnodes), 1)
        self.assertEqual(text_to_textnodes[0].text_type, TextType.TEXT)
        print(text_to_textnodes)
        print("")

if __name__ == "__main__":
    unittest.main()
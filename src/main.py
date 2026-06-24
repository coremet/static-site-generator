from textnode import TextNode, TextType

def main():
    def create_dummy_node():
        return TextNode(
            text="This is some anchor text",
            text_type=TextType.LINK,
            url="https://www.boot.dev"
        )

    dummy_node = create_dummy_node()
    print(dummy_node)

if __name__ == "__main__":
    main()
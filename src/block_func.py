

def markdown_to_blocks(markdown):
    blocks_list = markdown.split("\n\n")
    blocks = []
    for block in blocks_list:
        blocks.append(block.strip())
    blocks = [block for block in blocks if block != ""]
    return blocks
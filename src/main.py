import sys
from copy_static import copy_static
from generate_page import generate_pages_recursive

if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"

def main():
    copy_static("static", "docs")
    generate_pages_recursive(basepath, "content", "template.html", "docs")
    
if __name__ == "__main__":
    main()
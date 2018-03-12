"""
This script requires Python 3.6+.
"""

from pathlib import Path


SUPPORTERS_PATH = '_data/sf-individuals.txt'

def main():
    path = Path(SUPPORTERS_PATH)
    text = path.read_text()
    lines = text.splitlines()
    print(f'read {len(lines)} supporters')

    lines = sorted(lines)
    # Format for Markdown.
    lines = [f'1. {line}' for line in lines]
    markdown = '\n'.join(lines)

    temp_path = Path('temp.md')
    print(f'writing to: {temp_path}')
    temp_path.write_text(markdown)


if __name__ == '__main__':
    main()

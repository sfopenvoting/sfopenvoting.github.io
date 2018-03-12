"""
This script requires Python 3.6+.
"""

import json
from pathlib import Path


SUPPORTERS_JSON_PATH = '_data/supporters.json'
SUPPORTERS_PATH = '_prep/sf-individuals.txt'

def main():
    path = Path(SUPPORTERS_PATH)
    text = path.read_text()
    lines = text.splitlines()
    print(f'read {len(lines)} supporters')

    data = {'residents': lines}
    lines = sorted(lines)
    # Format for Markdown.
    lines = [f'1. {line}' for line in lines]
    markdown = '\n'.join(lines)

    temp_path = Path('temp.md')
    print(f'writing to: {temp_path}')
    temp_path.write_text(markdown)

    with open(SUPPORTERS_JSON_PATH, mode='w') as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    main()

import sys

def gen_html_row(bal_path, bir_path):
    file_name = bal_path.split('/')[-1]
    heading = f'<tr><td colspan="2" class="filename">{file_name}</td></tr>'
    bal = f"<td>{code_to_html(bal_path, 'language-ts hljs language-typescript')}</td>"
    bir = f"<td>{code_to_html(bir_path, 'language-scheme hljs')}</td>"
    body = f"<tr>{bal}{bir}</tr>"
    return heading + body

def code_to_html(file_path, css_class=""):
    with open(file_path, 'r') as f:
        code = f.read()
    return f'<pre><code class="{css_class}">{code}</code></pre>'

def gen_body(bal_path, bir_path):
    table = f"<table>{gen_html_row(bal_path, bir_path)}</table>"
    return f"<html><body>{table}</body></html>"

if __name__ == "__main__":
    bal_path, bir_path = sys.argv[1], sys.argv[2]
    with open('comp.html', 'w') as f:
        f.write(gen_body(bal_path, bir_path))

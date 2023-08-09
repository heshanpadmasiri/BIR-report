import os
import sys
from compGen import gen_html_row

def write_report(body):
    with open('report.html', 'w') as f:
        f.write(body)

def generate_report_for_dir(path):
    rows = []
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path) and filename.endswith("-v.bal"):
            bal_path = file_path 
            bir_path = file_path[:-4] + ".bir"
            rows.append(gen_html_row(bal_path, bir_path))
    return f'<html>{html_head()}<body data-new-gr-c-s-check-loaded="8.906.0" data-gr-ext-installed=""><table>{"".join(rows)}</table></body></html>'

def html_head():
    return '''<head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>nbir s-expr</title>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.1/styles/default.min.css">
            <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.1/highlight.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.1/languages/scheme.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/highlightjs-line-numbers.js/2.8.0/highlightjs-line-numbers.min.js"></script><style type="text/css">.hljs-ln{border-collapse:collapse}.hljs-ln td{padding:0}.hljs-ln-n:before{content:attr(data-line-number)}</style>
            <style>
                body {
                    background: #f3f3f3;
                    color: #444;
                    font-family: Open Sans,Arial;
                }
                table {
                    table-layout:fixed;
                }
                th {
                    font-size: 22px;
                }
                td {
                    overflow: hidden;
                    text-overflow: ellipsis;
                    word-wrap: break-word;
                }
                .filename {
                    background: #ddd;
                    text-align: center;
                    font-size: 20px;
                }
                .hljs-ln-numbers {
                    color: #ccc;
                }
            </style>
        <script type="text/javascript">(async function() { class ReadwiseElement extends HTMLElement {
          constructor() {
            super();
            [...this.children].forEach((child) => this.appendChild(child));
          }
        }
        try {
          customElements.define(
            "readwise-tooltip-container",
            class ReadwiseTooltipContainer extends ReadwiseElement {},
            {"extends":"div"},
          );
        } catch (e) {
          if(!e.message.includes("already been defined")
            && !e.message.includes("already been used with this registry")) {
            console.error("Failed to define custom element", e);
            throw e;
          }
        } })()</script><script type="text/javascript">document.body.appendChild(document.createElement("readwise-tooltip-container"));</script><script type="text/javascript">(async function() { class ReadwiseElement extends HTMLElement {
          constructor() {
            super();

            [...this.children].forEach((child) => this.appendChild(child));
          }
        }
        try {
          customElements.define(
            "rw-highlight",
            class ReadwiseHighlight extends ReadwiseElement {},
            {"extends":"mark"},
          );
        } catch (e) {
          if(!e.message.includes("already been defined")
            && !e.message.includes("already been used with this registry")) {
            console.error("Failed to define custom element", e);
            throw e;
          }
        } })()</script></head>'''

if __name__ == "__main__":
    test_dir = sys.argv[1]
    write_report(generate_report_for_dir(test_dir))


import markdown
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OpPath = os.path.join(project_root,'markdowns', 'PriceOp', '.html')



def priceOp(ai_data, code):
    html_content = markdown.markdown(ai_data)

    full_html_page = f"""<!DOCTYPE html>
    <html lang="fa" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Price opinion</title>
        <style>
            /* --- Import Google Font for Persian --- */
            @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;600;700&display=swap');

            /* --- General Styles --- */
            body {{
                font-family: 'Vazirmatn', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                line-height: 1.8;
                background-color: #f8f9fa; /* Light gray background */
                color: #212529; /* Dark text for high contrast */
                margin: 0;
                padding: 20px;
                display: flex;
                justify-content: center;
            }}

            /* --- Main Content Container --- */
            .container {{
                max-width: 800px;
                width: 100%;
                background-color: #ffffff; /* White paper background */
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
                padding: 30px 40px;
                border: 1px solid #e9ecef;
            }}

            /* --- Typography --- */
            h1 {{
                font-size: 2em;
                font-weight: 700;
                color: #343a40;
                text-align: center;
                margin-bottom: 25px;
                padding-bottom: 15px;
                border-bottom: 2px solid #dee2e6;
            }}

            h2 {{
                font-size: 1.5em;
                font-weight: 600;
                color: #495057;
                margin-top: 35px;
                margin-bottom: 15px;
                border-right: 4px solid #007bff; /* Blue accent line */
                padding-right: 12px;
            }}

            h3 {{ 
                font-size: 1.2em;
                font-weight: 600;
                color: #495057;
                margin-top: 25px;
                margin-bottom: 10px;
                border-right: 2px solid #007bff; 
                padding-right: 8px;
            }}

            p {{
                margin-bottom: 15px;
            }}

            /* --- List Styles --- */
            ul {{
                list-style-type: '✔  '; /* Custom bullet point */
                padding-right: 20px;
            }}

            li {{
                margin-bottom: 10px;
            }}
            
            ul ul {{
                list-style-type: '–  '; /* Nested list bullet point */
                margin-top: 10px;
            }}

            /* --- Keyword Highlighting --- */
            strong {{
                color: #0056b3; /* Slightly darker blue for emphasis */
                font-weight: 600;
            }}

            /* --- Final Notes/Recommendations --- */
            .note {{ 
                background-color: #e9ecef;
                border-right: 4px solid #6c757d;
                padding: 15px;
                border-radius: 8px;
                font-size: 0.95em;
                margin-top: 20px;
            }}

        </style>
    </head>
    <body>
        <div class="container">
            {html_content}
        </div>
    </body>
    </html>
    """

    output_filename = f"PriceOp({code}).html"
    with open(os.path.join(OpPath, output_filename), "w", encoding="utf-8") as f:
        f.write(full_html_page)

    print(f"{output_filename} saved successfully!")


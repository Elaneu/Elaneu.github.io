import subprocess
import os

# Define the path to the repository directory
repo_dir = r"C:\Users\User\Desktop\Web_Page\Scripts\Elaneu.github.io"

# Change to the repository directory
os.chdir(repo_dir)

# Check if the current directory is a Git repository
if not os.path.exists(os.path.join(repo_dir, ".git")):
    print("Error: The specified directory is not a Git repository.")
    exit(1)

# Function to generate HTML files
def generate_html_file(filename, title, content):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: yellow;
                margin: 0;
                padding: 20px;
            }}
            header {{
                background-color: green;
                color: #fff;
                padding: 10px 0;
                text-align: center;
            }}
            nav ul {{
                list-style-type: none;
                padding: 0;
            }}
            nav ul li {{
                display: inline;
                margin-right: 10px;
            }}
            nav ul li a {{
                color: #fff;
                text-decoration: none;
                cursor: pointer;
            }}
            main {{
                margin-top: 20px;
            }}
            footer {{
                text-align: center;
                padding: 10px 0;
                background-color: #333;
                color: #fff;
                position: absolute;
                bottom: 0;
                width: 100%;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>EVOELA</h1>
            <nav>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="about.html">About Me</a></li>
                    <li><a href="projects.html">Projects</a></li>
                    <li><a href="contact.html">Contact</a></li>
                </ul>
            </nav>
        </header>

        <main>
            <section id="{title.lower().replace(' ', '_')}">
                <h2>{title}</h2>
                <p>{content}</p>
            </section>
        </main>

        <footer>
            <p>&copy; 2024 EVOELA</p>
        </footer>
    </body>
    </html>
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(html_content)
    print(f"Web page generated and saved as {filename}")

# Generate the HTML files
generate_html_file("index.html", "Home", "This is the homepage of EVOELA, where we explore innovative educational methodologies.")
generate_html_file("about.html", "About Me", "Here will be your info.")
generate_html_file("projects.html", "Projects", "Here will be your info.")
generate_html_file("contact.html", "Contact", "Here will be your info.")

# Git operations
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "Update webpage content"], check=True)
subprocess.run(["git", "push", "origin", "main"], check=True)

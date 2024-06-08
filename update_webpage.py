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

# Step 1: Generate the HTML file
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EVOELA</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: yellow; /* Background color changed to yellow */
            margin: 0;
            padding: 20px;
        }
        header {
            background-color: #333;
            color: #fff;
            padding: 10px 0;
            text-align: center;
        }
        nav ul {
            list-style-type: none;
            padding: 0;
        }
        nav ul li {
            display: inline;
            margin-right: 10px;
        }
        nav ul li a {
            color: #fff;
            text-decoration: none;
            cursor: pointer;
        }
        main {
            margin-top: 20px;
        }
        section {
            display: none;
        }
        footer {
            text-align: center;
            padding: 10px 0;
            background-color: #333;
            color: #fff;
            position: absolute;
            bottom: 0;
            width: 100%;
        }
    </style>
    <script>
        function showSection(id) {
            var sections = document.querySelectorAll('section');
            sections.forEach(function(section) {
                section.style.display = 'none';
            });
            document.getElementById(id).style.display = 'block';
        }

        // Show the home section by default
        window.onload = function() {
            showSection('home');
        };
    </script>
</head>
<body>
    <header>
        <h1>EVOELA</h1>
        <nav>
            <ul>
                <li><a onclick="showSection('home')">Home</a></li>
                <li><a onclick="showSection('about')">About Me</a></li>
                <li><a onclick="showSection('projects')">Projects</a></li>
                <li><a onclick="showSection('contact')">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="home">
            <h2>Home</h2>
            <p>This is the homepage of EVOELA, where we explore innovative educational methodologies.</p>
        </section>

        <section id="about">
            <h2>About Me</h2>
            <p>Was ist Evolutionspädagogik (EVOPÄD)?
            Erklärungen des Geschehnisse, Gedanken, Gefühle und Fertigkeiten aus der Evolutionsgeschichte nach dem EVOPÄD Prinzip.
            Die neuesten Erkenntnisse aus der Gehirnforschung werden eingesetzt. Sie zeigen, dass das menschliche Gehirn sich im Laufe der Evolution in sieben Stufen entwickelt hat: von der Einzelle, des Reptils, des Säugetiers bis hin zum Affen, dem Menschen und schließlich dem denkenden Menschen.

            Die sieben Stufen greifen ineinander über und stehen in einer Wechselwirkung zueinander. Jede Entwicklungsstufe gibt uns eine bestimmte Erlebniswelt und erfordert bestimmte Fähigkeiten und Sicherheit.

            Dieses Evolutionsstufenmodell stellt eine gesamte Methode zur Verfügung, um Blockaden direkt einzuwirken, Verhaltensmuster und Defizite aufzulösen und unser Potenzial an Fähigkeiten zu erkennen und zu entfalten.

            » Evolutionspädagogik heißt Entfaltungspädagogik «.</p>
        </section>

        <section id="projects">
            <h2>Welche Mittel nutzt EVOPÄD?</h2>
            <p>
            Beobachten: Wie werden Informationen in Stresssituationen verarbeitet?
            Wahrnehmen: Aus welcher Gehirnentwicklungsstufe heraus agiert und reagiert der Mensch gerade (Evostufe)?
            Erkennen: Aus welchem Grund werden spezielle Schlüsse gezogen? Welche Folgen hat es?
            Bewegung: Evopäden gezielt aussuchen und trainieren, Defizite können sich auflösen, Talente zeigen sich und Gleichgewicht entwickelt sich.
            Anerkennen: Jeder Mensch hat Stärken und Talente. Jeder Mensch kann etwas. Talente zeigen sich, wenn sie anerkannt werden.
            Selbstsicherheit: Stress, Spannungen und Konflikte sind unvermeidbar und gehören zum Leben. Es wäre unnatürlich, dies alles aus dem Weg zu gehen. Wir haben gelernt, mit Stress, Spannungen und Konflikten umzugehen und sie zu lösen. Um ein konstruktiv mit Konflikten umgehen zu können, haben wir ein Handlungsfähigkeitsmodell entwickelt.
            Was ich nicht bauen kann, kann ich nicht verstehen. Wo Hand und Kopf (Hirn) zusammen arbeiten, entsteht Werkzeug.

            » EVOPÄD heißt „LERNEN“ durch „TUN“ «.</p>
        </section>

        <section id="contact">
            <h2>Contact</h2>
            <p>Contact information will go here.</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 EVOELA</p>
    </footer>
</body>
</html>
"""

# Write the HTML content to a file
with open("index.html", "w") as file:
    file.write(html_content)

print("Web page generated and saved as index.html")

# Step 2: Add the file to the staging area
subprocess.run(["git", "add", "index.html"], check=True)

# Step 3

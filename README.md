Story-Ordner Sceleton is as follows:<br>
Ordner "Story":<br>
    Ordner "Speekers":<br>
        Images of all speekers<br>
    Order "Icons":<br>
        Images of all Icons<br>
    Ordner "Scenes":<br>
        Ordner "[Scenename]":<br>
            Background Image as "background.jpeg"<br>
            Ordner "Choices":<br>
                Textfile for "choice(1..n).json":<br>
                    "choicename": as string<br>
                    (next) "scenename": as string<br>
            Textfile for "status.json":<br>
                "status": "Beginning"/"Middle"/"End" of this story<br>
            Ordner "Texts":<br>
                Textfile for "text(1..n).json":<br>
                    "text": is the text<br>
                    "speekername": is the name of the speeker (with .jpeg)<br>

In the "Dummies"-Folder, there are some (or at least one) "Scene"-Folder, which one can COPY into the "Dump"-Folder to test the filehandling.<br>

the syntax of the .json-files are as default:<br>
Example "choice1.json":<br>
"<br>
{<br>
    "choicename": "Let's go!",<br>
    "scenename": "In the lab 2"<br>
}<br>
"<br>

Example "text1.json":<br>
"<br>
{<br>
    "text": "Hi! How are you?",<br>
    "speekername": "I.jpeg"<br>
}<br>
"<br>
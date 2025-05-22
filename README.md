Story-Ordner Sceleton is as follows:
Ordner "Story":
    Ordner "Speekers":
        Images of all speekers
    Order "Icons":
        Images of all Icons
    Ordner "Scenes":
        Ordner "[Scenename]":
            Background Image as "background.jpeg"
            Ordner "Choices":
                Textfile for "choice(1..n).json":
                    "choicename": as string
                    (next) "scenename": as string
            Textfile for "status.json":
                "status": "Beginning"/"Middle"/"End" of this story
            Ordner "Texts":
                Textfile for "text(1..n).json":
                    "text": is the text
                    "speekername": is the name of the speeker

In the "Dummies"-Folder, there are some (or at least one) "Scene"-Folder, which one can COPY into the "Dump"-Folder to test the filehandling.

the syntax of the .json-files are as default:
Example "choice1.json":
"
{
    "choicename": "Let's go!",
    "scenename": "In the lab 2"
}
"

Example "text1.json":
"
{
    "text": "Hi! How are you?",
    "speekername": "I"
}
"
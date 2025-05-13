Story-Ordner Sceleton is as follows:
Ordner "Story":
    Ordner "Speekers":
        Images of all speekers
    Order "Icons":
        Images of all Icons
    Ordner "Scenes":
        Ordner "Scenename":
            Background Image as "background.png"
            Textfile for "choice(1..n).json":
                "choicename": as string
                next "scenename": as string
            Textfile for "status.json":
                "status": "Beginning"/"Middle"/"End" of this story
            Ordner "Texts":
                Textfile for "text(1..n).json":
                    "text": is the text
                    "speekername": is the name of the speeker


the syntax of the .json-files are as default:
Example 1:
"
{
    "choicename": "Let's go!"
    "scenename": "In the lab"
}
"
Example 2:
"
{
    "text": "Hi!\nHow are you?"
    "speeker": "I"
}
"
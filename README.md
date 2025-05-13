Story-Ordner Sceleton is as follows:
Story:
    Speekers:
        Images of all speekers
    Icons:
        Images of all Icons
    Scenes:
        Scene-name:
            Background Image as .png
            Textfile for "choice(1..n)" as .json:
                "choicename": as string
                next "scenename": as string
            Textfile for Status as .json:
                "status": "Beginning"/"Middle"/"End" of this story
            Texts:
                Textfile for "Text(1..n)" as .json:
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
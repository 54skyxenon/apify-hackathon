# Sign Friendly

## Features

This Sign Friendly scraping and automation tool was designed to run on top of the sign language translator app Sign Friendly for Android. Its purpose is to facilitate every-day communication for newly-deaf people or for deaf people with non-deaf people.

The free Sign Friendly actor allows you to [scrape](https://apify.com/web-scraping) ASL software and sign language websites for the translation of text into sign language in different languages. It is an ideal and quick solution if you find yourself in need of conveying a simple message in sign language but don't know where to start. It is designed to extract the sign translation of any word in two different formats:
 - spelling of the word, letter by letter, in sign language alphabet
 - word translated in sign language

This actor was successfully developed during [HackPrague 2021](https://www.hackprague.com/hackathon2021), where it won a sponsored prize for the Apify challenge.

## Tutorial

You can read more about the actor, its creation and its original usage [in this article](https://www.linkedin.com/pulse/welcome-sign-friendly-actor-app-iskra-rizovska/).

## How to use extracted sign language data

The Sign Friendly actor can be used to help communication for newly-deaf people, or for deaf people with non-deaf people. Other possible uses may include:

 - creating a translation app
 - designing a basic American/Czech/German Sign Language, dictionary (such as a sign language dictionary app)
 - shaping a basic sign language course
 - communicating with a non-verbal autistic person
 - communicating with a child who hasn't learnt how to speak yet
 - expanding one's vocabulary

At present, the translation is available in the following languages:
 - English (US)
 - Czech
 - German

## Input

Sign Friendly makes it easier for you to fill in the required fields, which are language and word. You can select the language from a drop-down menu and type the word you want translated into the "word" field.

Your input in JSON should look something like this:

{
  "word": "university",
  "language": "English (United States)"
}

## Output

Once you run the actor, you can view the output in JSON format in the Key-value store section. The output will consist in a PNG image with the sign for each of the letters that make up the word and an MP4 video of the word in sign language. It should look something like this:

{
  "video_url": "https://media.spreadthesign.com/video/mp4/13/58402.mp4",
  "image_urls": [
    "https://raw.githubusercontent.com/54skyxenon/apify-hackathon/main/assets/us/u.png",
    "https://raw.githubusercontent.com/54skyxenon/apify-hackathon/main/assets/us/n.png",
    "https://raw.githubusercontent.com/54skyxenon/apify-hackathon/main/assets/us/i.png",
    "https://raw.githubusercontent.com/54skyxenon/apify-hackathon/main/assets/us/v.png",
    "https://raw.githubusercontent.com/54skyxenon/apify-hackathon/main/assets/us/e.png",
    "https://raw.githubusercontent.com/54skyxenon/apify-hackathon/main/assets/us/r.png",
    "https://raw.githubusercontent.com/54skyxenon/apify-hackathon/main/assets/us/s.png",
    "https://raw.githubusercontent.com/54skyxenon/apify-hackathon/main/assets/us/i.png",
    "https://raw.githubusercontent.com/54skyxenon/apify-hackathon/main/assets/us/t.png",
    "https://raw.githubusercontent.com/54skyxenon/apify-hackathon/main/assets/us/y.png"
  ]
}

Keep in mind that the actor stores the results in Key-value store rather than in Dataset.

## Limitations

The main limitation of this actor is that it only works for single words rather than sentences. If you type a whole sentence or phrase into the input field, the result will only consist of the spelling for the single letters, rather than the Sign Language translation of the whole.

## Feedback

While only three languages are available at this time, the actor is under constant development and more languages will be added in the future. Feel free to [contact us](mailto:support@apify.com) for any suggestions or improvements.
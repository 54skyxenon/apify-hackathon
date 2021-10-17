# Sign Friendly

Sign Friendly is a mobile app for the deaf that translates words from multiple languages into that language's sign language representation. This is our actor deployed on the [Apify](https://apify.com) platform, written in Python 3. It scrapes for a video clip of a word's sign language translation and images of its sign language spelling. The mobile app frontend is written in Kotlin and can be found at this [GitLab repository](https://gitlab.com/petra.cende/sign-friendly).

![Sign Friendly logo](sh-logo.png)

## Installation

You can try out the scraper locally by cloning the repository and installing required packages. Write your own tests in the main block.

```bash
pip install -r requirements.txt
python3 scraper.py
```

## Usage
Example of input JSON, the `language` and `word` fields are required. Do not forget to pass in `application/json; charset=utf-8` for the `Content-Type` header!
```json
{
    "language": "Czech",
    "word": "Řidič" 
}
```

Languages supported are:
- `English (United States)`
- `Czech`
- `German (Germany)`

Example of response JSON (this might take a while to load):
```json
{
  "video_url": ".../ridic.mp4",
  "image_urls": [
    ".../assets/cz/r.png",
    ".../assets/cz/hook.png",
    ".../assets/cz/i.png",
    ".../assets/cz/d.png",
    ".../assets/cz/i.png",
    ".../assets/cz/c.png",
    ".../assets/cz/hook.png"
  ]
}
```


## Contributing
Currently only these languages are supported: American English, Czech, German. Pull requests are welcome to add support for more languages.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

# Spotify: Playlist from Text

1. Details

2. How to generate your own playlist

3. License

4. Credits

## 1. Details

- With this software, you are able to build a playlist, in which the song titles represent the text you entered.

- Here is an example:

  - The text "I love developing" will result in the following playlist:

  - | Songtitle  | Spotify ID                           |
    | ---------- | ------------------------------------ |
    | I Love     | spotify:track:30z4LVkScpeNhwHFIB8Ewa |
    | Developing | spotify:track:50Xu1K7QVR3RG5bXDPYmEp |

- This does not work for every text, since not every combination of words has a song that can represent it, but many of them do work

## 2. How to generate your own playlist

### 2.1 Cloud Execution

- Instead of installing this software locally on your computer, you are able to execute it in the [cloud](https://repl.it/@Tim_LucaL/spotify-playlist-from-text).

- After opening the page, click run and wait until are asked for the text you want to transform into a playlist.

- If your text can be converted to a playlist, you get a list of ID's which you can paste into a spotify playlist.

- If it does not work, just enter a new text.

### 2.2 Local Installation

#### 2.2.1 Installation

First, you need to clone or download this repository, open the folder and execute this command:

```bash
pip3 install -r requirements.txt
```

#### 2.2.2 Usage

First, you need to import the module

```python
import spotify_text
```

Then, you have to create a SpotifyText object. To do that, you need to replace the client id and secret from spotify with your own ones.

```python
st = SpotifyText("<spotify_client_id>",
                 "<spotify_client_secret>",
                 verbose=True
)
```

If you want to generate the playlist, type:

```python
st.generate_playlist("I love developing!", max_title_length=10)

# This will return a list if the playlist is generated successfully, else False
```

# 3. License

The code is published under the MIT License.

# 4. Credits

The code is developed by Tim-Luca Lagmöller.


# 5. Donations / Sponsors

I'm part of the official GitHub Sponsors program where you can support me on a monthly basis.

<a href="https://github.com/sponsors/lagmoellertim" target="_blank"><img src="https://github.com/lagmoellertim/shared-repo-files/raw/main/github-sponsors-button.png" alt="GitHub Sponsors" height="35px" ></a>

You can also contribute by buying me a coffee (this is a one-time donation).

<a href="https://ko-fi.com/lagmoellertim" target="_blank"><img src="https://github.com/lagmoellertim/shared-repo-files/raw/main/kofi-sponsors-button.png" alt="Ko-Fi Sponsors" height="35px" ></a>

Thank you for your support!



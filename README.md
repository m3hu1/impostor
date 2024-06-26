# Impostor

Impostor is a Python script that identifies Instagram accounts you are following but are not following you back. It uses the `instaloader` library to interact with Instagram and fetch follower and following data.<br>

**No need to use any fishy third-party apps!**


## Installation

1. Clone the repository or download the zip:
    ```
    git clone https://github.com/m3hu1/impostor.git
    ```
2. Navigate to the project directory:
    ```
    cd impostor
    ```
3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
    or
    ```
    pip3 install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```
    python impostor.py
    ```
    or
    ```
    python3 impostor.py
    ```
3. Enter your username in the terminal.
4. Enter your password when prompted (input will be hidden).
5. If 2FA is enabled, enter the 2FA code when prompted.

## Example

```sh
$ python impostor.py
Enter your username: your_username
Enter your password:
Two-factor authentication (2FA) is enabled on your account.
Enter the 2FA code: 123456
Here are the impostors:

impostor_user1
impostor_user2
```
<br>

> This uses [instaloader](https://instaloader.github.io/) module to fetch instagram data which is an open-source python library, therefore it is safe to do this and won't get your instagram account credentials stolen.



## DISCLAIMER

While using this tool is generally safe, Instagram's terms of service do not allow automated scraping or interaction with their platform. Use this script at your own risk.
Using this tool once or twice should still be safe.

However, if you want to be completely safe, you can make your original account public, make a new instagram account and pass those credentials in `impostor_public.py` and then provide the username of your original instagram account when prompted and that should keep your original account completely safe from any types of warnings or bans.

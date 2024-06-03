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

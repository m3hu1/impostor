import instaloader
import getpass

def login_instaloader():
    instance = instaloader.Instaloader()

    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    try:
        instance.login(username, password)
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        print("Two-factor authentication (2FA) is enabled on your account.")
        twoFA = input("Enter the 2FA code: ")
        instance.context.two_factor_login(twoFA)

    return instance

def fetchPublicFollowData(instance, username):
    profile = instaloader.Profile.from_username(instance.context, username)

    currFollowers = {follower.username for follower in profile.get_followers()}
    currFollowing = {following.username for following in profile.get_followees()}

    return currFollowers, currFollowing

def findImpostors(followings, followers):
    dhokebaaz = followings - followers
    return dhokebaaz

def getFullName(instance, username):
    profile = instaloader.Profile.from_username(instance.context, username)
    return profile.full_name

if __name__ == '__main__':
    instance = login_instaloader()
    username = input("Enter the public username to analyze: ")

    followers, followings = fetchPublicFollowData(instance, username)

    dhokebaaz = findImpostors(followings, followers)

    print("Here are the impostors with their profile links and full names:\n")
    for idx, user in enumerate(dhokebaaz, 1):
        full_name = getFullName(instance, user)
        profile_link = f"https://www.instagram.com/{user}"
        print(f"{idx}. {user}, {full_name}, {profile_link}")


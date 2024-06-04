import instaloader
import getpass # bhai yeh aapka password hide karne ke liye hai, naam thoda weird hai but kaam accha hai

def fetchFollowData(username, password):
    instance = instaloader.Instaloader()

    try:
        instance.login(username, password)

    except instaloader.exceptions.TwoFactorAuthRequiredException:
        print("Two-factor authentication(2FA) is enabled on your account.")
        twoFA = input("Enter the 2FA code: ")
        instance.context.two_factor_login(twoFA)

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
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ") # Added this to hide the password while typing
    # password = input("Enter your password: ")

    followers, followings = fetchFollowData(username, password)

    dhokebaaz = findImpostors(followings, followers)

    instance = instaloader.Instaloader()

    print("Here are the impostors with their profile links and full names:\n")
    for idx, user in enumerate(dhokebaaz, 1):
        full_name = getFullName(instance, user)
        profile_link = f"https://www.instagram.com/{user}"
        print(f"{idx}. {user}, {full_name}, {profile_link}")

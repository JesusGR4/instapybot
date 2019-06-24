
from InstagramAPI import InstagramAPI


def validate_instagram_account(instagram_account, instagram_password):
    instagramApiObject = InstagramAPI(instagram_account, instagram_password)
    instagramApiObject.login()
    return instagramApiObject.isLoggedIn


from django.db import models
from django.contrib.auth.models import AbstractUser

STATUS = {'ACTIVE': True,
          'DISABLED': False,
          'FOLLOWED': True,
          'UNFOLLOWED': False}


# User Entity: Main entity which contains User info
class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)  # Created date added by itself
    modified_at = models.DateTimeField(auto_now=True, blank=True)  # We we'll get a little log in User Changes

    def __str__(self):
        return self.email


# Instagram_Account entity: It represents all Instagram Accounts related to a User
class InstagramAccount(models.Model):
    instagram_account_name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(
        default=STATUS['ACTIVE'])  # This status represents if Instagram Account is active or not
    created_date = models.DateTimeField(auto_now_add=True, blank=True)  # Created date added by itself
    modified_at = models.DateTimeField(auto_now=True,
                                       blank=True)  # We we'll get a little log in Instagram_Account Changes

    def __str__(self):
        return self.name


# Strategy entity: It represents the strategy which will be used by internal bot if active
class Strategy(models.Model):
    strategy_name = models.CharField(max_length=150)
    instagram_account = models.ForeignKey(InstagramAccount, on_delete=models.CASCADE)
    status = models.BooleanField(default=STATUS['ACTIVE'])  # This status represents if Strategy is active or not
    created_date = models.DateTimeField(auto_now_add=True, blank=True)  # Created date added by itself
    modified_at = models.DateTimeField(auto_now=True, blank=True)  # We we'll get a little log in Strategy Changes

    def __str__(self):
        return self.strategy_name


# Influencer entity: It represents the influencer-strategy. It means, here we are goint to configure
# how many users to follow and all functional requisites in README included
class Influencer(models.Model):
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)
    influencer_instagram_id = models.CharField(
        max_length=255)  # I don't really know in this moment if needed and the type de Instagram ID from API Oficial Instagram
    name = models.CharField(max_length=150)  # Influencer name, it will be the @ on Instagram
    number_of_users_to_follow = models.PositiveIntegerField(
        default=0)  # It represents how many users follow in the schedule
    days_has_to_pass_to_unfollow = models.PositiveIntegerField(default=0)  # It sets how many days has to unfollow
    initial_time_to_follow = models.TimeField()  # Initial hour to follow people
    final_time_to_follow = models.TimeField()  # Final hour to follow people
    status = models.BooleanField(default=STATUS['ACTIVE'])  # This status represents if Strategy is active or not
    created_date = models.DateTimeField(auto_now_add=True, blank=True)  # Created date added by itself
    modified_at = models.DateTimeField(auto_now=True, blank=True)  # We we'll get a little log in Influencer Changes

    def __str__(self):
        return self.name


# It represents the person followed from a single Influencer
class InfluencerFollow(models.Model):
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)
    follow_instagram_id = models.CharField(
        max_length=255)  # I don't really know in this moment if needed and the type de Instagram ID from API Oficial Instagram
    status = models.BooleanField(default=STATUS['ACTIVE'])  # This status represents if user is active or not
    is_followed = models.BooleanField(default=STATUS['FOLLOWED'])
    follow_date = models.DateTimeField(auto_now_add=True, blank=True)  # Created date added by itself
    unfollow_date = models.DateTimeField(null=True, blank=True)  # We we'll get a little log in InfluencerFollow Changes

    def __str__(self):
        return self.follow_instagram_id


# It represents the hashtag which user wants to work on.
class Hashtag(models.Model):
    hashtag_name = models.CharField(max_length=150)
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)
    number_of_likes_per_day = models.PositiveIntegerField(default=0)
    initial_time_to_like_posts = models.TimeField()
    final_time_to_like_posts = models.TimeField()
    initial_time_to_comment_posts = models.TimeField()
    final_time_to_comment_posts = models.TimeField()
    status = models.BooleanField(default=STATUS['ACTIVE'])  # This status represents if Hashtag is active or not
    created_date = models.DateTimeField(auto_now_add=True, blank=True)  # Created date added by itself
    modified_at = models.DateTimeField(auto_now=True, blank=True)  # We we'll get a little log in Influencer Changes

    def __str__(self):
        return self.hashtag_name


# It represents liked post on Instagram
class LikedPost(models.Model):
    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
    id_instagram_liked_post = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)  # Created date added by itself

    def __str__(self):
        return self.id_instagram_liked_post


# It represents every word can be used to create a sentence on Instagram post
class Word(models.Model):
    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
    order_in_sentence = models.PositiveIntegerField(
        default=0)  # Zero is the first position of the sentence, This attribute represents the word's position in sentence
    content = models.CharField(max_length=30)
    status = models.BooleanField(default=STATUS['ACTIVE'])  # This status represents if Word is active or not
    created_date = models.DateTimeField(auto_now_add=True, blank=True)  # Created date added by itself
    modified_at = models.DateTimeField(auto_now=True, blank=True)  # We we'll get a little log in Word Changes

    def __str__(self):
        return self.content


# Here we have all post which the bot has commented
class Post(models.Model):
    id_instagram_commented_post = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)  # Created date added by itself
    words = models.ManyToManyField(Word)

    def __str__(self):
        return self.id_instagram_commented_post

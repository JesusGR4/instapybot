# Instapybot - Functional requirements
Instagram bot for making multiple needs true. Python developed. 

In this first development, we are going to develop a basics administration's panel where users can 
link Instagram accounts they need and make a singular strategies by account.

Requirements as anonymous 
-------------------------

1. Create an account

Requirements as User 
-------------------------

1. List Instagram accounts related to the User.

2. Register an Instagram account.

3. List strategies for Instagram account.

4. Create a strategy for an account. When strategy is created, 
the system must allow to config the following:
    1. Set a list of hashtag target.
    2. Set how many users follow per day related to a hashtag.
    3. Set a list of influencers.
    4. Set how many users follow per day related to a influencers.
    5. Set a list of commentaries to write in posts related to a hashtag.
    6. Set how many likes give in posts related to a hashtag.
    7. Show the list of likes given. System must allow to choose the day to show.
    8. Set the schedule that the system must like posts.
    9. Set the schedule that the system must comment posts.
    10. Set the schedule that the system must follow people.
    11. Set how many people unfollow who didn't folloy to the account.
5. Choose which strategy is active. Just one strategy can be active.
    
Infrastructure 
-------------------------

1. MongoDB as database.
2. Django as web framework.
3. Docker as working environment.

How to deploy?
-------------------------

1. First, clone the repo.
2. Checkout to develop branch.
3. Move to instapybot and run the following

`docker-compose build`

`docker-compose up`


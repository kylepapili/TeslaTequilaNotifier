# TeslaTequilaNotifier
A Notification Script For The Acquisition of Tesla Tequila

![Image of Tesla Tequila](https://teslatequila.tesla.com/static/3ca9efa457040d7e7ffa1988d2dbcc41/f6840/tesla-tequila-product%402x.jpg)


# Join The [Instant Notification Slack Workspace](http://papili.us/teslatequila)
I have created a website for users to join the Tesla Instant Notification System. This eliminates the need for you to go through the difficulties associated with running this program at all times.

# Usage
Clone the Repository

    git clone https://github.com/kylepapili/TeslaTequilaNotifier.git
    
Setup a [Slack Workspace](https://slack.com/help/articles/206845317-Create-a-Slack-workspace)

Setup a [Slack App](https://slack.com/help/articles/202035138-Add-apps-to-your-Slack-workspace)

Create two channels (#hourlyupdates and #alert)

[Add the Slack App](
https://stackoverflow.com/questions/60198159/slack-api-conversations-history-returns-error-not-in-channel) to Both Channels

Update the *slackToken.txt* file with your Slack App Token

Run the Script

    python notifier.py

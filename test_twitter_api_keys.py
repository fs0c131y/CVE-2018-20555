import csv
import optparse
import time
import tweepy


def retweet(api, id):
    try:
        api.retweet(id)
    except tweepy.TweepError as error:
        print(error)


def create_favorite(api, id):
    try:
        api.create_favorite(id)
    except tweepy.TweepError as error:
        print(error)


def get_me(api):
    try:
        return api.me()
    except tweepy.TweepError as error:
        print(error)


def test_credentials(api):
    me = get_me(api)
    if me is not None:
        print(str(line_count) + ': ' + 'screen_name = ' + me.screen_name +
              ', followers = ' + str(me.followers_count) + ', verified = ' + str(me.verified))


def authentication(consumer_key, consumer_secret, access_token, access_secret):
    try:
        # Twitter auth
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        return api
    except tweepy.TweepError as error:
        print(error)


def set_up_menu():
    parser = optparse.OptionParser()

    parser.add_option('-t', '--test-credentials',
                      action="store_true", dest="test",
                      help="Test credentials", default="False")
    parser.add_option('-l', '--like',
                      action="store", dest="like",
                      help="ID of the tweet to like", default="0")
    parser.add_option('-r', '--retweet',
                      action="store", dest="retweet",
                      help="ID of the tweet to retweet", default="0")

    return parser.parse_args()


if __name__ == '__main__':
    options, args = set_up_menu()

    with open('twitter_keys.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                api = authentication(row[1], row[2], row[3], row[4])
                if options.test == True:
                    test_credentials(api)
                elif options.like != "0":
                    create_favorite(api, options.like)
                elif options.retweet != "0":
                    retweet(api, options.retweet)

                line_count += 1

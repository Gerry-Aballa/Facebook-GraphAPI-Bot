import requests
import schedule
import keys
import time


# Grap API URL that allows appropriate user to post
POST_URL = f'https://graph.facebook.com/v18.0/{keys.PAGE_ID}/feed'

# Text that is to be posted
post_message = 'Hello Python 🐍. I bet you are awesome today!🚀🚀.\nI am a bot 🤖. Meet me on Github'

# Paylod - parameters sent over the API
post_data = {
    'message': post_message,
    'link': f'https://github.com/Gerry-Aballa/Facebook-GraphAPI-Bot',
    'access_token': keys.PAGE_ACCESS_TOKEN
}
def sendPost():
    # Send a POST request to the specified URL
    response = requests.post(POST_URL, data=post_data)

    # Print a message to indicate that the request was successful
    print("Posted successfully!")


schedule.every().day.at("08:00").do(sendPost) # Run everyday at the set time


while True:
    schedule.run_pending()
    time.sleep(1)


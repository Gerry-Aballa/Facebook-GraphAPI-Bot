# Facebook Graph API Bot

Meet me on this [Facebook page](https://www.facebook.com/profile.php?id=61551872334297)

This is a Python script for automating Facebook posts using the Facebook Graph API. The script allows you to schedule posts at specific times every day. It's useful for users who want to regularly share updates or content on their Facebook page without manual intervention.

## Prerequisites

Before using this script, you need to have the following:

1. **Facebook Page**: You should have a Facebook Page where you want to schedule posts.

2. **Facebook Developer Account**: You need to create a Facebook Developer account and create a Facebook App. This app will provide you with the necessary API credentials.

3. **Access Token**: You need to generate a Page Access Token for your Facebook Page. This token allows the script to post on your behalf. Ensure that this token has the required permissions to post on the Page.

4. **Python Dependencies**: You must have Python installed on your system along with the `requests` and `schedule` libraries. You can install these libraries using pip and `requirements.txt`

    ```
    pip install -r requirements.txt
    ```

## Configuration

Before running the script, you need to configure it by creating the `keys.py` file. Replace the placeholders with your actual Facebook Page ID and Page Access Token.

```python
# keys.py

PAGE_ID = 'your_page_id_here'
PAGE_ACCESS_TOKEN = 'your_page_access_token_here'
```

## Usage

1. **Define Your Post Content**: Modify the `post_message` variable to specify the text of the post you want to schedule. You can also include a link if desired.

2. **Schedule Posting Time**: Adjust the `schedule.every().day.at("08:00").do(sendPost)` line to set the time at which you want the post to be scheduled. By default, it's set to 08:00 AM.

3. **Run the Script**: Run the script using the following command:

    ```
    python3 facebook.py
    ```

4. **Sit Back and Relax**: The script will run continuously and post your scheduled content at the specified time every day.

## Important Notes

- Make sure your Page Access Token remains valid. If it expires, you'll need to regenerate a new token and update it in the `keys.py` file.

- Facebook's API may change over time, so ensure that your app and script are compatible with the current API version.

- This script is for educational and personal use. Please use it responsibly and ensure your posts comply with Facebook's terms and policies.

- You can find more information about the Facebook Graph API in the [official documentation](https://developers.facebook.com/docs/graph-api).

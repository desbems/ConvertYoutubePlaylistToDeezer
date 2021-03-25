# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def Liked():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "code.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    page_token = ""
    while True:
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            maxResults=50,
            myRating="like",
            pageToken= page_token
        )
        response = request.execute()
        if 'nextPageToken' in response:
            page_token = response['nextPageToken']                  
        #* save titles in a list
        titles = []
        with open('videos.txt', 'a') as f:
            for item in response['items']:
                titleList = item['snippet']['title']
                f.write(titleList)
                f.write('\n')
        if 'nextPageToken' not in response:
            print('finished')
            break



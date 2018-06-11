def checkVideoById(ID):
    """
    Uses the youtube API to check if we have a valid ID
    :param ID: The ID to be checked
    :return: The title of the video
    """

    from configHandler import config
    import googleapiclient.discovery as yt
    youtube = yt.build(serviceName=config('Youtube','apiService'), 
                       version=config('Youtube','apiVersion'),
                       developerKey=config('Youtube','clientKey'))
    
    video = youtube.videos().list(
        id=ID,part='snippet'
    ).execute()

    # If we have a valid ID, and presumebly a valid video, we get a reponse of length 1
    if len(video.get("items",[])) == 1:
        return video.get("items",[])[0]['snippet']['title']
    return ""
def regex_(source_url):
    """seperates blob and bucket name from google cloud storage gs link"""
    import re
    
    match = re.match(r'gs://([^/]+)/(.+)', source_url)# seperating blob name and file name
    prefix = match.group(2)
    #print(prefix)# blob name of file
    bucket_name = match.group(1)
    #print(bucket_name)#bucket name
    return bucket_name +'+'+ prefix



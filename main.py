from urllib.request import urlopen
import time

def get_load_time(url: str) -> float:
    """
    This function takes a user-defined URL as input and returns the time taken to load that URL in seconds.
    Args:
        url (str): The user-defined URL.
    Returns:
        float: The time taken to load the website in seconds.
    """
    if 'https' in url or 'http' in url: 
        open_this_url = urlopen(url)
    else:
        open_this_url = urlopen('https://' + url)
    
    start_time = time.time()
    open_this_url.read()
    end_time = time.time()
    
    open_this_url.close()
    
    time_to_load = end_time - start_time
    return time_to_load

if __name__ == "__main__":
    url = input("Enter the URL whose loading time you want to check: ")
    print(f'\nThe time taken to load {url} is {get_load_time(url):.2f} seconds.')
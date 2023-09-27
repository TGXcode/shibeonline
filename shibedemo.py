import requests

def get_shibe_images(count=1, urls=True, httpsUrls=True):
    base_url = "http://shibe.online/api/shibes?"
    params = {
        "count": count,
        "urls": str(urls).lower(),
        "httpsUrls": str(httpsUrls).lower()
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception if the request was not successful

        # Parse the response as JSON
        data = response.json()

        if isinstance(data, list):
            for image_url in data:
                print(image_url)
        else:
            print("Failed to retrieve shibe images.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    count = input("Enter the number of shibe images you want (1-100): ")
    try:
        count = int(count)
        if 1 <= count <= 100:
            get_shibe_images(count)
        else:
            print("Please enter a number between 1 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

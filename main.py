import requests

def send_friend_requests(cookie, csrf_token, target_id):
    url = f"https://friends.roblox.com/v1/users/{target_id}/request-friendship"
    headers = {
        "Cookie": cookie,
        "X-CSRF-TOKEN": csrf_token
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        print(f"Friend request sent to user ID: {target_id}")
    else:
        print(f"Failed to send friend request to user ID: {target_id}")

# Get cookie input from the user
cookie = input("Enter the cookie value: ")

# Retrieve X-CSRF-TOKEN from Roblox website
roblox_url = "https://www.roblox.com/home"
roblox_headers = {
    "Cookie": cookie
}
roblox_response = requests.get(roblox_url, headers=roblox_headers)
csrf_token = roblox_response.headers.get("X-CSRF-TOKEN")

# Read user IDs from users.txt file
with open("users.txt", "r") as file:
    user_ids = file.read().splitlines()

# Send friend requests for each user ID
for user_id in user_ids:
    send_friend_requests(cookie, csrf_token, user_id)

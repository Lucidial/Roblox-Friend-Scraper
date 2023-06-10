import requests

def get_user_friends(user_id):
    url = f"https://friends.roblox.com/v1/users/{user_id}/friends?userSort=0"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        friend_ids = [friend['name'] for friend in data['data']]
        return friend_ids
    else:
        print("Failed to retrieve user friends.")
        return []

def save_user_ids(user_ids):
    with open('users.txt', 'w') as file:
        for user_id in user_ids:
            file.write(str(user_id) + '\n')

# Get user ID input from the user
user_id = input("Enter the user ID: ")

# Send GET request and retrieve friend IDs
friend_ids = get_user_friends(user_id)

# Save friend IDs to users.txt
save_user_ids(friend_ids)

print("Friend IDs saved to users.txt")

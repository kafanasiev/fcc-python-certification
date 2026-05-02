# # - user stories by FCC
# ### - my comments

test_settings = {
    'name': 'user',
    'language': 'English',
    'theme': 'light',
    'notifications': 'off'
}

def add_setting(settings, kv):
    ###to unpack kv tuple
    key, val = kv
    #Convert the key and value to lowercase.
    key = key.lower()
    val = val.lower()  
    #If the key setting exists, return Setting '[key]' already exists! Cannot add a new setting with this name.
    for k in settings.keys():
        if k == key:
            return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings.update({f"{key}": f"{val}"})
    return f"Setting '{key}' added with value '{val}' successfully!"



def update_setting(settings, kv):
    key, val = kv

    key = key.lower()
    val = val.lower()

    for k in settings.keys():
        if k.lower() == key.lower():
            settings.update({f"{key}": f"{val}"})
            return f"Setting '{key}' updated to '{val}' successfully!"
        ### no need for 'else:' so that the loop can be finished
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):

    key = key.lower()

    for k in settings.keys():
        if k.lower() == key.lower():
            settings.pop(k)
            return f"Setting '{key}' deleted successfully!"
    ### no need for 'else:' so that the loop can be finished
    return "Setting not found!"

def view_settings(settings):
    if settings == {}:
        return "No settings available."
    else:
        result = 'Current User Settings:\n'
        for key, val in settings.items():
            key = key.capitalize()
            result += f'{key}: {val}\n'
        return result

print(add_setting(test_settings, ("A", "b")))

print(delete_setting(test_settings, 'A'))

print(view_settings(test_settings))



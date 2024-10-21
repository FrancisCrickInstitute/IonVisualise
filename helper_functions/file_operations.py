import os
import time


def remove_old_files(directory="temp_files", days_old=1):
    '''
    Remove files in a directory that are older than a certain number of days.
    '''
    # Get the current time
    current_time = time.time()
    # Calculate how many seconds in a day
    seconds_in_day = days_old * 86400  # 1 day = 86400 seconds

    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Iterate over the files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Get the file's last modification time
            last_modification_time = os.path.getmtime(file_path)

            # If the file hasn't been modified in the past 'days_old' days, remove it
            if current_time - last_modification_time > seconds_in_day:
                # print(
                #     f"Removing {file_path} (last modified: {time.ctime(last_modification_time)})"
                # )
                os.remove(file_path)

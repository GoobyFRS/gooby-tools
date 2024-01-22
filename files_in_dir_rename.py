#!/usr/bin/python3
#Removes a portion of a file name from files within a defined directory.
import os
def main():
    #
    directory = r"S:\BulkMediaStorage\TV Shows\$TVSHOW\$SEASON"
#https://stackoverflow.com/questions/37400974/error-unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3
    print("Starting Rename Job...")
#https://stackoverflow.com/questions/43728163/python-replace-all-spaces-with-underscores-and-convert-to-lowercase-for-all-fil
    [os.rename(os.path.join(directory, f), os.path.join(directory, f).replace('$WHAT2REMOVE', '').lower()) for f in os.listdir(directory)]
    print("Completed Rename Job Successfully")
    #
if __name__ == "__main__":
    main()
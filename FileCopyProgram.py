import os 

# Source and destination to be copied
sourceFileName = "source.doc"
destinationFileName = "destination.doc"

# Buffersize set to around 8KB to keep memory efficiency. 
bufferSize = 8192 

# While loop used to write from source to destination.
with open(sourceFileName, "rb") as sourceFile:
    with open(destinationFileName, "wb") as destinationFile:
        while True: 
            chunk = sourceFile.read(bufferSize)
            if not chunk:
                break
            destinationFile.write(chunk)
            
# Print statements to show that the process has completed, the file exists and lists the path of the directory.
print(f"Copied contents from {sourceFileName} to {destinationFileName}")
print(os.path.exists(sourceFileName))
print(os.getcwd())


# r_file = open("source.doc")
# w_file = open("destination.doc", "w")

# for x in r_file:
#     w_file.write(x)
#     pass
# print("Data has been copied successfully")

# f = open("test", "r")
# f = open("test", "w")
# print(f.read())
# f.close()
# f.write("Hey There\n")
# f.close()

# with open('test') as f:
#     print(f.read())
    


            
# with open('download.jpeg', 'rb') as rf:
#     with open('download_copy.jpeg', 'wb') as wf:
#         chunk_size = 4096
#         rf_chunk = rf.read(chunk_size)
    
#     while len(rf_chunk) > 0:
#         wf.wriite(rf_chunk)
#         rf_chunk(rf_chunk)
        
    
    



# file_to_read = "source.doc"
# write_to_file = "destination.doc"

# file = open(file_to_read, "r")
# data = file.read()
# file.close()

# with open(write_to_file, "a") as file:
#     file.write(data)
# print("Completed")

# source = "Python\Folder 1" # link
# destination = "Python\Folder 2" # link

# destination = copy{source, destination}
# destination = move{source, destination}

# userChoice = input("What would like to do Move: m or Copy: c")
# if (userChoice == "m"):
#     destination = move(source, destination)
# if (userChoice == "c"):
#     destination = copy(source, destination)


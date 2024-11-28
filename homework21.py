#1

import threading

def find_even():
    print("ლუწი რიცხვები 30-დან 50-მდე:")
    for i in range(30, 51):
        if i % 2 == 0:
            print(i)

def find_odd():
    print("კენტი რიცხვები 30-დან 50-მდე:")
    for i in range(30, 51):
        if i % 2 != 0:
            print(i)

# Thread-ების შექმნა
even_thread = threading.Thread(target=find_even)
odd_thread = threading.Thread(target=find_odd)

# Thread-ების გაშვება
even_thread.start()
odd_thread.start()

# Thread-ების დასრულების მოლოდინი
even_thread.join()
odd_thread.join()

print("პროცესი დასრულდა!")



#2

import threading
import requests

# ჩამოსატვირთი ფაილების ლინკები
mp3_urls = [
    "https://example.com/song1.mp3",
    "https://example.com/song2.mp3",
    "https://example.com/song3.mp3"
]

def download_mp3(url, file_name):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(file_name, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            print(f"ჩამოტვირთვა დასრულებულია: {file_name}")
        else:
            print(f"ვერ მოხერხდა {url} ჩამოტვირთვა. სტატუსი: {response.status_code}")
    except Exception as e:
        print(f"შეცდომა {url}-ზე: {e}")

threads = []

# თითოეული mp3 ფაილისთვის ახალი Thread
for i, url in enumerate(mp3_urls):
    file_name = f"song{i+1}.mp3"
    thread = threading.Thread(target=download_mp3, args=(url, file_name))
    threads.append(thread)
    thread.start()

# ყველა Thread-ის დასრულების მოლოდინი
for thread in threads:
    thread.join()

print("ყველა ფაილის ჩამოტვირთვა დასრულდა!")


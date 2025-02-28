# [project]
#buat folder di command prompt: uv init (nama folder) -> sbnrnya w/o brackets
#trus enter, ketik code .
#cd (nama folder) -> klo mau buka folder change directory
#cd .. ->utk balik ke folder sebelumnya
#uv run main.py = run venv in command prompt

from rumus_matematika import RumusMatematika
def main():
    print("Hello from main-app!")

    
def main():
    hasil = RumusMatematika.luas_persegi(4)
    print(hasil)

if __name__ == "__main__":
    main()
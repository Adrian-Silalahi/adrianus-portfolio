import os
from PIL import Image

# Tentukan folder tempat gambarmu berada
folder_path = './dist/img/'

# Loop semua file di folder tersebut
for filename in os.listdir(folder_path):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        # Path lengkap file asli
        file_path = os.path.join(folder_path, filename)
        
        # Buka gambar
        image = Image.open(file_path)
        
        # Nama file baru dengan ekstensi .webp
        new_filename = os.path.splitext(filename)[0] + ".webp"
        new_file_path = os.path.join(folder_path, new_filename)
        
        # Simpan sebagai WebP
        image.save(new_file_path, 'webp', quality=80)
        print(f"Berhasil convert: {filename} -> {new_filename}")

print("Selesai! Semua gambar sudah jadi WebP.")
import os

# Sesuaikan path ini dengan lokasi folder portfolio kamu
folder_path = './dist/img/portfolio/'

# Cek apakah folder tersebut ada
if os.path.exists(folder_path):
    print(f"Sedang memindai folder: {folder_path} ...\n")
    deleted_count = 0
    
    for filename in os.listdir(folder_path):
        # Cek apakah file berakhiran .png
        if filename.endswith(".png"):
            file_path = os.path.join(folder_path, filename)
            try:
                os.remove(file_path) # Perintah hapus
                print(f"🗑️  Dihapus: {filename}")
                deleted_count += 1
            except Exception as e:
                print(f"❌ Gagal menghapus {filename}: {e}")

    if deleted_count == 0:
        print("\nTidak ada file .png yang ditemukan (atau sudah bersih).")
    else:
        print(f"\n✅ Selesai! Total {deleted_count} file .png berhasil dihapus.")
else:
    print(f"❌ Folder tidak ditemukan: {folder_path}")
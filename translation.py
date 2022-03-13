class Translation(object):
    START_TEXT = """Hi {},
Saya Adalah URL Uploader!
Kamu Bisa upload File|Video Ke Telegram dengan direct link, Using this bot!
WEBSITE YANG DI DUKUNG <a href="https://ytdl-org.github.io/youtube-dl/supportedsites.html">HERE</a>
/help Untuk Lainnya!"""
    FORMAT_SELECTION = "Pilih Format Yang Dibawah: <a href='{}'>file size might be approximate</a> \nJika Kamu Ingin Pasang Custom Thumbnail, kirim foto sebelum atau dengan cepat setelah mengetuk salah satu tombol di bawah ini.\nKamu Bisa Pakai /deletethumbnail Untuk Menghapus auto-generated thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """Jika Kamu Ingin download premium videos, Ikuti Format Dibawah Ini:
URL | filename | username | password"""
    DOWNLOAD_START = "📥Downloading..."
    UPLOAD_START = "📤Uploading..."
    RCHD_TG_API_LIMIT = "Downloaded Dalam {} Detik.\nDetected File Size: {}\nMaaf. Tapi, Saya Tidak Bisa Mengupload File Lebih Dari 2GB Karena Pembatasan Telegram API."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Terima Kasih Telah Menggunakan Saya \n\n<b>Join @MustaxProject Untuk Bot Keren Seperti Saya </b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Di Download Dalam {} Detik.\nDi Upload Dalam {} Detik.\n\n@MustaxProject"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail Tersimpan. Gambar Ini Akan Saya Pakai di  video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail Berhasil Di Hapus."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    ABOUT_MSG = """ Something About Me :
    
   ☞My Name  : All Url Uploader Bot

   ☞Updates  : @MustaxProject    

   ☞Language : Python3

   ☞Library  : <a href="https://docs.pyrogram.org/">Pyrogram 1.0.7</a>"""
    HELP_USER = """Please Follow These steps!
    
1. Kirim URL (example.domain/File.mp4 | New Filename.mp4).
2. Kirim Gambar Sebagai Custom Thumbnail (Optional).
3. Pilih Tombol.
   SVideo - Give File as video with Screenshots
   DFile  - Give File (video) as file with Screenshots
   Video  - Give File as video without Screenshots
   File   - Give File without Screenshots

Jika Bot Tidak Merespon, PM Me @BIRD_from_HELL"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
You can use /rename command after receiving file to rename it with custom thumbnail support.
"""
    CANCEL_STR = "Process Dibatalkan"
    ZIP_UPLOADED_STR = "Uploaded {} files Dalam {} Detik"
    SLOW_URL_DECED = "Astaga, sepertinya itu URL yang sangat lambat. Karena Anda mengacaukan Bot saya, saya tidak berminat untuk mengunduh file ini. Sementara itu, mengapa Anda tidak mencoba ini:==> https://shrtz.me/PtsVnf6 dan berikan saya URL cepat sehingga saya dapat mengunggah ke Telegram, tanpa saya memperlambat untuk pengguna lain."

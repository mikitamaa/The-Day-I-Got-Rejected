
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# The game starts here.

label start:
    $ t = Takiya(Character("Takiya"), "Takiya", 0, 0, 0)
    $ n = Heroine(Character("Nana"), "Nana", 0, 0)

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene belakang_sekolah_sore

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    """
    Sore itu tidak seperti sore-sore biasanya.
    
    Matahari terasa lebih hangat, langit terlihat lebih jernih, suasana sekolah juga terasa lebih ceria.
    
    Keceriaan dari canda dan tawa sswa-siswi yang masih berkegiatan memenuhi suasana sekolah. Semua itu mewarnai sore di SMA Kaoshigai.
    
    {i}Pertanda baik, mungkin?{/i}
    
    Haahhhh.... Kuharap dia datang.

    Aku mengajaknya ke belakang sekolah melalui NINE beberapa menit sebelum bel pulang tadi.
    
    Aku tidak tahu apakah pesanku sudah dibaca atau belum olehnya.

    Tidak,

    lebih tepatnya Aku terlalu takut untuk tahu apakah pesanku sudah dibacanya.

    Aku lebih memilih untuk menunggu di tempat yang sudah kupilih ini dan melihat sendiri apakah dia datang atau tidak.

    Tadinya Aku memilih menunggu karena tidak mau gelisah menunggu tanda “Read” di atas timestamp pesan yang kukirimkan padanya, 

    tetapi bodohnya Aku ketika mengira menunggu di sini seperti orang bodoh tidak lebih menegangkan dibanding menunggu sebuah pesan untuk dibaca.
    """

    with fade
    scene introduction_nana

    "{i}Ayo, Takiya! Dia sudah datang ke sini. Masa mau mundur?{/i}"

    t.c "Eh... kegiatanmu sudah selesai semua?"

    n.c """
    Sudah, kok.

    Aku malah tidak ada kegiatan apa-apa sepulang sekolah hari ini.
    """

    t.c "Aku tidak menganggu kan?"
    n.c "Tidak, kok. Ada apa?"
    t.c "A-aku mau bicara jujur. Boleh, ya?"
    n.c "Eh? Boleh."
    
    scene belakang_sekolah_sore
    with dissolve

    t.c "{i}Ini dia...{/i}"
    python:
            renpy.choice_for_skipping()
    show nana_biasa

    t.c """
    Nana, Aku… Aku sudah lama menyukaimu.

    Maukah kau menjadi pacarku?
    """
    
    show nana_tutup_mata
    hide nana_biasa

    n.c """
    Taki... Aku benar-benar senang.

    Aku benar-benar menghargai perasaanmu kepadaku
    
    tetapi Aku belum berencana untuk menjalin hubungan dengan siapapun.
    
    Maaf, Aku tidak bisa menjadi pacarmu...
    
    tapi... kita masih bisa jadi sahabat, kan?
    """

    hide nana_tutup_mata
    with dissolve

    "{i}Hah? Aku baru saja ditolak, kan?{/i}"

    show nana_biasa
    with dissolve
    
    n.c "Taki?"

    # These display lines of dialogue.

    # This ends the game.

    return

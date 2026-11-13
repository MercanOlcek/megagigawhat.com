def aktarim_suresi(veri_tb, internet_mbit):

    veri_bit = veri_tb * 1024**4 * 8
    toplam_saniye = veri_bit / (internet_mbit * 1_000_000)

    gun = int(toplam_saniye // 86400)
    saat = int((toplam_saniye % 86400) // 3600)
    dakika = int((toplam_saniye % 3600) // 60)
    saniye = int(toplam_saniye % 60)

    return gun, saat, dakika, saniye

# string_utils.py

def is_harf(char):
    """Kendisine gönderilen karakterin bir harf olup olmadığını kontrol eder."""
    return char.isalpha()

def kucukharf(harf):
    """Kendisine gelen büyük harfi küçük harfe çevirir. Büyük harf değilse olduğu gibi döndürür."""
    return harf.lower() if harf.isupper() else harf

def harfyuzdesi(text):
    """Metindeki harflerin kullanım sıklığını (yüzdelik oranını) hesaplar."""
    harf = [char.lower() for char in text if char.isalpha()]
    total_harf = len(harf)
    frequency = {}
    for harf in harf:
        frequency[harf] = frequency.get(harf, 0) + 1
    for harf, count in frequency.items():
        frequency[harf] = (count / total_harf) * 100
    return frequency

def bilgiler():
    """Kişisel bilgiler ve notu ekrana yazdırır."""
    print("Ad: ibrahim")
    print("Soyad: Akbaba")
    print("Öğrenci Numarası: 211213029")
    print("Not: Her şey göründüğü gibi olsaydı deniz suyu da mavi olurdu...")

if __name__ == "__main__":
    bilgiler()


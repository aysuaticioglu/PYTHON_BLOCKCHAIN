# hashlib modülünü ekliyoruz
import hashlib

# Zaman ve tarih bilgileri modülünü ekliyoruz
from datetime import datetime

# Block adında bir sınıfı oluşturuyoruz.
class ornekblokzinciri:

# Block sınıfına ait işlemlerin yapılacağı ana yönteme ait parametreler
  def __init__(self, sira, zaman, bilgi, onceki_hash):
# block oluştururken gereken sıra bilgisi
    self.sira = sira
# block a ait zaman 
    self.zaman= zaman
# block a ait bilgi
    self.bilgi = bilgi
# block oluştutururken gereken önceki hash parametresi
    self.onceki_hash = onceki_hash
# karıştırılan bilgilerin ataması
    self.hash = self.karistir_hashle()

#Block sınıfına ait dönüş bilgilerinin bulundupu string değer
  def __str__(self):
# dönüş bilgisi formatı
    return '{}. blok'.format(self.sira)

# Block sınıfına gönderilen değerlerin karıştırılması için özel fonksiyon
  def karistir_hashle(self):
# hashlib altında bulunan sha256 ile karıştırma algoritması kullanılacak
    sha = hashlib.sha256()
# gönderilen değerler bir dizi haline getiriliyor
    dizi = (str(x) for x in (self.sira, self.zaman, self.bilgi, self.onceki_hash))
# tüm değerler join ile birleştiriliyor
    sha.update(''.join(dizi).encode('utf-8'))

# karıştırılan değerler HEX stringleri haline getiriliyor ve cevap olarak gönderiliyor.
    return sha.hexdigest()

# Block un çalışmaıs için gerekli ilk işlem
def ilk_block():
  block = ornekblokzinciri(sira=0,
    zaman=datetime.now(),
    bilgi="İlk Block",
    onceki_hash="0")
  return block

#yeni block oluşturmak için özel fonksiyon. Önceki block ve karıştırılacak bilgi parametreleri gerekli
def yeni_block_olustur(onceki_block, bilgi=''):
# yeni block için sırayı 1 artırıyoruz
  sira_artir = onceki_block.sira + 1
# yeni block için Block sınıfına değerler gönderiliyor.
  yeni_block = ornekblokzinciri(
    sira=sira_artir,
    zaman=datetime.now(),
    bilgi='{}{}'.format(bilgi, sira_artir),
    onceki_hash=onceki_block.hash)
  return yeni_block

#uygulamanın çalıştırılması için fonksiyonumuz.
def test_et():
# zincir adında bir liste oluştururouz ve ilk block u çağırıyoruz
  zincir = [ilk_block()]
# zincirde var olan tek ve ilk block u onceki_block olarak tanımlıyoruz
  onceki_block = zincir[0]

#üretilecek block sayısını belirtiyoruz ve döngüye başlıyoruz
  for _ in range(0, 5):
# yeni block oluşturmak için fonksiyona gerekli parametreleri gönderiyoruz.
    yeni_block = yeni_block_olustur(onceki_block, bilgi='NEYI KARIŞIRACAK!')
#oluşturlan yeni block u zincir listesine ekliyoruz
    zincir.append(yeni_block)
# yeni block üretmek için oluşturulan yeni block u onceki_block olarak tanımlayıp sırayla devam ediyoruz.
    onceki_block = yeni_block
    print('{} zincire eklendi!'.format(yeni_block))
    print('Hash: {}\n'.format(yeni_block.hash))

test_et()

"""
def parametler
_init_ Python'da bir nesne çağırdığınızda 
otomatik olarak çalışacak ve sadece nesneyi ilk oluşturduğunuzda çalışacak olan bir fonksiyondur.
Dışarıdan ulaşılmasını istediğimiz her fonksiyona self parametresini ekleyerek ulaşıyoruz. 
SHA-256:SHA (Secure Hash Algorithm / Güvenli Hash Algoritması); 
ABD Ulusal Güvenlik Ajansı (National Security Agency / NSA) tarafından geliştirilen hash algoritmaları serisinin adıdır.
SHA-256 standardı; girdi verisi bir harften de ibaret olsa, 
yüzlerce sayfalık roman uzunluğunda da olsa daima on altılık sayı sisteminde 64 karakterlik çıktı sunar.
"""


 
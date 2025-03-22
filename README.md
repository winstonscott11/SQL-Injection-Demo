# SQL-Injection-Demo

Bu depo, SQL Injection güvenlik açığını gösteren basit bir web uygulaması içerir. Eğitimsel amaçlarla hazırlanmış olup, güvenlik zafiyetlerini ve bu zafiyetlerin nasıl düzeltilebileceğini göstermek için tasarlanmıştır.

## Proje Bileşenleri

1. **Vulnerable_simple.py**: SQL Injection zafiyeti içeren uygulama
2. **Fixed_svul.py**: SQL Injection zafiyeti düzeltilmiş uygulama
3. **Db_setup_simple.py**: Veritabanı kurulum betiği
4. **HTML şablonları**: Login ve dashboard sayfalarının şablonları

## Zafiyet Açıklaması

### OWASP Kategorisi
Bu uygulama, OWASP Top 10 listesinde yer alan "A03:2021 – Injection" kategorisine giren bir SQL Injection zafiyeti içermektedir.

### Zafiyet Vektörü Dizisi (CVSS v3.1)
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H (CVSS Skoru: 9.8 - Kritik)

- **AV (Attack Vector)**: Network - Saldırgan uzaktan erişim sağlayabilir
- **AC (Attack Complexity)**: Low - Saldırı karmaşık değil, basit SQL komutları yeterli
- **PR (Privileges Required)**: None - Saldırı için kimlik doğrulama gerekmez
- **UI (User Interaction)**: None - Kullanıcı etkileşimi gerektirmez
- **S (Scope)**: Unchanged - Etki alanı değişmez
- **C (Confidentiality)**: High - Tüm veritabanı içeriğine erişim sağlanabilir
- **I (Integrity)**: High - Veri bütünlüğü tamamen tehlikeye girebilir
- **A (Availability)**: High - Sistemin kullanılabilirliği etkilenebilir

## Nasıl Çalıştırılır

1. Veritabanı kurulumu: `python db_setup_simple.py`
2. Zafiyetli uygulamayı çalıştırma: `python vulnerable_simple.py`
3. Düzeltilmiş uygulamayı çalıştırma: `python fixed_svul.py`

## Zafiyet Gösterimi

1. Zafiyetli uygulamayı çalıştırın
2. Kullanıcı adı alanına `admin' --` girin
3. Şifre alanına herhangi bir şey yazabilirsiniz
4. Bu SQL injection sayesinde admin hesabına şifre olmadan erişim sağlanabilir

## Zafiyet Düzeltme Yöntemi

Güvenli kod örneğinde, SQL injection zafiyeti parametre bağlama (parameterized queries) yöntemi kullanılarak düzeltilmiştir. Bu yöntem, kullanıcı girdisini SQL sorgusundan ayırır ve saldırganların kodu manipüle etmesini engeller.




https://github.com/user-attachments/assets/81cc690e-648d-4f39-86e7-fa469431fbfa




```python
# Güvensiz kod (Vulnerable)
query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"

# Güvenli kod (Fixed)
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))










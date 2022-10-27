from requests import get
with open('zh_cn.json', 'w', encoding='utf8') as file:
    file.write(get('https://raw.githubusercontent.com/DM-Earth/Cabricality/packwiz/1.18.2/quilt/dev/config/openloader/resources/cabf-assets/assets/cabricality/lang/zh_cn.json').text)
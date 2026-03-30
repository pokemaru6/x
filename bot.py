import requests

def get_site(url):
    response = requests.get(url)
    print(f"--- {url} の中身を取得しました ---")
    print(response.text[:500]) # 最初の500文字だけ表示

# ここに見たいサイトのURLを入れる
get_site("https://www.google.com")


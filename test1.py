import requests
from bs4 import BeautifulSoup

# ウェブページのURLを指定
url = "https://aws.amazon.com/jp/events/?events-japan-cards-feature.sort-by=item.additionalFields.sortDateTime&events-japan-cards-feature.sort-order=asc&events-japan-cards.sort-by=item.additionalFields.sortDateTime&events-japan-cards.sort-order=asc&awsf.event-type=*all&awsf.event-category=*all&events-japan-cards2.sort-by=item.additionalFields.sortDateTime&events-japan-cards2.sort-order=asc"

# HTTPリクエストを送信してウェブページのHTMLを取得
response = requests.get(url)

# レスポンスコードの確認
if response.status_code == 200:
    # ページのHTMLをBeautiful Soupで解析
    soup = BeautifulSoup(response.text, 'html.parser')

    print("抽出開始")

    # print(soup.prettify())

    # ファイルに出力
    f = open('soup.txt', mode='w', encoding='utf-8_sig')
    f.write(soup.prettify())
    f.close()

    # イベント情報を含む要素を抽出
    event_elements = soup.find_all("h2")  # イベント情報を含む要素のクラスに注意

    for event_element in event_elements:

        # print(event_element)

        print("抽出中")
        # イベントのタイトルを取得
        # title_element = event_element.find("h4")
        # title = title_element.text.strip()

        # イベントの日付を取得
        # date_element = event_element.find("div", class_="event-date")
        # date = date_element.text.strip()

        # イベントの場所を取得
        # location_element = event_element.find("div", class_="event-location")
        # location = location_element.text.strip()

        # イベント情報を出力
        # print("タイトル:", title)
        # print("日付:", date)
        # print("場所:", location)
        # print("-" * 30)

else:
    print("HTTPリクエストが失敗しました。ステータスコード:", response.status_code)

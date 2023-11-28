import openai
import gpt-researcher
import gspread
import logging
import os 
import time
import asyncio
''' 以下スプレッドシート取得,Googledrive書き込み,その他に必要なライブラリ(スプレッドシートは認証情報ではなくAPI)
'''
# OpenAI API
openai_api_key = os.getenv(OPENAI_API_KEY)
# Google APIを環境変数から取得(書き足す)

# リサーチ用の関数
async def get_report(query: str, report_type: str) -> str:
    researcher = GPTResearcher(query, report_type)
    report = await researcher.run()
    return report


async def main():
    try:
        # スプレッドシートのIDとAPIキー
        spreadsheet_id = 'your_spreadsheet_id'
        api_key = 'your_api_key'

        # Google Sheets APIを使ってデータを取得するURL
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/A:A?key={api_key}"

        # APIリクエストを送信してデータを取得
        response = requests.get(url)
        data = response.json()

        # A列のデータを取得
        queries = data['values']

        # 各クエリに対してレポートを作成
        for query in queries:
            report = await get_report(query[0], "research_report")
            # この部分の処理を明日追加
            print(report)

            # レート制限のために10秒待機
            time.sleep(10)

    except Exception as e:
        # エラーのログを記録
        print(f"An error occurred: {e}")

# main関数を実行
asyncio.run(main())
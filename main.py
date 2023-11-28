import openai
import gpt-researcher
import gspread
import logging
import os
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


async def main()
    # スプレッドシートからリサーチしたい内容を取得
    
    query = "クエリ内容を1個づつここに追加"
    report_type = "research_report"

    report = asyncio.run(get_report(query, report_type))
    print(report)

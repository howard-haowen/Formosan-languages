import streamlit as st
import pandas as pd

def main():
  st.title("台灣南島語-華語句庫資料集")
  st.subheader("Dataset of Formosan-Mandarin sentence pairs")
  st.markdown(
        """
![visitors](https://visitor-badge.glitch.me/badge?page_id=howard-haowen.Formosan-languages)

### 原始碼
[GitHub頁面](https://github.com/howard-haowen/Formosan-languages)

### 資料集
- 🎢 資料集合計`139102`筆句對
- ‼️ 此查詢系統僅供教學與研究之用，內容版權歸原始資料提供者所有

### 資料來源
- 🥅 九階教材: [族語E樂園](http://web.klokah.tw)
- 💬 生活會話: [族語E樂園](http://web.klokah.tw)
- 🧗 句型: [族語E樂園](http://web.klokah.tw)
- 🔭 文法: [臺灣南島語言叢書](https://alilin.apc.gov.tw/tw/)
   + 以上來源的資料是透過網路爬蟲取得。
- 📚 詞典: [原住民族語言線上詞典](https://e-dictionary.apc.gov.tw/Index.htm?fbclid=IwAR18XBJPj2xs7nhpPlIUZ-P3joQRGXx22rbVcUvp14ysQu6SdrWYvo7gWCc)
   + 詞典資料是透過`PDFMiner` 將2019版的PDF檔轉成HTML，再用`BeautifulSoup`抓取句對，偶爾會出現族語跟華語對不上的情形。若發現錯誤，請[聯絡我📩](https://github.com/howard-haowen)。詞典中重複出現的句子已從資料集中刪除。

### 使用方法
- 🔭 過濾：選擇來源與語言
- 📚 排序：點選首欄
- 🥅 放大：點選表格右上角進入全螢幕模式
- 💬 更多：句子太長時，將滑鼠移到句子上方即可檢視完整內容
"""
)
  
  df = get_data()
  pd.set_option('max_colwidth', 600)
  sources = st.radio(
        "請選擇來源",
        options=['詞典', '文法', '句型', '生活會話', '九階教材'],
        )
  langs = st.radio(
        "請選擇語言",
        options=['撒奇萊雅','阿美','噶瑪蘭','魯凱','排灣','卑南',
                 '賽德克','邵','拉阿魯哇','達悟','泰雅','太魯閣',
                 '鄒','卡那卡那富','賽夏','布農'],
                 )
  
  # select a source
  if sources == "詞典":
    s_filt = df['From'] == "詞典"
  elif sources == "文法":
    s_filt = df['From'] == "文法"
  elif sources == "句型":
    s_filt = df['From'] == "句型"
  elif sources == "生活會話":
    s_filt = df['From'] == "生活會話"
  elif sources == "九階教材":
    s_filt = df['From'] == "九階教材"
  
  # select a language 
  if langs == "噶瑪蘭":
    l_filt = df['Lang_En'] == "Kavalan"
  elif langs == "阿美":
    l_filt = df['Lang_En'] == "Amis"
  elif langs == "撒奇萊雅":
    l_filt = df['Lang_En'] == "Sakizaya"
  elif langs == "魯凱":
    l_filt = df['Lang_En'] == "Rukai"
  elif langs == "排灣":
    l_filt = df['Lang_En'] == "Paiwan"
  elif langs == "卑南":
    l_filt = df['Lang_En'] == "Puyuma"
  elif langs == "賽德克":
    l_filt = df['Lang_En'] == "Seediq"
  elif langs == "邵":
    l_filt = df['Lang_En'] == "Thao"
  elif langs == "拉阿魯哇":
    l_filt = df['Lang_En'] == "Saaroa"
  elif langs == "達悟":
    l_filt = df['Lang_En'] == "Yami"
  elif langs == "泰雅":
    l_filt = df['Lang_En'] == "Atayal"
  elif langs == "太魯閣":
    l_filt = df['Lang_En'] == "Truku"
  elif langs == "鄒":
    l_filt = df['Lang_En'] == "Tsou"
  elif langs == "卡那卡那富":
    l_filt = df['Lang_En'] == "Kanakanavu"
  elif langs == "賽夏":
    l_filt = df['Lang_En'] == "Saisiyat"
  elif langs == "布農":
    l_filt = df['Lang_En'] == "Bunun"

  filt_df = df[(s_filt) & (l_filt)]
  zh_columns = {'Lang_Ch': '語言_方言', 'Ab': '族語', 'Ch': '華語', 'From': '來源'}
  filt_df.rename(columns=zh_columns, inplace=True)
  st.dataframe(filt_df)

@st.cache
def get_data():
  df = pd.read_pickle('Formosan-Mandarin_sent_pairs_updated.pkl')
  del df['Num']
  clean_df = df.astype('str')
  clean_df = clean_df.apply(strip)  
  return clean_df

if __name__ == '__main__':
  main()

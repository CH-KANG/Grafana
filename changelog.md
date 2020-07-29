# Grafana 更新日誌
## 2020/03/16
**time range**
>發現問題，雖然使用local browser time可以使用正確的linux time
但根據Mysql手冊，From mysql manual " MySQL converts TIMESTAMP values from the current time zone to UTC for storage, and back from UTC to the current time zone for retrieval.
Bookroll資料庫的時間格式是datetime 所以會有這個問題
>20200724




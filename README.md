# Grafana 安裝教學
**一. 預先安裝
請確認Bookroll、Mysql是否已經安裝**

系統名稱       | 系統類型           | 
--------------|:-----------------:|
Moodle        | 帳號單一登入系統   |  
Bookroll      | 電子書平台        |  
MySQL         | Bookroll資料庫    | 


**二. 系統流程圖**
![image](https://github.com/CH-KANG/Grafana/blob/master/Pic/flow_chart.png)


**三. 安裝前需求**
* 系統為Linux / Windows皆可

* Python3
  * Ubuntu已有內建
  * Windows可下載  
  
    https://www.python.org/downloads/
  * 需求套件 : lti, oauthlib, flask
   ```python
   pip install lti
   pip install oauthlib
   pip install flask
   ```
* MySQL   
  * 安裝Bookroll時即安裝
  
* Grafana
  * 可選擇Linux, Windows, Mac, Docker等安裝方式與系統
  * 請參考官方文件  
  
    https://grafana.com/grafana/download?platform=linux
    

**四. Grafana配置**
* Step1. 啟動Grafana
  * 請參考官方文件  
  
    https://grafana.com/docs/grafana/latest/installation/debian/
  * 以Linux為例
   ```
   sudo service grafana-server start
   ```
  * 以Windows為例   
   ```
   cd '\Program Files\GrafanaLabs\grafana\bin'
   grafana-server.exe
   ```  
* Step2.用vim或其他編輯器開啟訪客模式(auth.anoymous)
  * These system settings are defined in or custom.ini
  
    以Linux為例，路徑為 /etc/grafana/grafana.ini
    
    開啟後需要restart
   ```
   sudo service grafana-server restart
   ```    
    ![image](https://github.com/CH-KANG/Grafana/blob/master/Pic/auth.anony.png)
    
* Step3.連接資料庫
  * 點選 Configuration    
  
  ![image](https://github.com/CH-KANG/Grafana/blob/master/Pic/Configuration.PNG)
  * 點選 Add data source
  
  ![image](https://github.com/CH-KANG/Grafana/blob/master/Pic/Add%20data%20source.PNG)
  * 點選 SQL - MySQL
  
  ![image](https://github.com/CH-KANG/Grafana/blob/master/Pic/SQL.PNG)
  
  * 填入Bookroll的MySQL ip 與 port
  
* Step4.匯入Panel面板
  * 先下載以下兩個Dashboard的模板(json檔案)
  * Analysis tool (Dashboard) 
  
    請下載或Clone
    
    https://github.com/CH-KANG/Grafana/blob/master/Analysis%20tool%20(Dashboard)-1583397153634.json
    
  * Weekly report (Dashboard) 
  
    請下載或Clone
    
    https://github.com/CH-KANG/Grafana/blob/master/Weekly%20Report-1583397606381.json

  * 點選 + → Create → import
  
  ![image](https://github.com/CH-KANG/Grafana/blob/master/Pic/import.png)
  * 分別匯入上述兩個模板
  
  ![image](https://github.com/CH-KANG/Grafana/blob/master/Pic/importjson.PNG)
  
  * 匯入完成後開啟，選擇share dashborad，並記錄下此串網址 註1*
  
  ![image](https://github.com/CH-KANG/Grafana/blob/master/Pic/link.PNG)
  
**五. Python檔案配置**
* 下載Python檔案
  * 請下載以下兩個python檔案，分別對應Analysis tool (Dashboard) 與 Weekly report (Dashboard)
  * Analysis tool (Dashboard) 
  
    請下載或Clone
    
    https://github.com/CH-KANG/Grafana/blob/master/flask_provider_Analysis_tool.py
    
  * Weekly report (Dashboard) 
  
    請下載或Clone
    
    https://github.com/CH-KANG/Grafana/blob/master/flask_provider_grafana_weekly_report.py
* 修改Python檔    
  * 打開python檔案，修改兩個python檔案(以Analysis tool為例)
  
    請修改以下部分

   ```python
   key = '12345678-8137-2FF2-ABCD'  #請修改成自訂的密碼(16進位)，並符合長度 (客戶密鑰) 註2*
   the_secret = 'sd54f65sd65f6sde'  #請修改成自訂的密碼，並符合長度 (共享的密鑰)
   ```  

   ```python
   def test():
                 ...
       return redirect('.......&var-flask_test=' + temp+'&refresh=1m') 
       #請將註1* 的網址複製到 '.......&var-flask_test=' 取代內容
       #並將&var-flask_test=之後的字元都去除
   ```  

   ```python
   if __name__=="__main__":
       app.debug = True
       app.run(host="0.0.0.0", port=8090) #可更改port號碼 並請記住port號碼 註3*
   ```  
* 執行Python檔
  * 修改完成後請背景執行兩個檔案並且不中斷
    
    以Linux為例，參考指令
   ```
   nohup python3 flask_provider_Analysis_tool.py 0<&- &> analysis_tool.log &
   nohup python3 flask_provider_grafana_weekly_report.py 0<&- &> grafana_weekly_report.log &
   ```     

**六. Moodle LTI連結**
* Step1. 請利用admin帳號進入moodle，依照下列步驟註冊LTI
  * Analysis tool (Dashboard) 與 Weekly report (Dashboard)都需要註冊，在這裡以Analysis tool為例
  * 點選網站管理
  
  ![image](https://github.com/CH-KANG/Grafana/blob/master/Pic/lti01.png)

  * 點選管理工具
  
  ![image](https://github.com/CH-KANG/Grafana/blob/master/Pic/lti02.png)
  
  * 點選手動配置一個工具
  
  ![image](https://github.com/CH-KANG/Grafana/blob/master/Pic/lti03.png)  
  
  * 輸入工具名稱 / 設定的python檔案網址(註3*) /  客戶密鑰, 共享的密鑰(註2*) / 預設啟動容器選擇 新視窗
  
  ![image](https://github.com/CH-KANG/Grafana/blob/master/Pic/lti04.png)
  
* Step2. 最後新增工具即可完成!
  * 啟動編輯模式
  
  ![image](https://github.com/CH-KANG/Grafana/blob/master/Pic/lti05.png)

  * 新增活動或資源
  
  ![image](https://github.com/CH-KANG/Grafana/blob/master/Pic/lti06.png)
  
  * 點選外部工具
  
  ![image](https://github.com/CH-KANG/Grafana/blob/master/Pic/lti07.png)  
  
  * 選擇Step1註冊的工具，完成!
  
  ![image](https://github.com/CH-KANG/Grafana/blob/master/Pic/lti08.png)   

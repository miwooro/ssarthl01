版本：<p>
Python 3.6.0<br/>
Django==1.10.5<p>

ssarthl01勤務管理系統<p>
<p>
功能：<p>
<p>
1.人事<p>
可以新增人員、刪除人員以及選擇是否搭伙<br/>
<p>
2.輪休表<p>
設定年份、月份並上傳輪休表docx檔案<br/>
上傳後系統會依照docx檔案自行判讀，各個人員休假日期、天數<br/>
再以表格輸出結果<br/>
並同時計算各個人員當月需繳餐費金額、製作當月餐費表格<br/>
注意：<br/>
輪休表製作完畢會自行製作餐費表格<br/>
刪除當月輪休表也會一併刪除當月餐費表格<br/>
<p>
3.餐費表格<p>
無法自行製作表格，也無法自行刪除<br/>
當月餐費表格於當月輪休製作時也會自動製作（也會自行帶入目前駐地所有人員，但若在新增人員時選擇不搭伙，該人員就不會被列入表格之中），而刪除當月輪休表時，也會一併刪除當月餐費表格<br/>
隊員餐費一天以80元計算，不需手動輸入上班天數，在輪休表點選休假日期會自動計算上班天數，並且同時更新該隊員當月應繳交之費用（上班天數 * 80）<br/>
替代役餐費一天以110元計算，但替代役餐費固定為1600元，每月上班以20天計算（替代役不以實際上班天數來計算，故不與輪休表之上班天數連動）<br/>
收款為替代役勤務，故收款人選項只會列出替代役<br/>
備註欄可以輸入是否需要找錢<br/>
若有新進人員搭伙天數不足一個月，無法以公式計算，可以使用特殊餐費來計算<br/>
輸入人員及金額即可新增金額<br/>
<p>
4.訓練業務<p>
選擇訓練項目、日期、照片送出後會自行生成訓練成果表格<br/>
當訓練表格數量超過5時，會自行刪除日期最早的表格<br/>

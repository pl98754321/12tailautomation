import requests
import time
line_access_token = "TQDIO3EHCJbj8U1JlFuM00ztpiTnjfwjAkUsdFayUqL"

url = "https://notify-api.line.me/api/notify"
header_raw = {
    "Authorization": f"Bearer {line_access_token}"
}
massage_raw = "test 1 "

print("ยังส่งไม่เรียบร้อย")
requests.post(url,headers= header_raw,data={"massage":massage_raw,"stickerId":2})
print("ส่งเรียบร้อย")
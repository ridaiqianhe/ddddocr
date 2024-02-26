# ddddocr
使用方法:

git clone https://github.com/ridaiqianhe/ddddocr.git
cd ddddocr
docker build -t ocr_server:v1 .
docker run -p 9898:9898 -d --name  ocr --restart=always ocr_server:v1

rm -r ddddocr
docker stop ocr && docker rm ocr
docker rmi ocr_server:v1

module 'pil.image' has no attribute 'antialias' 处理方法: pip install ddddocr==9.5.0

验证方法：
def verfiyCode(img):    
    data = {"img": img}
    try:
        posturl =  f"http://198.12.65.170:9898/ocr"
        try:
            result = requests.post(posturl,data = data,timeout = 10).json()
        except Exception as e:
            result = {"code":-1,"msg":f"错误 {e}"}
        print(result)
        if result.get("code") == 0:
            coderesult  = result["result"]
            print("识别成功  " , coderesult)
        else:
            print("识别失败")
            return None
    except Exception as e:
        print(e)
        time.sleep(10)
        return None
    return coderesult

b = '/9j/4AAQSkZJRgABAgAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAoAHsDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+iiigAoqjqd+bGNNiBncnGegx1/nVW6n1GwQTSSwyKx27NvCnk8dD0FUotmE68Ytrtv5GxVO41awtc+bdxghtpVTuIPuByKS9hbUdJeOCQxtMgKk/ng49en41nW/hSyjjImkklcqRkHaAfUD1+pIqQqSqXtTXzZr2t7bXse+2mWQDrjqPqOo6VPXE+Ht0fiAJA5kiw6s4XGU7H25C12NxcxWybpWxnoB1NBNHEKdPnnpYlorP/tm3/uS/kP8avowdFdTlWGQfam00aU69Op8DuJJJHEu6R1QZxljikjmilz5ciPjrtYHFQ3dlFeKokLAqeCprF1Kzgs2RI3cuRkhvT600kznxOIq0Ly5U4rz1OjoqhpELw2I34+dt4+hAq/Us6aU3OCk1a4UUUUGgUUUUAZmtmNbIM0Su27apJ+7kHn9KpXVtImmwXLXTyH5WKSnIJPTAP8AnrW5PBFcx+XMgZc5xVZdJsVYEQDIOeWJ/rWkZJI462HlOTatqv69Se1mNxaxyspUsuSCMf5Fc74k1jrY2svqJyv/AKDn+f5eorp1UKoVQAAMADtWRP4bsJ7x7hzNl33sgb5Se/bPP1qC68KsqfLB69TE0nUbDSIXch57mVM/KuFT/ZyefqRx064rc1e3kZxOADGqgE56c/8A16sw6Pp0CFUs4SCc/Ou8/mc03V45ZLdSgyiHLDv9f504vU5q1CUcNKMtbbWKV5ew3UMUaR+WVPJI4Uegx2/wrVskVLOJUYMMZyPXvWW12k1glrHAxkGOgz07j/Pc1oaZBJBaYkGCzbsdwMDrVS2IwknKvzfFdb2tbyLE8yW8LSyZ2qOcVhWELahfPNNyqnc3cE9hz2/wrYu7KO8VVkdwFOcKetSW1vHawiKPOAc5PU/WpTsjetQnWrR5vgX4sxPsnib/AKCNt/3yP/iKPtfib/oHW3/fQ/8Ai66CipOn2fZs5/8AtvVYP3c+iSvKOrRE7T9MA/zo/wCEg1D/AKANz/49/wDE10FFAckv5vyCiiig1CiiigAooooAKKKKACiiigAooooAKKKKACiiigD/2Q=='
verfiyCode(b)

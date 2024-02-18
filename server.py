#-*- coding:utf-8 -*-
from flask import Flask
from flask import request as req
from ocr import ocr,slide
#设置端口
port = 9898
rightkey = '****任意填写****'
#—————————————为flask基础配置——————————————————————————
class Config(object):
    DEBUG=True
    JSON_AS_ASCII=False
    SECRET_KEY = '1933ef4c9d9ea88c51e5b38a8e2ae222f422e27b6982bea9eee748e5922fe08d'
app = Flask(__name__)
app.config.from_object(Config)
@app.route('/ocr',methods=['GET','POST'], strict_slashes=False)
def ocrfun():
    try:
        img = req.values["img"]
        if req.values.get("old"):
            return ocr(img,True)
        return ocr(img)
    except Exception as e:
        return {"code":-1,"msg":str(e)}
#—————————————为api辅助参数______________
@app.route('/slide',methods=['GET','POST'], strict_slashes=False)
def slidefun():
    try:
        img,img1 = req.values["img"],req.values["img1"]
        return slide(img,img1)
    except Exception as e:
        return {"code":-1,"msg":str(e)}
    
 
@app.route('/ping', methods=['GET'])
def ping():
    return "pong"

@app.errorhandler(404)
def page_not_found(_):
    return "欢迎使用ocr识别系统"
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)

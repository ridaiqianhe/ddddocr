import ddddocr,base64
def ocr(imgb64,old = False):
    if not imgb64:return {"code":-1,"msg":"img值未传送"}
    ocr = ddddocr.DdddOcr()
    try:
        image = base64.b64decode(imgb64)
        res = ocr.classification(image)
        return {"code":0,"msg":"识别成功","result":res}
    except Exception as e:
        return {"code":-1,"msg":f"识别失败,原因:{str(e)}"}
def slide(target_bytesb64,background_bytesb64):
    try:
        det = ddddocr.DdddOcr(det=False, ocr=False)
        target_bytes,background_bytes = base64.b64decode(target_bytesb64),base64.b64decode(background_bytesb64)
        res = det.slide_match(target_bytes, background_bytes)
    except Exception as e:
        return {"code":-1,"msg":f"识别失败,原因:{str(e)}"}
    return {"code":0,"msg":"识别成功","result":res}
def detection(background_bytes):
    try:
        det = ddddocr.DdddOcr(det=False, ocr=False)
        res = det.detection( background_bytes)
    except Exception as e:
        return {"code":-1,"msg":f"识别失败,原因:{str(e)}"}
    return {"code":0,"msg":"识别成功","result":res}
 

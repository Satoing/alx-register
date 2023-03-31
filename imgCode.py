import ddddocr

def get_code():
    ocr = ddddocr.DdddOcr()
    with open('./img/tmp.jpg', 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    return res

if __name__ == "__main__":
    print(get_code())

from time import sleep

class TextDisplayer:
    def __init__(self):
        pass

    # n秒おきにテキストを表示する
    def printI(self, text: str, interval: float):
        texts = list(text)
        for text in texts:
            print(text, flush=True, end="")
            sleep(interval)
        
    # n秒間かけてテキストを表示する
    def printD(self, text: str, duration: float):
        texts = list(text)
        interval = duration / len(texts)
        for text in texts:
            print(text, flush=True, end="")
            sleep(interval)
    
    # 行ごとにn秒おきにテキストを表示する
    def printIL(self, text: str, interval: float):
        lines = text.strip().split("\n")
        for line in lines:
            print(line)
            sleep(interval)

    # 行ごとにn秒間かけてテキストを表示する
    def printDL(self, text: str, duration: float):
        lines = text.strip().split("\n")
        interval = duration / len(lines)
        for line in lines:
            print(line)
            sleep(interval)

    # n秒おきにテキストを表示後,入力させる
    def inputI(self, text: str, interval: float):
        texts = list(text)
        for text in texts:
            print(text, flush=True, end="")
            sleep(interval)
        input_content = input("")
        return input_content

    # n秒間かけてテキストを表示後,入力させる
    def inputD(self, text: str, duration: float):
        texts = list(text)
        interval = duration / len(texts)
        for text in texts:
            print(text, flush=True, end="")
            sleep(interval)
        input_content = input("")
        return input_content

    # n秒おきにテキストを表示する.表示前にランダムな文字を出す.(日本語は使えない)
    def printScrambleI(self, text: str, interval: float):
        texts = list(text)
        for i in range(len(texts)):
            parameter_text = " "
            try: 
                real_interval = interval / (ord(texts[i]) - ord(parameter_text))
            except ZeroDivisionError:
                real_interval = interval
            while parameter_text <= texts[i]:
                print(f"\033[0K\r{text[0:i]}{parameter_text}", flush=True, end="")
                parameter_text = chr(ord(parameter_text) + 1)
                sleep(real_interval)

    # n秒かけてテキストを表示する.表示前にランダムな文字を出す.(日本語は使えない)
    def printScrambleD(self, text: str, duration: float):
        texts = list(text)
        interval = duration / len(texts)
        for i in range(len(texts)):
            parameter_text = " "
            try:
                real_interval = interval / (ord(texts[i]) - ord(parameter_text))
            except ZeroDivisionError:
                real_interval = interval
            while parameter_text <= texts[i]:
                print(f"\033[0K\r{text[0:i]}{parameter_text}", flush=True, end="")
                parameter_text = chr(ord(parameter_text) + 1)
                sleep(real_interval)
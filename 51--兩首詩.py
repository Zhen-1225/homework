poem1=set("紅豆生南國，春來發幾枝。願君多采擷，此物最相思。")
poem2=set("春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。")
poem1.remove("，")
poem1.remove("。")
poem2.remove("，")
poem2.remove("。")
print(poem1 & poem2)
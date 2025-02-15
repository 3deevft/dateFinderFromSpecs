import arrr
from pyscript import document
global specsin
specsin = []
def Submit(event):
    if document.querySelector("#boy").checked:
        specsin.append("boy")
    if document.querySelector("#glasses").checked:
        specsin.append("glasses")
    if document.querySelector("#ng").checked:
        specsin.append("noglasses")
    if document.querySelector("#girl").checked:
        specsin.append("girl")
    if document.querySelector("#short").checked:
        specsin.append("short")  
    if document.querySelector("#avg").checked:
        specsin.append("avg")  
    if document.querySelector("#tall").checked:
        specsin.append("tall")  
    if document.querySelector("#music").checked:
        specsin.append("music")  
    if document.querySelector("#sports").checked:
        specsin.append("sports")  
    if document.querySelector("#nerd").checked:
        specsin.append("nerd")  
    if document.querySelector("#introvert").checked:
        specsin.append("introvert")  
    if document.querySelector("#friendly").checked:
        specsin.append("freindly")  
    if document.querySelector("#stirfeet").checked:
        specsin.append("stirfeet")  
    if document.querySelector("#shorthair").checked:
        specsin.append("shorthair")  
    if document.querySelector("#longhair").checked:
        specsin.append("longhair")  
    if document.querySelector("#rich").checked:
        specsin.append("rich")  
    if document.querySelector("#braces").checked:
        specsin.append("braces")  

    """ info={
        "boy" : document.querySelector("#boy").checked,
        "girl" : document.querySelector("#girl").checked,
        "glasses" : document.querySelector("#glasses").checked,
        "noglasses" : document.querySelector("#ng").checked,
        "short" : document.querySelector("#short").checked,
        "avg" : document.querySelector("#avg").checked,
        "tall" : document.querySelector("#tall").checked,
        "music" : document.querySelector("#music").checked,
        "sports" : document.querySelector("#sports").checked,
        "nerd" : document.querySelector("#nerd").checked,
        "introvert" : document.querySelector("#introvert").checked,
        "friendly" : document.querySelector("#friendly").checked,
        "stirfeet" : document.querySelector("#stirfeet").checked,
        "shorthair" : document.querySelector("#shorthair").checked,
        "longhair" : document.querySelector("#longhair").checked,
        "rich" : document.querySelector("#rich").checked,
        "braces" : document.querySelector("#braces").checked
    }
     """
    #for i in info.values():
     #   document.write(info.values)
       # if i == "true":
      #      specsin.append(info.get(i))
            
        ##   pass
    
    specs={
    "boy":["กฤตติ์ธามม์","กิตติพัศ","คีญ","เจณณวัฒน์","ชยุต","ญาณวุฒิ","ณพุทธ","ธนภัทร","ธีรวิษณุ์","บวรรัช","พงศภัค","พิชญภูมิ","ภทรธร","พาพัฒน์"],
    "girl":["ณญากร","ณภัทร","ณัชชา","ณัฐปภัสร์","ณิชณัชทฐ์","ปัญญาภรณ์","พิชชาภา","ภคมน","ภัทรพร ","เมืองพลอย","สิรภัทร","สิริลภัส","พาพัฒน์"],
    "noglasses":["กฤตติ์ธามม์","ชยุต","ญาณวุฒิ","ณพุทธ","พงศภัค","พาพัฒน์","ณญากร","ณิชณัชทฐ์","ปัญญาภรณ์","พิชชาภา","ภคมน","เมืองพลอย","สิรภัทร","สิริลภัส"],
    "glasses" : ["กิตติพัศ","คีญ","เจณณวัฒน์","ณภัทร","ณัชชา","ณัฐปภัสร์","ธนภัทร","ธีรวิษณุ์","บวรรัช","พิชญภูมิ","ภทรธร","ภัทรพร" ],
    "short" : ["กิตติพัศ","ธนภัทร","ธีรวิษณุ์","ภคมน","สิริลภัส"],
    "avg" : ["คีญ","เจณณวัฒน์","ชยุต","ณญากร","ณพุทธ","ณัฐปภัสร์","ณิชณัชทฐ์","บวรรัช","ปัญญาภรณ์","พิชชาภา","ภัทรพร ","เมืองพลอย"],
    "tall" : ["กฤตติ์ธามม์","ญาณวุฒิ","พงศภัค","ภทรธร","สิรภัทร","พาพัฒน์","พิชญภูมิ"],
    "sports" : ["กฤตติ์ธามม์","เจณณวัฒน์","ญาณวุฒิ","ธีรวิษณุ์","ปัญญาภรณ์","พงศภัค","พิชชาภา","พิชญภูมิ","ภคมน","เมืองพลอย","สิรภัทร","สิริลภัส","ณพุทธ","พาพัฒน์"],
    "nerd" : ["กิตติพัศ","คีญ","ณพุทธ"],
    "music" : ["ณิชณัชทฐ์","พิชญภูมิ","พาพัฒน์","สิริลภัส","คีญ","ณพุทธ"],
    "introvert" : ["ณญากร","บวรรัช","ภทรธร","สิรภัทร","กฤตติ์ธามม์"],
    "friendly" : ["ณัชชา","ณภัทร","ณัฐปภัสร์","ธีรวิษณุ์","ปัญญาภรณ์","พงศภัค","พิชญภูมิ","ภคมน","ภัทรพร ","สิรภัทร"],
    "stirfeet" : ["กิตติพัศ","ธนภัทร","ธีรวิษณุ์","พิชญภูมิ","ณพุทธ","ชยุต","พาพัฒน์"],
    "rich"  :["กฤตติ์ธามม์","ณพุทธ","ณิชณัชทฐ์","ปัญญาภรณ์"],
    "braces":["เจณณวัฒน์","ธีรวิษณุ์","พิชญภูมิ","ภคมน"],
    "shorthair":["กฤตติ์ธามม์","กิตติพัศ","คีญ","เจณณวัฒน์","ชยุต","ญาณวุฒิ","ณพุทธ","ธนภัทร","ธีรวิษณุ์","บวรรัช","พงศภัค","พิชญภูมิ","ภทรธร","พาพัฒน์"],
    "longhair":["ณญากร","ณภัทร","ณัชชา","ณัฐปภัสร์","ณิชณัชทฐ์","ปัญญาภรณ์","พิชชาภา","ภคมน","ภัทรพร ","เมืองพลอย","สิรภัทร","สิริลภัส"]
    }
    output = document.querySelector("#output")
    log = document.querySelector("#log")

    list=[]
    for i in specsin:
        list.append(specs.get(i))

   
    
    res = set(list[0]).intersection(*map(set, list[1:]))
    #res = set(list[0]).intersection(set(list[1]))
  

    print("จากสเปคแล้วคุณเหมาะกับ : "+" , ".join(res))
    
    
   
    output.innerText = "Your spec matches : "+" , ".join(res)
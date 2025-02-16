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
    if document.querySelector("#extrovert").checked:
        specsin.append("extrovert")  
    if document.querySelector("#ambivert").checked:
        specsin.append("ambivert")  
    if document.querySelector("#polite").checked:
        specsin.append("polite")  
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
    "boy":["กฤตติ์ธามม์","กิตติพัศ","คีญ","เจณณวัฒน์","ชยุต","ญาณวุฒิ","ณพุทธ","ธนภัทร","ธีรวิษณุ์","บวรรัช","พงศภัค","พิชญภูมิ","ภทรธร","พาพัฒน์"
,"ธนดล","ธนวัสส์","ธนากฤต","บารเมษฐ์","เป็นขลุ่ย","ปภังกร","พศิน","พาทิศ","พิชชากร","ภูมิพัฒน์","ภูริพงษ์","เมืองเอก","วิชศกร","อนุรุทธ์"],

    "girl":["ณญากร","ณภัทร","ณัชชา(พันช์)","ณัฐปภัสร์","ณิชณัชทฐ์","ปัญญาภรณ์","พิชชาภา","ภคมน","เมืองพลอย","สิรภัทร","สิริลภัส","พาพัฒน์"
,"จิรัชญา","ชนาภา","ญาดา","ณิชชา","ทิตชญา","ธรณ์ธันย์","นิยารินทร์","พิชชานันท์","อรภิชา","ศศิณัฎฐ์","สิรินทร์"],
    "noglasses":["กฤตติ์ธามม์","ชยุต","ญาณวุฒิ","ณพุทธ","พงศภัค","พาพัฒน์","ณญากร","ณิชณัชทฐ์","ปัญญาภรณ์","พิชชาภา","ภคมน","เมืองพลอย","สิรภัทร","สิริลภัส"
,"จิรัชญา","ชนาภา","ญาดา","ณิชชา","ธนดล","ธนวัสส์","ธนากฤต","ธรณ์ธันย์","นิยารินทร์","บารเมษฐ์","ปภังกร","พศิน","พาทิศ","พิชชากร","พิชชานันท์","ภูมิพัฒน์","ภูริพงษ์","วิชศกร","สิรินทร์","ศศิณัฎฐ์","อรภิชา"],

    "glasses" : ["กิตติพัศ","คีญ","เจณณวัฒน์","ณภัทร","ณัชชา(พันช์)","ณัฐปภัสร์","ธนภัทร","ธีรวิษณุ์","บวรรัช","พิชญภูมิ","ภทรธร","ภัทรพร",
"ทิตชญา","เป็นขลุ่ย","เมืองเอก","อนุรุทธ์"],
    "short" : ["กิตติพัศ","ธนภัทร","ธีรวิษณุ์","ภคมน","สิริลภัส",
"ธนดล","ธนากฤต","ธรณ์ธันย์","ภูริพงษ์","ภูมิพัฒน์"],
    "avg" : ["คีญ","เจณณวัฒน์","ชยุต","ณญากร","ณพุทธ","ณัฐปภัสร์","ณิชณัชทฐ์","บวรรัช","ปัญญาภรณ์","พิชชาภา","ภัทรพร ","เมืองพลอย"
,"จิรัชญา","ชนาภา","ญาดา","ณิชชา","ทิตชญา","ธนวัสส์","ธยาน์","นิยารินทร์","บารเมษฐ์","เป็นขลุ่ย","อรภิชา","สิรินทร์","พาทิศ","พิชชากร","พิชชานันท์,"วิชศกร"],
    "tall" : ["กฤตติ์ธามม์","ญาณวุฒิ","พงศภัค","ภทรธร","สิรภัทร","พาพัฒน์","พิชญภูมิ"
"ปภังกร","พศิน","อนุรุทธ์"],
    "sports" : ["กฤตติ์ธามม์","เจณณวัฒน์","ญาณวุฒิ","ธีรวิษณุ์","ปัญญาภรณ์","พงศภัค","พิชชาภา","พิชญภูมิ","ภคมน","เมืองพลอย","สิรภัทร","สิริลภัส","ณพุทธ","พาพัฒน์"
,"จิรัชญา","ชนาภา","ทิตชญา","ธนดล","ธนวัสส์","ธรณ์ธันย์","เป็นขลุ่ย","พาทิศ","พิชชากร","เมืองเอก","วิชศกร","อรภิชา","ศศิณัฎฐ์","อนุรุทธ์"],
    "nerd" : ["กิตติพัศ","คีญ","ณพุทธ"],
    "music" : ["ณิชณัชทฐ์","พิชญภูมิ","พาพัฒน์","สิริลภัส","คีญ","ณพุทธ"
,"ชนาภา","ธนากฤต","ธรณ์ธันย์"],
    "polite":["ณญากร","คีญ","ณัชชา","ณัฐปภัสร์"
,"สิรินทร์","พิชชานันท์"],
    "introvert" : ["ณญากร","บวรรัช","ภทรธร","สิรภัทร","ณิชณัชทฐ์"
,"ญาดา","ทิตชญา","นิยารินทร์","ธยาน์","พิชชานันท์"],
    "ambivert":["กฤตติ์ธามม์","กิตติพัศ","คีญ","เจณณวัฒน์","ชยุต","ญาณวุฒิ","ณพุทธ","ภัทรพร","ณัชชา","เมืองพลอย","พิชชาภา"
,"ธนดล","ธนวัสส์","ธนากฤต","ธรณ์ธันย์","ปภังกร","พศิน","พาทิศ","พิชชากร","ภูมิพัฒน์","ภูริพงษ์","เมืองเอก","วิชศกร","อรภิชา","สิรินทร์"],
    "extrovert" : ["ณภัทร","ณัฐปภัสร์","ธีรวิษณุ์","ปัญญาภรณ์","พงศภัค","พิชญภูมิ","ภคมน","ธนภัทร","พาพัฒน์"
,"จิรัชญา","ชนาภา","ณิชชา","บารเมษฐ์","เป็นขลุ่ย","อนุรุทธ์","ศศิณัฎฐ์"],
    "stirfeet" : ["กิตติพัศ","ธนภัทร","ธีรวิษณุ์","พิชญภูมิ","ณพุทธ","ชยุต","พาพัฒน์"
,"ธนากฤต","บารเมษฐ์","เป็นขลุ่ย","อนุรุทธ์","ศศิณัฎฐ์"],
    "rich"  :["กฤตติ์ธามม์","ณพุทธ","ณิชณัชทฐ์","ปัญญาภรณ์"
,"พิชชากร","ณิชชา","จิรัชญา"],
    "braces":["เจณณวัฒน์","ธีรวิษณุ์","พิชญภูมิ","ภคมน"
,"ธนดล","เป็นขลุ่ย","อนุรุทธ์","อรภิชา",],
    "shorthair":["กฤตติ์ธามม์","กิตติพัศ","คีญ","เจณณวัฒน์","ชยุต","ญาณวุฒิ","ณพุทธ","ธนภัทร","ธีรวิษณุ์","บวรรัช","พงศภัค","พิชญภูมิ","ภทรธร","พาพัฒน์"
,"ธนดล","ธนวัสส์","ธนากฤต","บารเมษฐ์","เป็นขลุ่ย","ปภังกร","พศิน","พาทิศ","พิชชากร","ภูมิพัฒน์","ภูริพงษ์","เมืองเอก","วิชศกร","อนุรุทธ์","ธรณ์ธันย์","อรภิชา","ศศิณัฎฐ์","ทิตชญา"],
    "longhair":["ณญากร","ณภัทร","ณัชชา(พันช์)","ณัฐปภัสร์","ณิชณัชทฐ์","ปัญญาภรณ์","พิชชาภา","ภคมน","ภัทรพร ","เมืองพลอย","สิรภัทร","สิริลภัส",
"จิรัชญา","ชนาภา","ญาดา","ณิชชา","นิยารินทร์","พิชชานันท์","อรภิชา","สิรินทร์"],
]

    }
    output = document.querySelector("#output")
    log = document.querySelector("#log")

    list=[]
    for i in specsin:
        list.append(specs.get(i))

   
    try:
        res = set(list[0]).intersection(*map(set, list[1:]))
        #res = set(list[0]).intersection(set(list[1]))
        resfin = "จากสเปคแล้วคุณเหมาะกับ : "+" , ".join(res)
    except:
        resfin = "ไม่พบคนตามสเปค"
  
    
    print("จากสเปคแล้วคุณเหมาะกับ : "+" , ".join(res))
    
    
   
    output.innerText = resfin
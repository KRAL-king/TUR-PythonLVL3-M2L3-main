# Görev 2 - İhtiyacınız olan her şeyi içe aktarın

class Question:
    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        # store options as a list for easier handling
        self.options = list(options)

    @property
    def text(self):
        return self.__text

    @property
    def answer_id(self):
        return self.__answer_id

    def gen_buttons(self):
        # Return the option labels as a list
        return self.options

# Görev 4 - Listeyi sorularınızla doldurun
flag_questions = [
   Question(
       "Aşağıdaki bayraklardan hangisi Türkiye bayrağıdır?",
       0,
       "tr.png",
       "pk.png",
       "az.png",
   ),
    Question(
         "Aşağıdaki bayraklardan hangisi Almanya bayrağıdır?",
         1,
         "fr.png",
         "de.png",
         "it.png",
    ),
    Question(
         "Aşağıdaki bayraklardan hangisi cezayir bayrağıdır?",
         2,
         "dz.png",
         "ma.png",
         "tn.png",
    ),
    Question(
         "Aşağıdaki bayraklardan hangisi rusya bayrağıdır?",1,
         "ba.png",
         "ru.png",
         "cz.png"),
    Question(
            "Aşağıdaki bayraklardan hangisi çin bayrağıdır?",0,
            "cn.png",
            "vn.png",
            "kr.png",
    ),
    Question("Aşağıdaki bayraklardan hangisi mısır bayrağıdır?",0, "eg.png", "ye.png", "iq.png")
    

          
  

   
]
cat_questions = [
   Question("Kediler onları kimse görmediğinde ne yapar?", 1, "Uyurlar", "Espri yazarlar"),
   Question("Kediler sevgilerini nasıl ifade ederler?", 0, "Yüksek sesle mırıldanırlar", "Sevimli fotoğraflar", "Havlar"),
   Question("Kediler hangi kitapları okumayı sever?", 3, "Kişisel gelişim kitapları", "Zaman yönetimi: Günde 18 saat nasıl uyunur","Sahibinizden 5 dakika erken uyumanın 101 yolu", "İnsan yönetimi rehberi")
]

# Combine available question sets into the single list used by the bot
quiz_questions = flag_questions + cat_questions

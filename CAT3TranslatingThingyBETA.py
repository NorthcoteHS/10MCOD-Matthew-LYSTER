"""
Prog: CAT3TranslatingThingyThatProbablyDoesntWork.py
Name: Matthew Lyster
Date: 7/6/18
Desc: A program that takes some of the most common phrases in japanese (hiragana/romaji) and accurately translates them into english.
"""

thisThing = input("What common japanese phrase would you like translated?(enter in HIRAGANA/ROMAJI): ")
thisThing = thisThing.lower()

thanks = ["ありがとう", "ありがとうございます", "ありがとうございました", "arigatou", "arigatougozaimasu", "arigatougozaimashita"]
if thisThing in thanks:
    print("arigatou/arigatougozaimasu/arigatougozaimashita: Thank you. 'arigatou' is a little less formal, kind of like 'thanks'. 'arigatougozaimasu' is basically the same thing, as well as 'arigatougozaimashita' only they are a tad less casual. Though the difference between 'arigatougozaimasu' and 'arigatougozaimashita' is very miniscule in that it's the tense;   '-masu' means present tense, so if someone is in the process of doing something for you then use 'arigatougozaimasu', whereas '-mashita' is past tense but you shouldn't really worry about those tiny differences at this point.")
baka = ["baka", "ばか"]
if thisThing in baka:
    print("baka: basically an insult referring to one's intelligence. Depending on the situation it can range from 'silly' to 'retard'.")
chigau = ["chigau", "ちがう"]
if thisThing in chigau:
    print("chigau: A verb that translates to something like 'to deviate' or 'to be different'. Commonly used to say someone is wrong. When exclaimed it can mean 'No way!' or 'Don't be rediculous'.")
chotto = ["chotto", "chiisai", "ちょっと", "ちいさい"]
if thisThing in chotto:
    print("chotto: a little. Only used as an adverb ('chiisai' is the adjective version). When exclaimed it can mean 'Hold it/on!' or 'Cut it out'.")
daijoubu = ["daijoubu", "だいじょうぶ"]
if thisThing in daijoubu:
    print("daijoubu: OK. Most commonly used in reference to someone's health.")
dame = ["dame", "だめ"]
if thisThing in dame:
    print("dame: no good, bad, no can do. ")
dare = ["dare", "だれ"]
if thisThing in dare:
    print("dare: who. certain particles can be added to the end to change the meaning, e.g. 'dareka' meaning someone.")
doko = ["doko", "どこ"]
if thisThing in doko:
    print("doko: where")
ganbaru = ["ganbaru", "がんばる"]
if thisThing in ganbaru:
    print("ganbaru: to do your best. Commonly used when encouraging someone, e.g. 'Hang in there!' or 'Do your best!'.")
iku = ["iku", "ikou", "ikimashou", "ike", "ikinasai", "いく", "いこう", "いきましょう", "いけ", "いきなさい"]
if thisThing in iku:
    print("iku: to go. other forms include ikimashou, ikou(Shall we go?/let's go), ike and ikinasai(Go!/Begone!)")
kami = ["kami", "かみ"]
if thisThing in kami:
    print("kami: God, god.")
kawaii = ["kawaii", "かわいい"]
if thisThing in kawaii:
    print("kawaii: cute.")
kokoro = ["kokoro", "こころ"]
if thisThing in kokoro:
    print("kokoro: heart.")
korosu = ["korosu", "ころす"]
if thisThing in korosu:
    print("korosu: to kill.")
kowai = ["kowai", "こわい"]
if thisThing in kowai:
    print("kowai: to be frightful, afraid.")
mahou = ["mahou", "まほう"]
if thisThing in mahou:
    print("mahou: magic, magic spell.")
masaka = ["masaka", "まさか"]
if thisThing in masaka:
    print("masaka: can it be?; It can't be!, No!")
mochiron = ["mochiron", "もちろん"]
if thisThing in mochiron:
    print("mochiron: of course, without a doubt.")
nani = ["nani", "なに"]
if thisThing in nani:
    print("nani: what.")
naruhodo = ["naruhodo", "なるほど"]
if thisThing in naruhodo:
    print("naruhodo: I see.; So.")
ohayou = ["ohayou", "ohayougozaimasu", "おはよう", "おはようございます"]
if thisThing in ohayou:
    print("ohayou/ohayougozaimasu: Good morning. ohayou is just an abbreviated form of ohayougozaimasu.")
onegai = ["onegai", "onegaishimasu", "おねがい", "おねがいします"]
if thisThing in onegai:
    print("onegai/onegaishimasu: 'I beg of you!', 'Please!'.")
senpai = ["senpai", "せんぱい"]
if thisThing in senpai:
    print("senpai: anyone in superior hierarchy.")
shinjiru = ["shinjiru", "しんじる"]
if thisThing in shinjiru:
    print("shinjiru: to believe in.")
shinu = ["shinu", "しぬ"]
if thisThing in shinu:
    print("shinu: to die.")
sugoi = ["sugoi", "suteki", "subarashii", "すごい", "すてき", "すばらしい"]
if thisThing in sugoi:
    print("sugoi/suteki/subarashii: common superlatives. Basically ways to say 'amazing'. They are all generally interchangeable, though there are a couple of slight differences. sugoi is often used when admiring someone else's talent or power, and can be mixed with a sense of dread, so either 'awesome' or 'awful' (usually awesome though). suteki is most often used in regard to  physical appearance (mostly for women, but can be used for anyone). subarashii is slightly more neutral, so it's more of a 'great'. Another spoken variant of sugoi is 'suge-e!'")
suki = ["suki", "すき"]
if thisThing in suki:
    print("suki: liking, affection. Also used fairly frequently to signify 'love'.")
taihen = ["taihen", "たいへん"]
if thisThing in taihen:
    print("taihen: when used modifying an adjective it means 'extremely'. When used with no adjectives describing a situation, it means 'terrible'.")
tasukeru = ["tasukeru", "tasukete", "tasukete kure", "たすける", "たすけて", "たすけて　くれ", "たすけてくれ"]
if thisThing in tasukeru:
    print("tasukeru: to aid. When exclaimed as 'tasukete kure!', this means something along the lines of 'Help/save me!'")
tomodachi = ["tomodachi", "ともだち"]
if thisThing in tomodachi:
    print("tomodachi: friend")
ureshii = ["ureshii", "うれしい"]
if thisThing in ureshii:
    print("ureshii: happy.")
urusai = ["urusai", "うるさい"]
if thisThing in urusai:
    print("urusai: noisy. As an exclamation, it means 'Be quiet!' or even 'Shut up!'")
wana = ["wana", "わな"]
if thisThing in wana:
    print("wana: trap, snare.")
wakaru = ["wakaru", "wakatta", "wakaranai", "wakannai", "wakanne-e", "わかる", "わかった", "わからない", "わかんあい", "わかんえーえ"]
if thisThing in wakaru:
    print("wakaru: to understand. other terms for this are 'wakatta' (understood) and 'wakaranai' (don't understand). There are also abbreviated forms of 'wakaranai', which seem to be gender specific, these being 'wakannai' (favoured by women) and 'wakaran' or 'wakanne-e' (favoured by men).")
yatta = ["yatta", "やった"]
if thisThing in yatta:
    print("yatta: used to proclaim victory or good fortune. Possible translations include 'hooray!', 'banzai!', 'I did it!' and 'Yay!'.")
yoshi = ["yoshi", "よし"]
if thisThing in yoshi:
    print("yoshi: used as an exclamation when readying oneself to take an important action. Possible translations could be 'Here I come', 'All right (,then)!'.")
youkai = ["youkai", "ようかい"]
if thisThing in youkai:
    print("youkai: an occult monster.")
yume = ["yume", "ゆめ"]
if thisThing in yume:
    print("yume: dream.")
else:
    print("sorry, I can't translate that :(    try again. (make sure you don't use any kanji, punctuation, or unnecessary spaces)")

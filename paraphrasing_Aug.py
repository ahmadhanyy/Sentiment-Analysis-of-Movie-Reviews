import spacy
from nltk.corpus import wordnet as wn

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define a function for paraphrasing
def paraphrase(texts):
    all_paraphrases = []
    for text in texts:
        # Process the input text
        doc = nlp(text)

        # Initialize lists to store synonyms for odd and even positions
        odd_synonyms = []
        odd_synonyms_positions = []
        even_synonyms = []
        even_synonyms_positions = []

        # Iterate over each token in the input text
        for i, token in enumerate(doc):
            # Check if the token is a noun, verb, adjective, or adverb
            if token.pos_ in ["NOUN", "VERB", "ADJ", "ADV"]:
                # Initialize synonym variable
                synonym = None
                # Find synonyms for the token's lemma using WordNet
                for synset in wn.synsets(token.lemma_):
                    for lemma in synset.lemmas():
                        synonym = lemma.name()
                        break  # Only consider the first synonym
                    if synonym:
                        break  # Exit the loop if synonym is found
                # Store synonyms based on odd or even positions
                if i % 2 == 0:
                    if synonym:
                        even_synonyms.extend([synonym] * len(token.text.split()))
                        even_synonyms_positions.append(i)
                else:
                    if synonym:
                        odd_synonyms.extend([synonym] * len(token.text.split()))
                        odd_synonyms_positions.append(i)

        even_paraphrase = ''
        odd_paraphrase = ''
        # Iterate over each token in the input text
        for i, token in enumerate(doc):
            # Check if the token's position is in the list of odd positions
            if i in odd_synonyms_positions:
                # Replace the token with a synonym from the odd list
                odd_paraphrase += odd_synonyms.pop(0) + " "
                # Keep the original token for the even paraphrase
                even_paraphrase += token.text + " "
            # Check if the token's position is in the list of even positions
            elif i in even_synonyms_positions:
                # Replace the token with a synonym from the even list
                even_paraphrase += even_synonyms.pop(0) + " "
                # Keep the original token for the odd paraphrase
                odd_paraphrase += token.text + " "
            else:
                # Keep the original token
                odd_paraphrase += token.text + " "
                even_paraphrase += token.text + " "
        
        all_paraphrases.append(text.strip())
        all_paraphrases.append(odd_paraphrase.strip())
        all_paraphrases.append(even_paraphrase.strip())

    return all_paraphrases

# Example usage
texts = [
    '''
    on june 30 , 1960 , a self-taught , idealistic , yet pragmatic , young man became , at age 36 , the first head of government of a newly independent african state , formerly the belgian congo . 
two months later , he was ousted from his powerful position and hunted by government troops until he was captured and brutally murdered along with two aides . 
this little-known story of this meteoric rise and fall is told my international filmmaker raoul peck in " lumumba . " 
patrice lumumba's ( eriq ebouaney ) story has been told previously by helmer peck in his 1991 award winning documentary , " lumumba - death of a prophet , " virtually guaranteeing that his new , fictional account of a patriot remains true to its subject . 
peck , with co-writer pascal bonitzer , begins at the end of the story of the young political leader . 
we watch as two white men perform the gruesome task of dismembering the bodies of three black men . 
images of hatchets , saws and fast-emptying whiskey bottles accompany the grisly image . 
jump back a few years to a meeting among the black leaders in the belgian-owned congo . 
a third class postal worker , lumumba , speaks his mind to heads of the most powerful tribes , proclaiming himself not tribal , not regional , but a national leader . 
his small , mobile party , the congolese national movement ( mnc ) is gaining prominence and patrice leaves his clerical job to sell beer , and get his face known , in the bustling capital , stanleyville . 
at a time when the colonial empires are falling down around the world , lumumba is in the right place at the right time and , through political savvy and chess-like manipulation , achieves a position of leadership of the mnc . 
as the date for independence approaches , he tactically positions himself to be the new nation's first prime minister and defense minister , supporting the presidency of joseph kasa vubu ( maka kotto ) . 
the coalition he created soon starts to fall apart as the former belgian masters continue to exert influence on the struggling nation as they strive to maintain economic hold on the country's vast natural resources of copper , diamonds , gold and more . 
lumumba won't seek the help of the us , knowing that they would try to create de facto american control of the fledgling government . 
his initial investigation into soviet assistance immediately tags patrice as a communist and his integrity is overshadowed by the cold war threat of russian domination . 
the situation goes from bad to worse as the army mutinies , the remaining whites begin to evacuate or arm themselves , belgian troops violently intervene , the lucrative katanga province succeeds under the leadership of rival moise tschombe ( pascal nzonzi ) and lumumba is refused access to his own country when he returns from a conference abroad . 
this tumultuous and little known period of modern african history saw a score of nations struggling for independence from the sometimes-odious colonialists who have ruled much of the world from their european seats of power for centuries . 
peck focuses his story on familiar material that strives to give an honest portrayal of patrice lumumba , his friend and foes and the independence movements that gripped africa in the 50's and 60's . 
 ( during the time the story takes place , many new nations , including nigeria and somalia , were born , with varying degrees of success and failure , usually dependent upon which country colonized them . 
some colonial masters were better than others . ) 
the effort involved in " lumumba " is quite ambitious as peck and his crew before and behind the camera strive to bring to life this slice of world history that might have gone unexplored for decades , if at all . 
production values are first rate on what must be a small , by us standards , budget . 
the period feel and realistic african settings are nicely maintained in a production that traveled from zimbabwe to mozambique . 
the screenplay covers a lot of ground and does yeoman's work in providing a great deal of detailed history while trying to do justice to the story of lumumba's life . 
the political side of things is evenly told in a linear , straightforward manner that teaches , not preaches . 
it concentrates on the good deeds of the man , if a bit as a stalwart saint , but doesn't embellish on a larger than life persona . 
the family side of patrice's life is handled in several , perfunctory and brief interludes that show him talking to one of his children , embracing his wife or lamenting the death of his child . 
i know the intent is to flesh the man out , but too short a shrift is given to the family man side of lumumba . 
the story , as such , has a lopsided feel about it . 
high marks go to eriq ebouaney as the title character . 
the actor gives a convincing , charismatic performance as the multifaceted , politically deft patrice lumumba who has the good of his people and his country as the force driving his own ambitions . 
in true docudrama tradition , the supporting cast does not outshine the star , complementing his good efforts , instead . 
 " lumumba " is a solid , interesting , educational and honest docudrama that should appeal to film buffs and politicos , both . 
it has more intelligence in its telling than anything i've seen out of hollywood for months and i give it a b+ . 

    ''',
    '''
    a movie like mortal kombat : annihilation works ( and must be reviewed on ) multiple levels . 
first , there's the rampant usage of randian subtext that pervades the entire movie . 
but occasionaly , almost as if making an ironic , self-depreciating remark , the movie tosses in clearly marxist imagery . 
no no . . . 
just kidding . 
had you going there for a moment , didn't i ? 
in all seriousness however , and to be fair to the movie , it * is * necessary to provide two viewpoints : that of a movie watcher unfamiliar ( or only marginally familiar ) with the whole mortal kombat phenomenon , and that of a fan of the first movie and/or a fan of the games . 
the first movie ( mortal kombat ( 1995 ) ) concerned itself with a martial arts tournament that would decide the fate of earth ( and it's 5 billion inhabitants ) . 
the mortals won , and in theory this should have prevented the emperor shao khan from taking over the earth . 
unfortunately , shao khan was a poor loser , and the very final scene in mortal kombat showed him arriving anyway , ready to take over the planet , as our heroes assumed a fighting stance . 
the first movie was extraordinarily entertaining for those ( like myself ) who are fans of the game . 
i'd even go so far as to say that many folks who didn't know about the game probably enjoyed the movie . 
the writers and directors knew the limitations of both their cast and of the basic story itself , and they didn't try to overachieve . 
there were a lot of really cool fight scenes ( with really cool accompanying music ) , intersperesed with some distracting ( but ultimately non-intrusive ) bits of fluff passing itself off as a plot . 
and , as we know , the movie was a smashing success at the box office . 
mortal kombat : annihilation picks up precisely where that movie left off , with some introductory exposition to clue in those who may not have seen the first movie . 
shao khan has decided that he's going to take over the earth * anyways * , and to hell with some silly rule about mortals winning the tournament . 
thereafter follows approximately 85 minutes of film that alternates between being confused , being trite , being silly , and being just plain stupid . 
one gets the general impression that the producers of the movie thought " hey , that last movie was such a success that we can get more money and make a * real * movie now . " 
too bad they didn't simply stick with the formula from the first movie . 
i could write volumes about the things that are wrong with this picture , but here are the high points : 
 * the acting is truly bad . 
sandra hess ( playing the sonya blade character ) is particularly execrable , especially in scenes where she tries to convince us that she loved johnny cage ( a character from the first movie who gets greased at the beginning of this movie ) . 
 * in one of the worst pieces of mis-casting i think i've * ever * seen , james remar plays raiden , the god of thunder . 
in the first movie , christopher lambert played raiden and played his character as though he was in on the joke : a french actor playing a japanese thunder god being revered by chinese mystics . 
i generally like it when actors are cast against type ( tim " tiny " lister , jr . being cast as the president of the u . s . in the fifth element , for example ) , and remar has always been one of my favorite " utility " actors but he's so totally wrong for this part that he doesn't even have the luxury of amused self-awareness . 
 * there are too many characters that are introduced as being potentially important , but then never seen again . 
 * there are a number of completely meaningless story sidetracks , including a muddled scene where liu kang ( robin shou ) seeks out nightwolf ( litefoot ) , has a mystical hallucination , and then wanders off with jade ( irina pantaeva ) . 
for these reasons ( and many others ) , i can only give the movie a 2 . . . 
 . . . unless you're a huge fan of the games and/or the first movie . 
in that case , the following critiques also apply : 
 * sandra hess , while being an even worse actress than bridgette wilson ( who played sonya blade in the first movie ) , is much more convincing as a fighter . 
wilson looked like she was simply mimicing some movements taught to her by the fight choreographer . 
hess looks like she actually knows some martial arts , and puts together a much more believable fight scene . 
 * in the fights , each of the characters does at least * one * thing they do in the game ( and often more ) . 
sonya does her " kiss of death , " jax does his " earthquake , " liu kang does his " animality , " and so on . 
a big bonus for those of us who were looking for similar moves in the first movie and found them only rarely . 
 * there aren't as many fight scenes in this movie as there were in the first , because the folks making the movie mistakenly try to hang a more robust plot in between . 
silly , silly folks . 
and the lamest fight involved two of the women in what turns into a mud-wrestling match . 
lame and so obviously sexist even i ( politically incorrect , for the most part ) noticed and remarked upon it . 
 * the special effects are generally better , except for the final fight scene between the emporer and liu kang in which both perform their " animalities . " 
motaro and sheeva are both more convincing and lifelike than goro was in the first movie . 
for folks like myself who loved the first movie and enjoy the games , i give this a 5 . 
you'll probably like it , but not nearly as much as you liked the first one . 

    '''
]

paraphrases = paraphrase(texts)

# Print the paraphrases
#print("Paraphrases:")
#for idx, para_set in enumerate(paraphrases):
    #print(f"Text {idx + 1}:")
    #print("Original:", para_set[0])
    #print("Odd Paraphrase:", para_set[1])
    #print("Even Paraphrase:", para_set[2])
print('----------------------------------------------------------------')
print(len(paraphrases))
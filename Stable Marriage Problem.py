import random

proposing='male'
numpeople=100 #<=100
printing=0

malenames=['Noah', 'Liam', 'Jacob', 'Mason', 'William', 'Ethan', 'Michael', 'Alexander', 'Jayden', 'Daniel', 'Elijah', 'Aiden', 'James', 'Benjamin', 'Matthew', 'Jackson', 'Logan', 'David', 'Anthony', 'Joseph', 'Joshua', 'Andrew', 'Lucas', 'Gabriel', 'Samuel', 'Christopher', 'John', 'Dylan', 'Isaac', 'Ryan', 'Nathan', 'Carter', 'Caleb', 'Luke', 'Christian', 'Hunter', 'Henry', 'Owen', 'Landon', 'Jack', 'Wyatt', 'Jonathan', 'Eli', 'Isaiah', 'Sebastian', 'Jaxon', 'Julian', 'Brayden', 'Gavin', 'Levi', 'Aaron', 'Oliver', 'Jordan', 'Nicholas', 'Evan', 'Connor', 'Charles', 'Jeremiah', 'Cameron', 'Adrian', 'Thomas', 'Robert', 'Tyler', 'Colton', 'Austin', 'Jace', 'Angel', 'Dominic', 'Josiah', 'Brandon', 'Ayden', 'Kevin', 'Zachary', 'Parker', 'Blake', 'Jose', 'Chase', 'Grayson', 'Jason', 'Ian', 'Bentley', 'Adam', 'Xavier', 'Cooper', 'Justin', 'Nolan', 'Hudson', 'Easton', 'Jase', 'Carson', 'Nathaniel', 'Jaxson', 'Kayden', 'Brody', 'Lincoln', 'Luis', 'Tristan', 'Damian', 'Camden', 'Juan']
femalenames=['Sophia', 'Emma', 'Olivia', 'Isabella', 'Ava', 'Mia', 'Emily', 'Abigail', 'Madison', 'Elizabeth', 'Charlotte', 'Avery', 'Sofia', 'Chloe', 'Ella', 'Harper', 'Amelia', 'Aubrey', 'Addison', 'Evelyn', 'Natalie', 'Grace', 'Hannah', 'Zoey', 'Victoria', 'Lillian', 'Lily', 'Brooklyn', 'Samantha', 'Layla', 'Zoe', 'Audrey', 'Leah', 'Allison', 'Anna', 'Aaliyah', 'Savannah', 'Gabriella', 'Camila', 'Aria', 'Kaylee', 'Scarlett', 'Hailey', 'Arianna', 'Riley', 'Alexis', 'Nevaeh', 'Sarah', 'Claire', 'Sadie', 'Peyton', 'Aubree', 'Serenity', 'Ariana', 'Genesis', 'Penelope', 'Alyssa', 'Bella', 'Taylor', 'Alexa', 'Kylie', 'Mackenzie', 'Caroline', 'Kennedy', 'Autumn', 'Lucy', 'Ashley', 'Madelyn', 'Violet', 'Stella', 'Brianna', 'Maya', 'Skylar', 'Ellie', 'Julia', 'Sophie', 'Katherine', 'Mila', 'Khloe', 'Paisley', 'Annabelle', 'Alexandra', 'Nora', 'Melanie', 'London', 'Gianna', 'Naomi', 'Eva', 'Faith', 'Madeline', 'Lauren', 'Nicole', 'Ruby', 'Makayla', 'Kayla', 'Lydia', 'Piper', 'Sydney', 'Jocelyn', 'Morgan']

malenames=malenames[:numpeople]
femalenames=femalenames[:numpeople]


def Print(*arg, end='\n'):
    global printing
    if printing:
        print(' '.join([str(i) for i in arg]), end=end)

class person():
    global proposingpeople
    name=''
    single=True
    pname=''
    prefs=[]
    proposenumber=0
    def __init__(self, name, prefs):
        self.name=name
        self.prefs=prefs
    def getproposed(self, person):
        response=False
        if self.single:
            Print(self.name,': Yes, because im single :(')
            response=True
            self.pname=person.name
        elif self.prefs.index(person.name)<self.prefs.index(self.pname):
            Print(self.name,": Yes! You're better! (",self.prefs.index(person.name),'<',self.prefs.index(self.pname),')')
            response=True            
            for i in range(len(proposingpeople)):
                if proposingpeople[i].name==self.pname:
                    proposingpeople[i].reject()
                    Print(self.name,': rejected:',proposingpeople[i].name)
            self.pname=person.name
        else:
            Print(self.name,": nope, I'm good.")
        self.single=False
        return response
    def propose(self, person):
        Print(self.name,': proposing:', person.name)
        
        if person.getproposed(self):
            Print(self.name,': success!')
            self.pname=person.name
            self.single=False
        else:
            self.proposenumber+=1
    def reject(self):
        Print(self.name, ': I got rejected!! :(')
        self.proposenumber+=1
        self.single=True
    def go(self):
        g=0
        if self.single:
            self.propose(proposedpeople[[i.name for i in proposedpeople].index(self.prefs[self.proposenumber])])
            
proposingpeople=[]
proposedpeople=[]
if proposing=='female':
    for i in range(numpeople):
        mn=malenames[:]
        fn=femalenames[:]
        random.shuffle(mn)
        random.shuffle(fn)
        proposingpeople.append(person(femalenames[i], mn))
        proposedpeople.append(person(malenames[i], fn))
if proposing=='male':
    for i in range(numpeople):
        mn=malenames[:]
        fn=femalenames[:]
        random.shuffle(mn)
        random.shuffle(fn)
        proposingpeople.append(person(malenames[i], fn))
        proposedpeople.append(person(femalenames[i], mn))
        

while (True in [i.single for i in (proposingpeople+proposedpeople)]):
    singleladies=[]
    for i in (proposingpeople+proposedpeople):
        if i.single:
            singleladies.append(i.name)
    Print(str(len(singleladies))+' people are single, they are: '+', '.join(singleladies))
    for pperson in proposingpeople:
        pperson.go()


proposedpeoplepicks=[]
proposingpeoplepicks=[]
for pperson in proposedpeople:
    try:
        Print(pperson.name+'♥'+ pperson.pname)
    except:
        Print(pperson.name+' and '+ pperson.pname)
for pperson in proposedpeople:
    Print(pperson.name,'got the',pperson.prefs.index(pperson.pname)+1,'pick.')
    proposedpeoplepicks.append(pperson.prefs.index(pperson.pname)+1)
for pperson in proposingpeople:
    Print(pperson.name,'got the',pperson.prefs.index(pperson.pname)+1,'pick. ('+str(pperson.proposenumber+1)+')')
    proposingpeoplepicks.append(pperson.prefs.index(pperson.pname)+1)

print('\nproposed ('+['male', 'female'][int(proposing=='male')]+') average:', sum(proposedpeoplepicks)/len(proposedpeoplepicks))
print('proposing ('+proposing+') average:', sum(proposingpeoplepicks)/len(proposingpeoplepicks))
input()








    

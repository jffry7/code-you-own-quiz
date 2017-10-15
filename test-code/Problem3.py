#!/usr/bin/python
# coding=utf-8

"""
req D100 missing docstring.

D200 more than one line required
"""
# Create a distribution table of all the letters in this article. The table should be a dictionary
# that contains every letter found in this article and the count of how many of the characters
# is present in the article.
#
# Article copied from Paul Ford's "What is Code?"


def find_character_count_dict(some_string):
    #     Find the count of each character in a given string
    # Takes a string as input, returns a dictionary.
    character_count_dict = {}
    while some_string:
        current_char = str(some_string[0])
        if current_char in character_count_dict:
            character_count_dict[current_char] += 1
        else:
            character_count_dict[current_char] = 1
        some_string = some_string[1:]
    return character_count_dict


"""
def find_character_count_list(some_string):
    Find the count of each character in a given string.
    Takes a string as input, returns two lists:
    The first list is the characters encountered.
    The second list is the count for each given character from the first list
    characters = []
    character_count_list = []
    while some_string:
        current_char = str(some_string[0])
        if current_char in characters:
            for i in range(len(characters)):
                if current_char == characters[i]:
                    character_count_list[i] += 1
                    break
        else:
            characters.append(current_char)
            character_count_list.append(1)
        some_string = some_string[1:]
    return characters, character_count_list
"""

article = """
You are an educated, successful person capable of abstract thought. A VP doing an SVP's job. Your office, appointed with decent furniture and a healthy amount of natural light filtered through vertical blinds, is commensurate with nearly two decades of service to the craft of management.

Copper plaques on the wall attest to your various leadership abilities inside and outside the organization: One, the Partner in Innovation Banquet Award 2011, is from the sales team for your support of its 18-month effort to reduce cycle friction—net sales increased 6.5 percent; another, the Civic Guidelight 2008, is for overseeing a volunteer team that repainted a troubled public school top to bottom.

You have a reputation throughout the organization as a careful person, bordering on penny-pinching. The way you’d put it is, you are loath to pay for things that can’t be explained. You expect your staff to speak in plain language. This policy has served you well in many facets of operations, but it hasn’t worked at all when it comes to overseeing software development.

For your entire working memory, some Internet thing has come along every two years and suddenly hundreds of thousands of dollars (inevitably millions) must be poured into amorphous projects with variable deadlines. Content management projects, customer relationship management integration projects, mobile apps, paperless office things, global enterprise resource planning initiatives—no matter how tightly you clutch the purse strings, software finds a way to pry open your fingers.

Here we go again. On the other side of your (well-organized) desk sits this guy in his mid-30s with a computer in his lap. He’s wearing a taupe blazer. He’s come to discuss spending large sums to create intangible abstractions on a “website re-architecture project.” He needs money, support for his team, new hires, external resources. It’s preordained that you’ll give these things to him, because the CEO signed off on the initiative—and yet should it all go pear-shaped, you will be responsible.
Coders are insanely expensive, and projects that start with uncomfortably large budgets have an ugly tendency to grow from there. You need to understand where the hours will go.


PHOTOGRAPHER: COREY OLSEN FOR BLOOMBERG BUSINESSWEEK
He says: “We’re basically at the limits with WordPress.”

Who wears a taupe blazer?

The CTO was fired six months ago. That CTO has three kids in college and a mustache. It was a bad exit. The man in the taupe blazer (TMitTB) works for the new CTO. She comes from Adobe and has short hair and no mustache.

Here is what you’ve been told: All of the computer code that keeps the website running must be replaced. At one time, it was very valuable and was keeping the company running, but the new CTO thinks it’s garbage. She tells you the old code is spaghetti and your systems are straining as a result. That the third-party services you use, and pay for monthly, are old and busted. Your competitor has an animated shopping cart that drives across the top of the screen at checkout. That cart remembers
everything customers have ever purchased and generates invoices on demand. Your cart has no memory at all.

Salespeople stomp around your office, sighing like theater students, telling you how embarrassed they are by the site. Nothing works right on mobile. Orders are cutting off halfway. People are logged out with no warning. Something must be done.

Which is why TMitTB is here.

Who’s he, anyway? Webmaster? IT? No, he’s a “Scrum Master.”

“My people are split on platform,” he continues. “Some want to use Drupal 7 and make it work with Magento—which is still PHP.” He frowns. “The other option is just doing the back end in Node.js with Backbone in front.”

You’ve furrowed your brow; he eyes you sympathetically and explains: “With that option it’s all JavaScript, front and back.”

Those are all terms you’ve heard. You’ve read the first parts of the Wikipedia pages and a book on software project estimation. It made some sense at the time.

You ask the universal framing question: “Did you cost these options?”

He gives you a number and a date. You know in your soul that the number is half of what it should be and that the project will go a year over schedule. He promises long-term efficiencies: The $85,000 in Oracle licenses will no longer be needed; engineering is moving to a free, open-sourced database. “We probably should have done that back when we did the Magento migration,” he says. Meaning, of course, that his predecessor probably should have done that.

You consult a spreadsheet and remind him that the Oracle contract was renewed a few months ago. So, no, actually, at least for now, you’ll keep eating that cost. Sigh.

This man makes a third less than you, and his education ended with a B.S. from a large, perfectly fine state university. But he has 500+ connections on LinkedIn. That plus sign after the “500” bothers you. How many more than 500 people does he know? Five? Five thousand?

We know that a computer is a clock with benefits, and that software starts as code, but how?

We know that someone, somehow, enters a program into the computer and the program is made of code. In the old days, that meant putting holes in punch cards. Then you’d put the cards into a box and give them to an operator who would load them, and the computer would flip through the cards, identify where the holes were, and update parts of its memory, and then it would—OK, that’s a little too far back. Let’s talk about modern typing-into-a-keyboard code. It might look like this:

ispal: {x~|x}
That’s in a language called, simply, K, famous for its brevity. 2 That code will test if something is a palindrome. If you next typed in ispal "able was i ere i saw elba", K will confirm that yes, this is a palindrome.

So how else might your code look? Maybe like so, in Excel (with all the formulas hidden away under the numbers they produce, and a check box that you can check):

Excel
But Excel spreadsheets are tricky, because they can hide all kinds of things under their numbers. This opacity causes risks. One study by a researcher at the University of Hawaii found that 88 percent of spreadsheets contain errors.

Programming can also look like Scratch, a language for kids:

Scratch
That’s definitely programming right there—the computer is waiting for a click, for some input, just as it waits for you to type an “a,” and then it’s doing something repetitive, and it involves hilarious animals.

Or maybe:

      PRINT *, "WHY WON'T IT WORK
      END

That’s in Fortran. The reason it’s not working is that you forgot to put a quotation mark at the end of the first line. Try a little harder, thanks.

All of these things are coding of one kind or another, but the last bit is what most programmers would readily identify as code. A sequence of symbols (using typical keyboard characters, saved to a file of some kind) that someone typed in, or copied, or pasted from elsewhere. That doesn’t mean the other kinds of coding aren’t valid or won’t help you achieve your goals. Coding is a broad human activity, like sport, or writing. When software developers think of coding, most of them are thinking
about lines of code in files. They’re handed a problem, think about the problem, write code that will solve the problem, and then expect the computer to turn word into deed.

Code is inert. How do you make it ert? You run software that transforms it into machine language. The word “language” is a little ambitious here, given that you can make a computing device with wood and marbles. Your goal is to turn your code into an explicit list of instructions that can be carried out by interconnected logic gates, thus turning your code into something that can be executed—software.

A compiler is software that takes the symbols you typed into a file and transforms them into lower-level instructions. Imagine a programming language called Business Operating Language United System, or Bolus. It’s a terrible language that will have to suffice for a few awkward paragraphs. It has one real command, PRINT. We want it to print HELLO NERDS on our screen. To that end, we write a line of code in a text file that says:

PRINT {HELLO NERDS}
And we save that as nerds.bol. Now we run gnubolus nerds.bol, our imaginary compiler program. How does it start? The only way it can: by doing lexical analysis, going character by character, starting with the “p,” grouping characters into tokens, saving them into our one-dimensional tree boxes. Let’s be the computer.

Character Meaning
P Hmmmm...?
R Someone say something?
I I’m waiting...
N [drums fingers]
T Any time now...
Space Ah, "PRINT"
{ String coming!
H These
E letters
L don’t
L matter
O la
Space la
N just
E saving
R them
D for
S later
} Stringtime is over!
End of file Time to get to work.
The reason I’m showing it to you is so you can see how every character matters. Computers usually “understand” things by going character by character, bit by bit, transforming the code into other kinds of code as they go. The Bolus compiler now organizes the tokens into a little tree. Kind of like a sentence diagram. Except instead of nouns, verbs, and adjectives, the computer is looking for functions and arguments. Our program above, inside the computer, becomes this:


Trees are a really pleasant way of thinking of the world. Your memo at work has sections that have paragraphs? Tree. Your e-mail program contains messages that contain subject lines and addresses? Tree. Your favorite software program that has a menu bar with individual items that have subitems? Tree. Every day is Arbor Day in Codeville.

You are reading a tree right now! Look down there. You’ll see this section of the article organized as a tree. Click the boxes to expand branches for every paragraph, image, and table. Everything you have just read is a branch—even this graphic of a tree. That’s right: This tree contains a tree. Computers are weird.
paragraphparagraphparagraphsubsubheadinggeneric block containerparagraphparagraphparagraphparagraphparagraphparagraphparagraphEmbedded imageparagraphgeneric block containergeneric block containerparagraphEmbedded imageparagraphtablegeneric block container

Of course, it’s all a trick. If you cut open a computer, you’ll find countless little boxes in rows, places where you can put and retrieve bytes. Everything ultimately has to get down to things in little boxes pointing to each other. That’s just how things work. So that tree is actually more like this:

Every character truly, truly matters. Every single stupid misplaced semicolon, space where you meant tab, bracket instead of a parenthesis—mistakes can leave the computer in a state of panic. The trees don’t know where to put their leaves. Their roots decay. The boxes don’t stack neatly. For not only are computers as dumb as a billion marbles, they’re also positively Stradivarian in their delicacy.

That process of going character by character can be wrapped up into a routine—also called a function, a method, a subroutine, or component. (Little in computing has a single, reliable name, which means everyone is always arguing over semantics.) And that routine can be run as often as you need. Second, you can print anything you wish, not just one phrase. Third, you can repeat the process forever, and nothing will stop you until the machine breaks or, barring that, heat death of the universe.
Obviously no one besides Jack Nicholson in The Shining really needs to keep typing the same phrase over and over, and even then it turned out to be a bad idea.

Instead of worrying about where the words are stored in memory and having to go character by character, programming languages let you think of things like strings, arrays, and trees. That’s what programming gives you. You may look over a programmer’s shoulder and think the code looks complex and boring, but it’s covering up repetitive boredom that’s unimaginably vast. 3

This thing we just did with individual characters, compiling a program down into a fake assembly language so that the nonexistent computer can print each character one at a time? The same principle applies to every pixel on your screen, every frequency encoded in your MP3 files, and every imaginary cube in Minecraft. Computing treats human language as an arbitrary set of symbols in sequences. It treats music, imagery, and film that way, too.

It’s a good and healthy exercise to ponder what your computer is doing right now. Maybe you’re reading this on a laptop: What are the steps and layers between what you’re doing and the Lilliputian mechanisms within? When you double-click an icon to open a program such as a word processor, the computer must know where that program is on the disk. It has some sort of accounting process to do that. And then it loads that program into its memory—which means that it loads an enormous to-do list into
its memory and starts to step through it. What does that list look like?

Maybe you’re reading this in print. No shame in that. In fact, thank you. The paper is the artifact of digital processes. Remember how we put that “a” on screen? See if you can get from some sleepy writer typing that letter on a keyboard in Brooklyn, N.Y., to the paper under your thumb. What framed that fearful symmetry?

Thinking this way will teach you two things about computers: One, there’s no magic, no matter how much it looks like there is. There’s just work to make things look like magic. And two, it’s crazy in there.

"""
# Let's try a different article to see if the problem is that variable
character_dict = find_character_count_dict(article)
for character in character_dict:
    print character, character_dict[character]

# print character_dict

print "End Dictionary!"

"""characters, character_count_list = find_character_count_list(article)
for i in range(len(characters)):
    # Let's test to see if the list version gives the same answer as the dictionary one
    char, count = characters[i], character_count_list[i]
    if char in character_dict:
        if count != character_dict[char]:
            print char, ": ", count, "Should be:", character_dict[char]
        # else: #if we want to see what characters are here
        #     print "Good!", char, ' = ', count
    else:
        print char, 'not in list.'
"""

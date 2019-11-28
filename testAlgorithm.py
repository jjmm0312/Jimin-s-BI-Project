#import dprocess
import recommendation
from flask import Flask, request, jsonify
import json

if __name__ == "__main__":

    NEWS_DATA = []
    TAG_DATA = []

    print('i am okay')
    fname = 'old_list.json'

    with open(fname, "r") as st_json:
        NEWS_DATA = json.load(st_json)

    for i in range (len(NEWS_DATA)):
        NEWS_DATA[i]['index'] = i

    print(NEWS_DATA[0])

    '''
    with open(fname) as st_json:
        i=0
        for line in st_json:
            item = json.loads(line)
            item['index'] = i
            NEWS_DATA.append(item)
            i = i+1
    '''
    '''
    print(NEWS_DATA[0])
    print(NEWS_DATA[1])
    print(NEWS_DATA[2])
    '''
    print('data load finish\n\n')

    # data_processing
    #TAG_DATA = dprocess.data_process(NEWS_DATA)
    fname = 'corpus.json'
    with open(fname, "r") as st_json:
        TAG_DATA = json.load(st_json)
    print("data process finish")

    #print(TAG_DATA[0])

    history = [{'category': 'ENTERTAINMENT', 'headline': "'Westworld' Conspiracy Theory About Stock Photo Gets New Twist", 'authors': 'Bill Bradley and Leigh Blickley', 'link': 'https://www.huffingtonpost.com/entry/westworld-conspiracy-theory-about-that-photo-gets-crazier_us_5ae23f89e4b02baed1b8666d', 'short_description': 'The woman from that "Westworld" photo is now on the show, and everything just got more interesting.', 'date': '2018-04-30', 'index': 26333}, {'category': 'ENTERTAINMENT', 'headline': "Emma Stone Delivered The Perfect Burn To The Oscars' Male-Dominated Director Category", 'authors': 'Alanna Vagianos', 'link': 'https://www.huffingtonpost.com/entry/emma-stone-delivered-the-perfect-burn-to-the-oscars-male-dominated-director-category_us_5a9cc467e4b0479c0254298e', 'short_description': 'So. Much. Shade.', 'date': '2018-03-05', 'index': 26937}, {'category': 'ENTERTAINMENT', 'headline': "Jimmy O. Yang Of ‘Silicon Valley’: Asians Who Aren't Hunks Need Screen Time, Too!", 'authors': 'Kimberly Yam', 'link': 'https://www.huffingtonpost.com/entry/jimmy-o-yang-silicon-valley-how-to-american_us_5ab11d30e4b0eb3e2b30bc07', 'short_description': '"What are you going to tell me? Don’t represent me on TV because I don’t look like Chow Young Fat? Like f**k you, dude!"', 'date': '2018-03-28', 'index': 26709}, {'category': 'ENTERTAINMENT', 'headline': "'Sense8' Filmed Its Finale. Daryl Hannah Weighs In On What To Expect.", 'authors': 'Lauren Moraski', 'link': 'https://www.huffingtonpost.com/entry/sense8-just-filmed-its-finale-daryl-hannah-weighs-in-on-what-to-expect_us_5ab2b3a2e4b0decad04664a3', 'short_description': 'The Netflix series, abruptly canceled last year, will return one last time.', 'date': '2018-03-23', 'index': 26756}, {'category': 'ENTERTAINMENT', 'headline': 'This Is What Super Mario Looks Like Without Hair, And People Are Freaked Out', 'authors': 'Elyse Wanshel', 'link': 'https://www.huffingtonpost.com/entry/this-is-what-super-mario-looks-like-without-hair-and-people-are-freaked-out_us_5af9eb7ae4b0200bcab7e6e7', 'short_description': 'He’s missing his sideburns, iconic mustache and eyebrows.', 'date': '2018-05-14', 'index': 26155}, {'category': 'ENTERTAINMENT', 'headline': "Luke Bryan Defends Katy Perry Over 'Uncomfortable' American Idol Kiss", 'authors': 'Carly Ledbetter', 'link': 'https://www.huffingtonpost.com/entry/luke-bryan-defends-katy-perry-over-uncomfortable-american-idol-kiss_us_5ab2a4a8e4b008c9e5f3ab44', 'short_description': '“It’s unfortunate that stuff like that turns into a story that big."', 'date': '2018-03-21', 'index': 26783}, {'category': 'ENTERTAINMENT', 'headline': 'Former Dave Matthews Band Violinist Boyd Tinsley Accused Of Sexual Misconduct', 'authors': 'David Moye', 'link': 'https://www.huffingtonpost.com/entry/boyd-tinsley-accused-sexual-misconduct_us_5aff133ce4b07309e057c71d', 'short_description': '"I will defend myself against these false accusations," Tinsley said in a statement.', 'date': '2018-05-18', 'index': 26101}, {'category': 'ENTERTAINMENT', 'headline': 'Geena Davis And 4th Husband Reza Jarrahy Are Divorcing', 'authors': 'Ron Dicker', 'link': 'https://www.huffingtonpost.com/entry/geena-davis-and-longtime-4th-husband-reza-jarrahy-are-divorcing_us_5af2bdb6e4b0a0d601e824f4', 'short_description': 'The surgeon cited irreconcilable differences with the "Thelma & Louise" star.', 'date': '2018-05-09', 'index': 26218}, {'category': 'ENTERTAINMENT', 'headline': 'Armie Hammer Shares His Mug Shot From A 2011 Arrest For Weed', 'authors': 'Carly Ledbetter', 'link': 'https://www.huffingtonpost.com/entry/armie-hammer-mug-shot-arrest_us_5aa91dbbe4b001c8bf15b251', 'short_description': 'Thanks for sharing, Armie.', 'date': '2018-03-14', 'index': 26842}, {'category': 'ENTERTAINMENT', 'headline': "John Mayer's Weird New Low-Budget Video Is A Meme-Worthy Masterpiece", 'authors': 'Ed Mazza', 'link': 'https://www.huffingtonpost.com/entry/john-mayer-new-light-video_us_5b0780d6e4b0568a8809b6fa', 'short_description': 'Mayer\'s hilariously strange "New Light" video even spells his name wrong.', 'date': '2018-05-25', 'index': 26024}, {'category': 'ENTERTAINMENT', 'headline': "Twitter Goes Bonkers Over WTF 'Bachelor' Finale", 'authors': 'Ron Dicker', 'link': 'https://www.huffingtonpost.com/entry/twitter-goes-bonkers-over-wtf-bachelor-finale_us_5a9e641fe4b0a0ba4ad7769d', 'short_description': 'Viewers had some less-romantic proposals for Arie Luyendyk Jr.', 'date': '2018-03-06', 'index': 26925}, {'category': 'ENTERTAINMENT', 'headline': 'Moses Farrow Defends Woody Allen And Accuses Mia Farrow Of Abuse', 'authors': 'Ron Dicker', 'link': 'https://www.huffingtonpost.com/entry/moses-farrow-mia-farrow-abuse_us_5b0681ace4b07c4ea10510c2', 'short_description': 'Dylan Farrow called her brother\'s essay "beyond hurtful" and "easily disproven."', 'date': '2018-05-24', 'index': 26034}, {'category': 'ENTERTAINMENT', 'headline': "Margot Kidder, Actress Who Played Lois Lane In 'Superman,' Dead At 69", 'authors': 'David Moye', 'link': 'https://www.huffingtonpost.com/entry/margot-kidder-lois-lane-dead-dies_us_5af9bd81e4b0200bcab7a375', 'short_description': 'The cause of death has not been made public.', 'date': '2018-05-14', 'index': 26164}, {'category': 'CRIME', 'headline': 'Muslim Man Shot Near Mosque In Texas', 'authors': 'Alana Horowitz Satlin', 'link': 'https://www.huffingtonpost.com/entry/muslim-man-shot-mosque-texas_us_577904b8e4b0a629c1aa5cab', 'short_description': "Police said there's no indication that the attack was a hate crime, but its proximity to the mosque has some members worried.", 'date': '2016-07-03', 'index': 27992}, {'category': 'CRIME', 'headline': 'Dylann Roof Mentally Competent To Stand Trial, Judge Rules', 'authors': '', 'link': 'https://www.huffingtonpost.com/entry/dylann-roof-trial-psychiatric-evaluation_us_5838550be4b01ba68ac4730e', 'short_description': 'Earlier this month, defense attorneys had raised concerns for the first time about whether Roof was able to understand the nature of the proceedings against him and to assist in his defense.', 'date': '2016-11-25', 'index': 27691}, {'category': 'CRIME', 'headline': 'Charles Manson Reportedly Hospitalized, In Deteriorating Condition', 'authors': 'Carla Herreria', 'link': 'https://www.huffingtonpost.com/entry/charles-manson-hospitalized_us_5a0cd32ae4b0b17e5e13d996', 'short_description': 'The infamous mass murderer is serving a life sentence in a California prison.', 'date': '2017-11-16', 'index': 27222}, {'category': 'CRIME', 'headline': "Feds Escalate Charges Against Edgar Welch, Alleged 'Pizzagate' Shooter", 'authors': 'Kim Bellware', 'link': 'https://www.huffingtonpost.com/entry/pizzagate-federal-charges_us_58502c44e4b0bd9c3dfef964', 'short_description': 'Federal investigators have tacked on two more charges since the initial indictment.', 'date': '2016-12-13', 'index': 27650}, {'category': 'CRIME', 'headline': "Package Thief Gets A Painful Dose Of Instant Karma, And It's All Caught On Video", 'authors': 'Ed Mazza', 'link': 'https://www.huffingtonpost.com/entry/package-thief-instant-karma_us_5a6fe79fe4b0a52682fede41', 'short_description': "That's gotta hurt.", 'date': '2018-01-30', 'index': 27146}, {'category': 'CRIME', 'headline': "Woman Maced 3 Wendy's Employees For Serving Stale Fries, Police Say", 'authors': 'David Moye', 'link': 'https://www.huffingtonpost.com/entry/stale-fries-wendys-attack_us_5925b503e4b0ec129d31964e', 'short_description': "Where's the beef? With the fries!", 'date': '2017-05-24', 'index': 27390}, {'category': 'CRIME', 'headline': 'Uber Faces Criminal Probe Over Software Used To Evade Authorities', 'authors': 'Dan Levine and Joseph Menn, Reuters', 'link': 'https://www.huffingtonpost.com/entry/uber-faces-criminal-probe-over-software-used-to-evade-authorities_us_590be33ee4b0e7021e966a38', 'short_description': 'The criminal probe adds to the problems facing the struggling company.', 'date': '2017-05-05', 'index': 27404}, {'category': 'CRIME', 'headline': 'Neighbor Opens Fire As Father In Clown Mask Chases Child', 'authors': 'Nina Golgowski', 'link': 'https://www.huffingtonpost.com/entry/father-clown-mask-chases-child_us_59bffc72e4b06f9bf04865ee', 'short_description': "The dad said he wanted to scare his daughter into behaving, but she ran screaming into a stranger's home.", 'date': '2017-09-19', 'index': 27299}, {'category': 'PARENTS', 'headline': 'Why I’m Done Apologizing for My Son’s Autism', 'authors': 'Mandy Cowley, ContributorFreelance creative and activist.', 'link': 'https://www.huffingtonpost.com/entry/why-im-done-apologizing-for-my-sons-autism_us_59c6ae08e4b0f2df5e83aeb6', 'short_description': 'I’ve spent a significant amount of time over the past six years apologizing to people because of my son’s disability.', 'date': '2017-09-23', 'index': 18287}, {'category': 'PARENTS', 'headline': 'Of Course, Serena Williams Had A Most Iconic Baby Shower Theme', 'authors': 'Doha Madani', 'link': 'https://www.huffingtonpost.com/entry/serena-williams-baby-shower-theme_us_5987107ce4b08b75dcc77dd1', 'short_description': 'And her squad of ladies made it even better.', 'date': '2017-08-06', 'index': 18480}, {'category': 'PARENTS', 'headline': 'Single Mom Makes Major Statement At School Event For Dads', 'authors': 'Elise Solé, Yahoo Lifestyle', 'link': 'https://www.huffingtonpost.com/entry/single-mom-makes-major-statement-at-school-event-for-dads_us_5a15bc27e4b025f8e9333212', 'short_description': 'A single mom who didn’t want her kids to feel left out on “Doughnuts With Dad” day at school hit the event dressed as a man', 'date': '2017-11-22', 'index': 18097}, {'category': 'PARENTS', 'headline': 'Dad Asks Famous People To Tweet His Bullied Son A Happy Birthday, And They Deliver', 'authors': 'Lee Moran', 'link': 'https://www.huffingtonpost.com/entry/dad-bullied-son-happy-birthday-wishes_us_59562059e4b05c37bb7d8c51', 'short_description': "Russell Crowe, Dionne Warwick, Chris Hadfield and Monica Lewinsky are among those who've responded so far.", 'date': '2017-06-30', 'index': 18621}, {'category': 'PARENTS', 'headline': '8 Reasons Your Kid Should Travel (Without You)', 'authors': 'Beth Markley, ContributorWriter', 'link': 'https://www.huffingtonpost.com/entry/8-reasons-your-kid-should-travel-without-you_us_58e97ce6e4b0acd784ca5931', 'short_description': 'The first time we sent our children on a trip without us (or any other relative), it was to a weeklong camp near a mountain', 'date': '2017-04-09', 'index': 18927}, {'category': 'PARENTS', 'headline': "Mom Explains Exactly Why Parents Should Thank Their Kids' Teachers", 'authors': 'Taylor Pittman', 'link': 'https://www.huffingtonpost.com/entry/mom-explains-exactly-why-parents-should-thank-their-kids-teachers_us_59ce77d3e4b05f005d341cb2', 'short_description': 'A nice reminder that teachers rule.', 'date': '2017-09-29', 'index': 18261}, {'category': 'BUSINESS', 'headline': 'Starbucks Offering Employees Free Legal Advice On Immigration', 'authors': "Lydia O'Connor", 'link': 'https://www.huffingtonpost.com/entry/starbucks-immigration-advice_us_589a22ace4b09bd304be3ad1', 'short_description': "The announcement comes shortly after the coffee company's CEO pledged to hire 10,000 refugees.", 'date': '2017-02-07', 'index': 32455}, {'category': 'THE WORLDPOST', 'headline': 'At Least Five Dead In Shooting At Mexico Music Festival', 'authors': 'Gabriel Stargardter, Reuters', 'link': 'https://www.huffingtonpost.com/entry/shooting-mexico-music-festival_us_587ccfe4e4b0e58057ff7fa3', 'short_description': 'Quintana Roo State Attorney General Miguel Angel Pech said 15 people were injured, of whom 7 were still in hospital. The state government said in a statement that one person was in grave condition.', 'date': '2017-01-16', 'index': 9972}, {'category': 'WEIRD NEWS', 'headline': "Burger King's 'Who Is The King?' Vote Reportedly Angers Belgian Royal", 'authors': 'Nina Golgowski', 'link': 'https://www.huffingtonpost.com/entry/burger-king-challenges-belgium-roya_us_592af371e4b053f2d2ad0015', 'short_description': "The advertising campaign playfully challenges King Philippe's reign as the company plans to expand abroad.", 'date': '2017-05-28', 'index': 33429}]
    priority=[{'category':'ENTERTAINMENT'},{'category':'CRIME'},{'category':'PARENTS'}]
    #result = recommendation.e_recommend(TAG_DATA, priority, NEWS_DATA)


    result = recommendation.i_recommend(TAG_DATA, history, NEWS_DATA)
    #print(result)

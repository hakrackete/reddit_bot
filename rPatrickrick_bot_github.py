
import praw
replycount = 0
reddit = praw.Reddit(client_id = 'as if i told ya',      # erschafft reddit instanz
                     client_secret = 'psst, it\'s a secret',
                     username = 'Patrick_bot',
                     password = '[redacted]',
                     user_agent = 'quotingbot')
subreddits = reddit.subreddit('historymemes+animemes+BikiniBottomTwitter+dankchristianmemes+dankmemesfromsite19+BokuNoMetaAcademia+bonehurtingjuice+comedycemetry+ComedyNecrophilia+comedyheaven+Memes_Of_The_Dank+terriblefacebookmemes+Showerthoughts+funny+HollowKnightMemes+itmayorbenotmaybeloss+leagueofmemes+me_irl+prequelmemes+dankmemes')   # erschafft subreddit instanz

while True:       #für dauerhaftes durchgehen
    for submission in subreddits.hot(limit=None):     #durchgehen durch submissions in einem subreddit , sortiert nach "hot"
        submission.comments.replace_more(limit=None)  # irgendwas, sodass man alle commentantworten aufrufen kann. Hab ich noch nicht ganz verstanden
        print('-----------------------------------------')
        print('currently on post:')
        print(submission.title)
        print('-----------------------------------------')
        for comment in submission.comments:       # geht durch erstcomments der jeweiligen submissions durch
                        
            names = []     # namensliste, um zu überprüfen, ob der bot bereits geantwortet hat
            
            for childcomment in comment.replies:  
                names.append(childcomment.author)      # ergänzung der namensliste um die autoren der antworten
                
            if  comment.body.lower().startswith('is this') and 'Patrick_bot' not in names[:]:   # antwortinstanz + feedback für mich
                try:
                    a = 21
                    comment.reply('No, This Is Patrick!')
                    
                except:
                    pass
                #print('reply was sent to:')
                #print('reddit.com' + comment.permalink)
                replycount += 1
                #print('replies for this run: ' + str(replycount))
            
            def a_process(comment, replycount):   # um sich durch alle antworten zu graben + aufrufen des parameters "comment"
                for comment in comment.replies:
                                
                    names = []
                    parent = comment.parent()
                    names.append(parent.author)
                    for childcomment in comment.replies:
                        names.append(childcomment.author)
                        
                    if  comment.body.lower().startswith('is this') and 'Patrick_bot' not in names[:]:
                        try:
                            comment.reply('No, This Is Patrick!')
                            replycount += 1
                            
                        except:
                            pass
                        #print('reply was sent to:')
                        #print('reddit.com' + comment.permalink)
                        #print('replies for this run: ' + str(replycount))
                    a_process(comment, replycount)  # der prozess geht durch jeden comment-verlauf und wiederholt sich


            a_process(comment,replycount)    

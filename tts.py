from gtts import gTTS
text1 = '''My husky.
Today I want to talk about my favourate friend-my pet, a husky.
Although my mum is always angry
at my husky after it destroyed our house,
but it is really a wonderful companion to me.
Once a time, my parents left me alone at home.
It was too late,it was dark.
I was too worried to do my homework.
At that moment,my husky seemed to know my worry,
it came to lick my fingers,
and took its favourate toy-a ball to let me play with it.
Then we have a good time.
At last,
I restarted to read my book while it put its head on my leg,
it made me calm down until my parents came back.
I love my husky,
it is not only a friend but a family to me.
I am very thankful to have my every enjoy moment with my husky.
I believe you will like it when you see it
That's all, Thank you!
        '''
text2 = '''
Protect the Ocean Protect Our Earth
It seens too far away from us to talk about protecting the Ocean.
But,we all know that the ocean is an important part of the earth,
and the earth is our common hometown.
And the ocean plays a very important role on the earth.
So It's as important to protect the ocean and protect the earth.
Therefore,how to protect the ocean?
I think everyone can do as these:
First of all,educating ourselves about oceans and warning others.
The more we learn about the ocean,
the more we will want to help
ensure its health-then share that knowledge to inspire others.
Change our mind,and take action.
Secondly, helping take care of the beach.
When we do something on the beach,
we can keep the beach clean without leaving any rubbish.
At the same time,
we can encourage others to respect the ocean by joining in local beach cleanups.
Then,there are so many things we can do to proteceting the ocean,
but the most important thing is taking action right now.
Time flies,don't wait!
OK,that's all.Thank you!
'''
tts = gTTS(text=text2, lang='en-uk')
tts.save("Ocean.mp3")

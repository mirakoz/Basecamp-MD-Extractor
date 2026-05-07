---
title: 'KeyShot | Performance Marketing: GTM Auth handling'
url: https://basecamp.com/2325709/projects/19095668/messages/111069048
author: Unknown
date: Unknown
type: basecamp-export
---

# KeyShot | Performance Marketing: GTM Auth handling

# [KeyShot | Performance Marketing](/2325709/projects/19095668)

KeyShot | Performance Marketing: GTM Auth handling

# just moved this page.

See it in its new location →

# just copied this page.

[Go back to the original](#)
or See it in its new location →

The client can’t see anything on this page

#### Are you sure you want to show this message and its comments to the client?

They’ll be able to see any comments that have been made so far and add their own.

# Message

Project: [KeyShot | Performance Marketing](/2325709/projects/19095668)

### GTM Auth handling

Posted by Josh Mings on Sep 10, 2025

[![Josh Mings](https://asset1.basecamp.com/2325709/people/18698286/photo/avatar.96.gif "Josh Mings")](/2325709/people/18698286)

Hi Fathy and Mucahit, I added some tags/triggers/variables to GTM to work around the limitation we have with tracking through the login page. Everything should be working but the tags on the account.keyshot.com side are not triggered.  
  
The premise here is to:  
1. Capture the start of the authorization (sign up or sign in)  
2. Set a cookie to keep the intent in place  
3. Capture the successful login  
  
It's looking at /login-callback path and token for a successful outcome, but /login-callback redirects and I'm not seeing a token passed along. I wanted to get your input. I imagine it's something simple I'm missing.  
  
Here's what is set up...  

Tags:

AWS Cognito auth\_start (sign in)

AWS Cognito auth\_start (sign up)

AWS Cognito auth\_success  
AWS Cognito auth\_error

AWS Cognito clear intent cookie

Triggers:

KeyShot Account Sign in button

KeyShot Account Sign up button  
Callback SUCCESS

Calback ERROR

User-Defined Variables:

JS – AuthMethod

JS – ErrorDescription

JS – Error

JS – HasError

JS – HasIdToken

JS – HasAuthCode

ks\_auth\_intent

#### Discuss this message

[![Fathy Elsayed](https://asset1.basecamp.com/2325709/people/18538829/photo/avatar.96.gif "Fathy Elsayed")](/2325709/people/18538829)

**Fathy Elsayed**   
Hi Josh,   
  
Thank you for setting up the GTM tags and triggers to handle authentication tracking.  
  
We will delve deeper into the flow to identify where the process might be failing. We will review the tags, triggers, and variables you've set up and get back to you with our findings as soon as possible.  
  
Best,  
Fathy

[Posted on Sep 10, 2025](/2325709/projects/19095668/messages/111069048#comment_959225425)

[![Josh Mings](https://asset1.basecamp.com/2325709/people/18698286/photo/avatar.96.gif "Josh Mings")](/2325709/people/18698286)

**Josh Mings**   
Thanks, Fathy. I think this would be huge and help us see more conversions get passed. I'm thinking it's an ID not being passed or a consent not set or interferring. I'll wait to hear from you though. Thanks again.

[Posted on Sep 10, 2025](/2325709/projects/19095668/messages/111069048#comment_959263227)

![](https://asset1.basecamp.com/people/19154717/photo/avatar.96.gif "Mirak Ozoglu")

Add a comment or upload a file…

[By-the-minute history for this message...](#)

---

## Comments

#### Discuss this message

[![Fathy Elsayed](https://asset1.basecamp.com/2325709/people/18538829/photo/avatar.96.gif "Fathy Elsayed")](/2325709/people/18538829)

**Fathy Elsayed**   
Hi Josh,   
  
Thank you for setting up the GTM tags and triggers to handle authentication tracking.  
  
We will delve deeper into the flow to identify where the process might be failing. We will review the tags, triggers, and variables you've set up and get back to you with our findings as soon as possible.  
  
Best,  
Fathy

[Posted on Sep 10, 2025](/2325709/projects/19095668/messages/111069048#comment_959225425)

[![Josh Mings](https://asset1.basecamp.com/2325709/people/18698286/photo/avatar.96.gif "Josh Mings")](/2325709/people/18698286)

**Josh Mings**   
Thanks, Fathy. I think this would be huge and help us see more conversions get passed. I'm thinking it's an ID not being passed or a consent not set or interferring. I'll wait to hear from you though. Thanks again.

[Posted on Sep 10, 2025](/2325709/projects/19095668/messages/111069048#comment_959263227)

![](https://asset1.basecamp.com/people/19154717/photo/avatar.96.gif "Mirak Ozoglu")

Add a comment or upload a file…
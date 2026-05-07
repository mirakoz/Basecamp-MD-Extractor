---
title: 'Green Group | PPC: [Urgent] Tracking Issue'
url: https://basecamp.com/2325709/projects/19130411/messages/110267354
author: Unknown
date: Unknown
type: basecamp-export
---

# Green Group | PPC: [Urgent] Tracking Issue

# [Green Group | PPC](/2325709/projects/19130411)

Green Group | PPC: [Urgent] Tracking Issue

# just moved this page.

See it in its new location →

# just copied this page.

[Go back to the original](#)
or See it in its new location →

The client can’t see anything on this page

#### Are you sure you want to show this message and its comments to the client?

They’ll be able to see any comments that have been made so far and add their own.

# Message

Project: [Green Group | PPC](/2325709/projects/19130411)

### [Urgent] Tracking Issue

Posted by Can Basaloglu on May 8, 2025

[![Can Basaloglu](https://asset1.basecamp.com/2325709/people/18232741/photo/avatar.96.gif "Can Basaloglu")](/2325709/people/18232741)

Hi Francisco,

We’ve identified tracking issues on the website. When checking GTM in preview mode, variables appear as undefined, which prevents certain conversions from being tracked. The same issue is also affecting Google Analytics.

This might be caused by having two different GTM containers on the website. We're currently using GTM-PHVN7ZQ, but it looks like GTM-PDR56SM is also active. If the client could remove GTM-PDR56SM, it may resolve the issue. Alternatively, if we can get access to GTM-PDR56SM, we could migrate our tags into that container.

Could you please take a look?

Let me know if you need any help. We're also happy to investigate directly if backend access can be granted.

Best,  
Can

[![](https://asset1.basecamp.com/2325709/projects/19130411/attachments/509859169/608f724a-2c26-11f0-84bd-0242ac110004/thumbnail.png)


Screenshot\_3.png

Project: Green Group | PPC

Added by Can B. on May 8, 2025
 · 

127 KB](https://asset1.basecamp.com/2325709/projects/19130411/attachments/509859169/Screenshot_3.png)

[26 comments](/2325709/projects/19130411/messages/110267354)

[Label...](#)

May 8, 2025

127 KB

Can B.

#### Discuss this message

[![Francisco Freyre](https://asset1.basecamp.com/2325709/people/18046896/photo/avatar.96.gif "Francisco Freyre")](/2325709/people/18046896)

**Francisco Freyre**   
Hello, thank you this.  
This is the response they got from the people taking care of the site:  

*I've just run a test through the Google Tag Assistant companion, and everything appears to be firing without error.*

*There are currently two tags on the dashboard, but we aren't able to discontinue either of them. When a website is created on the platform, the dashboard automatically associates a Google Tag Manager instance with it. This allows us to connect the dashboard's statistics section to Google Analytics and provides some additional functionality that allows us to expedite the website in search results. This is currently in place for all users of our website platform and has no effect on the secondary code added by the advisor.*

*It sounds like this might be an issue within Google Tag Manager itself. If you'd like, we can place a new Tag Manager instance on the website to rule out any errors from the previous one. We'd just need the team to generate that new property and provide it to us.*

Please let me know what's next.  
  
Thanks and regards

[Posted on May 9, 2025](/2325709/projects/19130411/messages/110267354#comment_951812143)

[![Can Basaloglu](https://asset1.basecamp.com/2325709/people/18232741/photo/avatar.96.gif "Can Basaloglu")](/2325709/people/18232741)

**Can Basaloglu**   
I don't think this will solve the issue but let's try it first. Below are the scripts for the new GTM container:  
  

<!-- Google Tag Manager -->

<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':

new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],

j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=

'[https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore…](https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f); "https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);")

})(window,document,'script','dataLayer','GTM-MSN87VHP');</script>

<!-- End Google Tag Manager -->  
  

<!-- Google Tag Manager (noscript) -->

<noscript><iframe src="<https://www.googletagmanager.com/ns.html?id=GTM-MSN87VHP>"

height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>

<!-- End Google Tag Manager (noscript) -->  
  
  
Please let me know once the code has been implement.  
  
Thank you!

[Posted on May 9, 2025](/2325709/projects/19130411/messages/110267354#comment_951816304)

[![Can Basaloglu](https://asset1.basecamp.com/2325709/people/18232741/photo/avatar.96.gif "Can Basaloglu")](/2325709/people/18232741)

**Can Basaloglu**   

I looked into the issue further, and it seems that our container ID is hard-coded into the website, while the other container is added through a Drupal module. This difference might be causing the conflict.

Because they’re loaded in different ways, they overwrite each other’s listeners.

Would it be possible to remove the hard-coded snippet and register our container ID through the same Drupal module that’s already adding the platform container? Loading both IDs with the same module should eliminate the conflict and restore accurate tracking.

[Posted on May 9, 2025](/2325709/projects/19130411/messages/110267354#comment_951816989)

[![Francisco Freyre](https://asset1.basecamp.com/2325709/people/18046896/photo/avatar.96.gif "Francisco Freyre")](/2325709/people/18046896)

**Francisco Freyre**   
Hello,   
  
I sent the email with the code and they responded before I received your lates comment.  
This is what he said:  
  

*The new code has now been added!*

*​To investigate this further, would you mind either sharing screenshots or a quick screen recording demonstrating which data isn't visible?*

Is the message you sent above about the hardcoded ID still valid so I send it to him?  
After the new code was added, do we continue to have problems?  
  
Thanks and regards

[Posted on May 9, 2025](/2325709/projects/19130411/messages/110267354#comment_951818172)

[![Can Basaloglu](https://asset1.basecamp.com/2325709/people/18232741/photo/avatar.96.gif "Can Basaloglu")](/2325709/people/18232741)

**Can Basaloglu**   

Hi,  
  
We’re experiencing the same issue with the new container. Here's a screenshot showing the problem, all variables are coming through as undefined.

This is actually the first time we've encountered something like this, so I suspect it might be related to how the GTM code is implemented through the Drupal module.  
  
Hope it helps. Thanks!

[Posted on May 9, 2025](/2325709/projects/19130411/messages/110267354#comment_951818475)

[![](https://asset1.basecamp.com/2325709/projects/19130411/attachments/509884159/96a26b0a-2c60-11f0-9b5c-0242ac110005/thumbnail.png)


Screenshot\_4.png

Project: Green Group | PPC

Added by Can B. on May 9, 2025
 · 

117 KB](https://asset1.basecamp.com/2325709/projects/19130411/attachments/509884159/Screenshot_4.png)

[26 comments](/2325709/projects/19130411/messages/110267354)

[Label...](#)

May 9, 2025

117 KB

Can B.

[![](https://asset1.basecamp.com/2325709/projects/19130411/attachments/509884160/b90457ee-2c60-11f0-a6ac-0242ac110004/thumbnail.png)


Screenshot\_5.png

Project: Green Group | PPC

Added by Can B. on May 9, 2025
 · 

133 KB](https://asset1.basecamp.com/2325709/projects/19130411/attachments/509884160/Screenshot_5.png)

[26 comments](/2325709/projects/19130411/messages/110267354)

[Label...](#)

May 9, 2025

133 KB

Can B.

[View all of these files at once](/2325709/projects/19130411/comments/951818475/image_attachments)
•
[Download all of these files](/2325709/attachment_exports?attachable_id=951818475&attachable_type=Comment)
Downloading...

[![Francisco Freyre](https://asset1.basecamp.com/2325709/people/18046896/photo/avatar.96.gif "Francisco Freyre")](/2325709/people/18046896)

**Francisco Freyre**   
Thank you!  
I just sent this to them and your explanation about the hard-coded info.  
I will let you know when he responds  
  
Regards

[Posted on May 9, 2025](/2325709/projects/19130411/messages/110267354#comment_951818652)

[![Francisco Freyre](https://asset1.basecamp.com/2325709/people/18046896/photo/avatar.96.gif "Francisco Freyre")](/2325709/people/18046896)

**Francisco Freyre**   
Hello,   
This is their response:   

*Appreciate all the context provided!*

*I've flagged this directly to our senior product engineer to investigate. Was this something that you previously had operational, and it recently broke, or is this getting configured for the first time?*

*Also, could you give our team permission to access the property? This will allow us to test in real time. Please send the permissions to**tylerb@snappkraken.com**.*

I don't understand what permissions he would like to get. Please let me know if you do and if we can grant access.   
  
Thanks and regards

[Posted on May 9, 2025](/2325709/projects/19130411/messages/110267354#comment_951877217)

[![Can Basaloglu](https://asset1.basecamp.com/2325709/people/18232741/photo/avatar.96.gif "Can Basaloglu")](/2325709/people/18232741)

**Can Basaloglu**   

Hi,

Yes, it was operational from the start of the project and remained so until last week.

They are requesting Google Tag Manager access to run tests on their side. With your approval, we can grant access, that would be the fastest way to resolve the issue, as we don’t have access to their backend.

Please let me know if you would like me to proceed with granting access.

Best,

[Posted on May 9, 2025](/2325709/projects/19130411/messages/110267354#comment_951878348)

[![Francisco Freyre](https://asset1.basecamp.com/2325709/people/18046896/photo/avatar.96.gif "Francisco Freyre")](/2325709/people/18046896)

**Francisco Freyre**   
Yes, please grant access.   
Let me know when it is ready  
  
Regards

[Posted on May 9, 2025](/2325709/projects/19130411/messages/110267354#comment_951879313)

[![Can Basaloglu](https://asset1.basecamp.com/2325709/people/18232741/photo/avatar.96.gif "Can Basaloglu")](/2325709/people/18232741)

**Can Basaloglu**   
An email with the @almcorp.com domain is also added to the property, could this be an issue, should we remove it before granting access?

[Posted on May 9, 2025](/2325709/projects/19130411/messages/110267354#comment_951880103)

[![Francisco Freyre](https://asset1.basecamp.com/2325709/people/18046896/photo/avatar.96.gif "Francisco Freyre")](/2325709/people/18046896)

**Francisco Freyre**   
If possible, yes  
Thanks

[Posted on May 9, 2025](/2325709/projects/19130411/messages/110267354#comment_951880421)

[![Can Basaloglu](https://asset1.basecamp.com/2325709/people/18232741/photo/avatar.96.gif "Can Basaloglu")](/2325709/people/18232741)

**Can Basaloglu**   
Okay, I’ve removed the email, but I’m unable to invite the provided email address. Please see the attached screenshot for more details.

[Posted on May 9, 2025](/2325709/projects/19130411/messages/110267354#comment_951882834)

[![](https://asset1.basecamp.com/2325709/projects/19130411/attachments/509923914/f4c47ba6-2d0f-11f0-8b61-0242ac110004/thumbnail.png)


Screenshot 2025-05-09.png

Project: Green Group | PPC

Added by Can B. on May 9, 2025
 · 

38 KB](https://asset1.basecamp.com/2325709/projects/19130411/attachments/509923914/Screenshot%202025-05-09.png)

[26 comments](/2325709/projects/19130411/messages/110267354)

[Label...](#)

May 9, 2025

38 KB

Can B.

[![Francisco Freyre](https://asset1.basecamp.com/2325709/people/18046896/photo/avatar.96.gif "Francisco Freyre")](/2325709/people/18046896)

**Francisco Freyre**   
Hello  
  
The correct email is: [tylerb@snappykraken.com](mailto:tylerb@snappykraken.com) (mailto:[tylerb@snappykraken.com](mailto:tylerb@snappykraken.com))  
  
Thank you

[Posted on May 9, 2025](/2325709/projects/19130411/messages/110267354#comment_951887327)

[![Can Basaloglu](https://asset1.basecamp.com/2325709/people/18232741/photo/avatar.96.gif "Can Basaloglu")](/2325709/people/18232741)

**Can Basaloglu**   

Hi,

Thank you for the correction. I've sent the invitation.

Best,  
Can

[Posted on May 9, 2025](/2325709/projects/19130411/messages/110267354#comment_951887631)

[![Francisco Freyre](https://asset1.basecamp.com/2325709/people/18046896/photo/avatar.96.gif "Francisco Freyre")](/2325709/people/18046896)

**Francisco Freyre**   
Thank you!

[Posted on May 9, 2025](/2325709/projects/19130411/messages/110267354#comment_951887702)

[![Francisco Freyre](https://asset1.basecamp.com/2325709/people/18046896/photo/avatar.96.gif "Francisco Freyre")](/2325709/people/18046896)

**Francisco Freyre**   
Hello,   
Just to let you know what they just wrote:  
  

*Quick update on this!*

*Upon investigation, our development team replicated this issue on a couple of our instances, and we're currently looking into a fix. I have a meeting scheduled with them on Wednesday and should have more to share then.*  
  
While they are working on this, what is the status of the campaign?   
Thanks and regards

[Posted on May 12, 2025](/2325709/projects/19130411/messages/110267354#comment_951999694)

[![Can Basaloglu](https://asset1.basecamp.com/2325709/people/18232741/photo/avatar.96.gif "Can Basaloglu")](/2325709/people/18232741)

**Can Basaloglu**   
Hi,  
  
Thank you for the update. I hope the issue can be resolved as soon as possible.   
  
The campaigns are still active, and we're able to track calls from ad extensions and lead form submissions (somehow thank-you page tracking is still working). However, we're currently unable to track click-based conversions.  
  
I wouldn’t recommend pausing the campaigns if the fix is expected soon. But if it looks like it will take another week or more, then we should definitely consider pausing them.  
Best,

[Posted on May 13, 2025](/2325709/projects/19130411/messages/110267354#comment_952000982)

[![Francisco Freyre](https://asset1.basecamp.com/2325709/people/18046896/photo/avatar.96.gif "Francisco Freyre")](/2325709/people/18046896)

**Francisco Freyre**   
Thank you for the quick response.   
I will not propose to suspend the campaign yet, let's see how they advance by Wednesday.   
I will keep you posted.  
Regards

[Posted on May 13, 2025](/2325709/projects/19130411/messages/110267354#comment_952001134)

[![Francisco Freyre](https://asset1.basecamp.com/2325709/people/18046896/photo/avatar.96.gif "Francisco Freyre")](/2325709/people/18046896)

**Francisco Freyre**   
Hello,   
Just to share the update they just sent:  
  
*I appreciate your patience as our team looks into the issue! Some additional work is being done to pinpoint the exact issue, and they'll be attempting to make a hotfix to fix the existing instances. Unfortunately, there's no workaround for the error at the moment, but as soon as there is movement, I'll let you know.*  
  
Is there something we can suggest or just wait?  
  
Thanks and regards

[Posted on May 14, 2025](/2325709/projects/19130411/messages/110267354#comment_952181461)

[![Can Basaloglu](https://asset1.basecamp.com/2325709/people/18232741/photo/avatar.96.gif "Can Basaloglu")](/2325709/people/18232741)

**Can Basaloglu**   

Hi,

If they agree, we can ask them to add our tags, triggers, and variables to their own GTM container until the issue is resolved. Since they already have access to our container, they can simply export our setup and import it into theirs. In the meantime, we can pause the tags in our container.

If that's not possible, unfortunately, we have no other option but to wait. For now, we can still track lead form submissions and calls made through call extensions.

Best,

[Posted on May 14, 2025](/2325709/projects/19130411/messages/110267354#comment_952183098)

[![Francisco Freyre](https://asset1.basecamp.com/2325709/people/18046896/photo/avatar.96.gif "Francisco Freyre")](/2325709/people/18046896)

**Francisco Freyre**   
Thank you,   
I have already passed the message.   
I will let you know what they respond.  
  
Regards

[Posted on May 15, 2025](/2325709/projects/19130411/messages/110267354#comment_952186245)

[![Francisco Freyre](https://asset1.basecamp.com/2325709/people/18046896/photo/avatar.96.gif "Francisco Freyre")](/2325709/people/18046896)

**Francisco Freyre**   
Hello,   
  
The client asked if we should pause the campaign. I already responded what you indicated before about keeping it unless it is not a fast solution.  
  
The tech guy responded this afterwards:  

*Most of the basic functionality is still operational, but it seems the triggers specifically are having issues loading. We were able to replicate this with our tag properties loaded by Drupal, so it won't be possible for us to add your tags, triggers, and variables to our version of GTM.*

*​We've had a couple of our developers working on this, who are currently reviewing older code to rule out if this is an issue with Tag Manager itself or our specific instance. As an official fix hasn't been identified yet, I'd recommend pausing the campaigns if the click conversations are essential for your tracking.*  
  
What do you think?

Thanks

[Posted on May 15, 2025](/2325709/projects/19130411/messages/110267354#comment_952190748)

[![Can Basaloglu](https://asset1.basecamp.com/2325709/people/18232741/photo/avatar.96.gif "Can Basaloglu")](/2325709/people/18232741)

**Can Basaloglu**   
Hi,  
  
If the developers are actively working on it, I believe we’ll have an update soon. In the meantime, we can keep the campaigns running, maybe with a reduced budget.  
  
If they can fix it, there’s nothing to worry about. If not, we’ll need to find an alternative solution anyway. We’re already able to track calls and lead form submissions. We can also set up website call tracking in addition to those, but it will need to be tested first.  
  
Best,

[Posted on May 15, 2025](/2325709/projects/19130411/messages/110267354#comment_952209068)

[![Francisco Freyre](https://asset1.basecamp.com/2325709/people/18046896/photo/avatar.96.gif "Francisco Freyre")](/2325709/people/18046896)

**Francisco Freyre**   
Hello,   
  
This is what they just sent:  
  
*Our Product team pushed a fix this morning that we think should take care of the issue. When you get a chance, can you check on your end and let us know if everything looks good?*  
  
Please let me know if it is working or not.  
Thanks and regards

[Posted on May 16, 2025](/2325709/projects/19130411/messages/110267354#comment_952344684)

[![Can Basaloglu](https://asset1.basecamp.com/2325709/people/18232741/photo/avatar.96.gif "Can Basaloglu")](/2325709/people/18232741)

**Can Basaloglu**   

Hi,

I just tested our conversions, and everything is working fine.

Best,

[Posted on May 16, 2025](/2325709/projects/19130411/messages/110267354#comment_952349553)

[![Francisco Freyre](https://asset1.basecamp.com/2325709/people/18046896/photo/avatar.96.gif "Francisco Freyre")](/2325709/people/18046896)

**Francisco Freyre**   
Perfect!   
Thank you so much.   
Have a great weekend   
Regards

[Posted on May 16, 2025](/2325709/projects/19130411/messages/110267354#comment_952352469)

![](https://asset1.basecamp.com/people/19154717/photo/avatar.96.gif "Mirak Ozoglu")

Add a comment or upload a file…

[By-the-minute history for this message...](#)

---

## Comments

26 comments
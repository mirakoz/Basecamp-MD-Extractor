---
title: 'BlueChameleonInvestigations-Local SEO & PPC: Website Conversion Tracking'
url: https://basecamp.com/2325709/projects/19887717/todos/506692988
author: Unknown
date: Unknown
type: basecamp-export
---

# BlueChameleonInvestigations-Local SEO & PPC: Website Conversion Tracking

# [BlueChameleonInvestigations-Local SEO & PPC](/2325709/projects/19887717)

BlueChameleonInvestigations-Local SEO & PPC: Website Conversion Tracking

# just moved this page.

See it in its new location →

# just copied this page.

[Go back to the original](#)
or See it in its new location →

# To-do item

Project: [BlueChameleonInvestigations-Local SEO & PPC](/2325709/projects/19887717)

From the to-do list:
[Pending Items & Updates](/2325709/projects/19887717/todolists/71133208)

* [Website Conversion Tracking](/2325709/projects/19887717/todos/506692988)
  Website Conversion Tracking

  [7 comments](/2325709/projects/19887717/todos/506692988)

  (Completed by Can Basaloglu on 21 May)

#### Discuss this to-do

[![Can Basaloglu](https://asset1.basecamp.com/2325709/people/18232741/photo/avatar.96.gif "Can Basaloglu")](/2325709/people/18232741)

**Can Basaloglu**   

Hi Luciana,

I've noticed an issue with the "SEND US A MESSAGE" button on the homepage and the "CONTACT" button at the bottom of every page. They are currently redirect to <http://trustbci.com/contact> instead of the secure version, <https://trustbci.com/contact>. I could have changed it myself, but since I’m not a web expert, I didn’t want to risk causing issues. I've attached a screenshot for reference.

Additionally, we’re unable to see the traffic source for form submissions. The current setup only shows the page URL without any UTM parameters. It would be helpful if the client could either add hidden input fields for utm\_source, utm\_medium, etc., or use a different plugin or addon that captures this data. This information is important for both us and the client to track which leads are coming from ads and assess their quality. I’ve attached a screenshot showing the issue I’m referring to.

Please let me know if you need any clarification.

Best,

Can

[Posted on Apr 11, 2025, updated 14 minutes later](/2325709/projects/19887717/todos/506692988#comment_950126475)

[![](https://asset1.basecamp.com/2325709/projects/19887717/attachments/508839575/192b3652-16d0-11f0-bf8a-0242ac110005/thumbnail.png)


Screenshot\_3.png

Project: BlueChameleonInvestigations-Local SEO & PPC

Added by Can B. on Apr 11, 2025
 · 

796 KB](https://asset1.basecamp.com/2325709/projects/19887717/attachments/508839575/Screenshot_3.png)

[7 comments](/2325709/projects/19887717/todos/506692988)

[Label...](#)

Apr 11, 2025

796 KB

Can B.

[![](https://asset1.basecamp.com/2325709/projects/19887717/attachments/508840516/6b11c826-16dc-11f0-86b8-0242ac110005/thumbnail.png)


Screenshot\_9.png

Project: BlueChameleonInvestigations-Local SEO & PPC

Added by Can B. on Apr 11, 2025
 · 

81 KB](https://asset1.basecamp.com/2325709/projects/19887717/attachments/508840516/Screenshot_9.png)

[7 comments](/2325709/projects/19887717/todos/506692988)

[Label...](#)

Apr 11, 2025

81 KB

Can B.

[![](https://asset1.basecamp.com/2325709/projects/19887717/attachments/508840517/711b7e56-16dc-11f0-a4cd-0242ac110005/thumbnail.png)


Screenshot\_8.png

Project: BlueChameleonInvestigations-Local SEO & PPC

Added by Can B. on Apr 11, 2025
 · 

105 KB](https://asset1.basecamp.com/2325709/projects/19887717/attachments/508840517/Screenshot_8.png)

[7 comments](/2325709/projects/19887717/todos/506692988)

[Label...](#)

Apr 11, 2025

105 KB

Can B.

[View all of these files at once](/2325709/projects/19887717/comments/950126475/image_attachments)
•
[Download all of these files](/2325709/attachment_exports?attachable_id=950126475&attachable_type=Comment)
Downloading...

[![Luciana Salanitri](https://asset1.basecamp.com/2325709/people/18974264/photo/avatar.96.gif "Luciana Salanitri")](/2325709/people/18974264)

**Luciana Salanitri**   
Let me ask the client!

[Posted on Apr 11, 2025](/2325709/projects/19887717/todos/506692988#comment_950159084)

[![Luciana Salanitri](https://asset1.basecamp.com/2325709/people/18974264/photo/avatar.96.gif "Luciana Salanitri")](/2325709/people/18974264)

**Luciana Salanitri**   
Hi Can, the first URL should be corrected now.   
  
Regarding the UTMs, this is what she answered:

Hope you had a good weekend! I just downloaded HandL UTM
Grabber, installed, and activated it on WordPress.

Does she need to do anything else?

[Posted on Apr 15, 2025](/2325709/projects/19887717/todos/506692988#comment_950284661)

[![Can Basaloglu](https://asset1.basecamp.com/2325709/people/18232741/photo/avatar.96.gif "Can Basaloglu")](/2325709/people/18232741)

**Can Basaloglu**   
Hi Luciana,  
  
The URL looks good, thank you.

However, the contact form still needs to be configured to include hidden fields, as it currently doesn’t collect any UTM data.

Once the hidden fields are added, a JavaScript snippet will be needed to capture and populate the UTM values.

  
Please let me know if you need any clarification.  
  
Best,  
Can

[Posted on Apr 15, 2025](/2325709/projects/19887717/todos/506692988#comment_950345056)

[![Luciana Salanitri](https://asset1.basecamp.com/2325709/people/18974264/photo/avatar.96.gif "Luciana Salanitri")](/2325709/people/18974264)

**Luciana Salanitri**   
Oh, that's weird, I see in their video that the hidden fields should be added automatically: <https://utmgrabber.com/the-most-effective-utm-tracking-in-gravity-form/>.   
  
Regarding the JavaScript snippet, how is that implemented? Never did it before, tks

[Posted on Apr 15, 2025](/2325709/projects/19887717/todos/506692988#comment_950358676)

[![Can Basaloglu](https://asset1.basecamp.com/2325709/people/18232741/photo/avatar.96.gif "Can Basaloglu")](/2325709/people/18232741)

**Can Basaloglu**   
That's because the video uses Gravity Forms as an example. However BCI doesn't use a contact form plugin. Instead, the contact form is added via Jetpack using the block editor, directly within the pages.  
  
Javascript needs to be added to the footer section, the web dev should know how to do that.

[Posted on Apr 16, 2025](/2325709/projects/19887717/todos/506692988#comment_950363935)

[![Luciana Salanitri](https://asset1.basecamp.com/2325709/people/18974264/photo/avatar.96.gif "Luciana Salanitri")](/2325709/people/18974264)

**Luciana Salanitri**   
Oh, ok. I told her, but they don't have a web dev. My client is who is building the website. She knows how to work with these platforms like WP, but not so much in detail. I'll see if she knows how to do this.

[Posted on Apr 16, 2025](/2325709/projects/19887717/todos/506692988#comment_950365396)

[![Can Basaloglu](https://asset1.basecamp.com/2325709/people/18232741/photo/avatar.96.gif "Can Basaloglu")](/2325709/people/18232741)

**Can Basaloglu** completed the to-do

on May 21, 2025

![](https://asset1.basecamp.com/people/19154717/photo/avatar.96.gif "Mirak Ozoglu")

Add a comment or upload a file…

[By-the-minute history for this to-do...](#)

[Delete…](#)

[Delete this to-do?](/2325709/projects/19887717/todos/506692988/trash)
[Never mind](#)

---

## Comments

[7 comments](/2325709/projects/19887717/todos/506692988)
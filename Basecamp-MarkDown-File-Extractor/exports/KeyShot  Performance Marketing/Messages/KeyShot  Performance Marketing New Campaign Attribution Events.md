---
title: 'KeyShot | Performance Marketing: New Campaign Attribution Events'
url: https://basecamp.com/2325709/projects/19095668/messages/112088722
author: Unknown
date: Unknown
type: basecamp-export
---

# KeyShot | Performance Marketing: New Campaign Attribution Events

# [KeyShot | Performance Marketing](/2325709/projects/19095668)

KeyShot | Performance Marketing: New Campaign Attribution Events

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

### New Campaign Attribution Events

Posted by Josh Mings on Feb 12

[![Josh Mings](https://asset1.basecamp.com/2325709/people/18698286/photo/avatar.96.gif "Josh Mings")](/2325709/people/18698286)

Hi Fathy, you'll see some tags/triggers/variables for two new events in GTM under the Campaign Attribution folder. Dev is sending two events, campaign\_attribution and user\_email\_captured, across the Congnito signin/up form. And I've got it captured in GTM!! But that's not all, because of that, we can capture it in GA4 and HubSpot. You'll can see some testing in GA4 and HubSpot staging. It's currently on the dev staging site. I'll be testing over the next few days and then it will roll out to production.  
  
This will connect some dots we've been missing for campaign activity. I'll want you to review the GTM setup once I get the next set of testing started. I'll let you know when that is ready. In the meantime, let me know if you have any questions/concerns.  
  
Josh

#### Discuss this message

[![Fathy Elsayed](https://asset1.basecamp.com/2325709/people/18538829/photo/avatar.96.gif "Fathy Elsayed")](/2325709/people/18538829)

**Fathy Elsayed**   

Hi Josh, thanks for the update. This is a great step forward. Capturing both events at the sign-in/sign-up level should really help.

Let me know when testing is ready on your side.

Best,

Fathy

[Posted on Feb 12](/2325709/projects/19095668/messages/112088722#comment_967921385)

[![Josh Mings](https://asset1.basecamp.com/2325709/people/18698286/photo/avatar.96.gif "Josh Mings")](/2325709/people/18698286)

**Josh Mings**   
Hey Fathy, all done. Everything is in the GTM Campaign Attribution folder. I was able to get the *user\_email\_captured* event separated from the *campaign\_attribution* event, so the related tags are not firing and sending two submissions to HubSpot. The scripts in the tags are configured for HubSpot staging, but I'll update them for production once dev deploys the updates to production.  
  
These events will initially be sent from dev-managed sites that go to the login, i.e. account.keyshot.com, trial.keyshot.com, drive.keyshot.com. If people go to the login page from [www.keyshot.com](http://www.keyshot.com) (clicking Sign in, or Buy now), the events will currently not be sent. That will come later.  
  
Have a look and let me know if you catch anything that could be improved or that I missed.  
  
Thanks again,  
Josh

[Posted on Feb 14](/2325709/projects/19095668/messages/112088722#comment_968016240)

[![Fathy Elsayed](https://asset1.basecamp.com/2325709/people/18538829/photo/avatar.96.gif "Fathy Elsayed")](/2325709/people/18538829)

**Fathy Elsayed**   
Hi Josh, thank you for the detailed update. We’ll test everything and get back to you.

[Posted on Feb 14](/2325709/projects/19095668/messages/112088722#comment_968017176)

[![Josh Mings](https://asset1.basecamp.com/2325709/people/18698286/photo/avatar.96.gif "Josh Mings")](/2325709/people/18698286)

**Josh Mings**   
One thing we may need to do is prevent those tags from firing on the staging sites, so we don't get any test data into the production sites once it's live. The staging sites include:  
  
<https://staging.keyshot.com>  
<https://staging-account.keyshot.com/>  
<https://staging-drive.keyshot.com/>  
<https://staging-webviewer.keyshot.com/>

[Posted on Feb 16](/2325709/projects/19095668/messages/112088722#comment_968065603)

[![Fathy Elsayed](https://asset1.basecamp.com/2325709/people/18538829/photo/avatar.96.gif "Fathy Elsayed")](/2325709/people/18538829)

**Fathy Elsayed**   
Noted. We’ll block those tags on the staging domains (via hostname rules in GTM).

[Posted on Feb 16](/2325709/projects/19095668/messages/112088722#comment_968066807)

[![Josh Mings](https://asset1.basecamp.com/2325709/people/18698286/photo/avatar.96.gif "Josh Mings")](/2325709/people/18698286)

**Josh Mings**   
Ok, we're live! Those events are only firing on traffic from account.keyshot.com. I'm not seeing utm's passed. However, the user email is still set, which is capturing the ad activity *prior* to signing up. We're now getting source data and ip data, which allows us to set the country.  
  
In the image attached, previously, the Country would have been mostly empty, and all the Record Source Integration would have had Original and Latest Source of Integration.

[Posted on Feb 19](/2325709/projects/19095668/messages/112088722#comment_968312432)

[![](https://asset1.basecamp.com/2325709/projects/19095668/attachments/520230333/7c839b02-0dc6-11f1-9992-0242ac120003/thumbnail.png)


Screenshot 2026-02-19 130409.png

Project: KeyShot | Performance Marketing

Added by Josh M. on Feb 19
 · 

567 KB](https://asset1.basecamp.com/2325709/projects/19095668/attachments/520230333/Screenshot%202026-02-19%20130409.png)

[10 comments](/2325709/projects/19095668/messages/112088722)

[Label...](#)

Feb 19

567 KB

Josh M.

[![Fathy Elsayed](https://asset1.basecamp.com/2325709/people/18538829/photo/avatar.96.gif "Fathy Elsayed")](/2325709/people/18538829)

**Fathy Elsayed**   

Hi Josh, thanks for the update — this is a great step forward.

We’ve updated the GTM tags to exclude the staging domains as discussed. We’ll run tests on our end to confirm the data is flowing as expected and will get back to you with any feedback or fixes, especially around the UTM passing.

[Posted on Feb 19](/2325709/projects/19095668/messages/112088722#comment_968317836)

[![Josh Mings](https://asset1.basecamp.com/2325709/people/18698286/photo/avatar.96.gif "Josh Mings")](/2325709/people/18698286)

**Josh Mings**   
Thanks, Fathy, I checked this morning and looks like the automated tests on staging are still coming through. Can you check the GTM setup? Here's the URL that shows the form submission.  
  
<https://staging-account.keyshot.com/account-settings>

[Posted on Feb 23](/2325709/projects/19095668/messages/112088722#comment_968439639)

[![](https://asset1.basecamp.com/2325709/projects/19095668/attachments/520312622/f92277be-10c8-11f1-b93e-0242ac120003/thumbnail.png)


Screenshot 2026-02-23 090417.png

Project: KeyShot | Performance Marketing

Added by Josh M. on Feb 23
 · 

422 KB](https://asset1.basecamp.com/2325709/projects/19095668/attachments/520312622/Screenshot%202026-02-23%20090417.png)

[10 comments](/2325709/projects/19095668/messages/112088722)

[Label...](#)

Feb 23

422 KB

Josh M.

[![Fathy Elsayed](https://asset1.basecamp.com/2325709/people/18538829/photo/avatar.96.gif "Fathy Elsayed")](/2325709/people/18538829)

**Fathy Elsayed**   
Hi Josh, I updated the tags with a second layer of URL exclusion for the mentioned URL and similar ones.

[Posted on Feb 23](/2325709/projects/19095668/messages/112088722#comment_968444887)

[![Josh Mings](https://asset1.basecamp.com/2325709/people/18698286/photo/avatar.96.gif "Josh Mings")](/2325709/people/18698286)

**Josh Mings**   
Awesome. Thanks, Fathy.

[Posted on Feb 23](/2325709/projects/19095668/messages/112088722#comment_968445253)

![](https://asset1.basecamp.com/people/19154717/photo/avatar.96.gif "Mirak Ozoglu")

Add a comment or upload a file…

[By-the-minute history for this message...](#)

---

## Comments

#### Discuss this message

[![Fathy Elsayed](https://asset1.basecamp.com/2325709/people/18538829/photo/avatar.96.gif "Fathy Elsayed")](/2325709/people/18538829)

**Fathy Elsayed**   

Hi Josh, thanks for the update. This is a great step forward. Capturing both events at the sign-in/sign-up level should really help.

Let me know when testing is ready on your side.

Best,

Fathy

[Posted on Feb 12](/2325709/projects/19095668/messages/112088722#comment_967921385)

[![Josh Mings](https://asset1.basecamp.com/2325709/people/18698286/photo/avatar.96.gif "Josh Mings")](/2325709/people/18698286)

**Josh Mings**   
Hey Fathy, all done. Everything is in the GTM Campaign Attribution folder. I was able to get the *user\_email\_captured* event separated from the *campaign\_attribution* event, so the related tags are not firing and sending two submissions to HubSpot. The scripts in the tags are configured for HubSpot staging, but I'll update them for production once dev deploys the updates to production.  
  
These events will initially be sent from dev-managed sites that go to the login, i.e. account.keyshot.com, trial.keyshot.com, drive.keyshot.com. If people go to the login page from [www.keyshot.com](http://www.keyshot.com) (clicking Sign in, or Buy now), the events will currently not be sent. That will come later.  
  
Have a look and let me know if you catch anything that could be improved or that I missed.  
  
Thanks again,  
Josh

[Posted on Feb 14](/2325709/projects/19095668/messages/112088722#comment_968016240)

[![Fathy Elsayed](https://asset1.basecamp.com/2325709/people/18538829/photo/avatar.96.gif "Fathy Elsayed")](/2325709/people/18538829)

**Fathy Elsayed**   
Hi Josh, thank you for the detailed update. We’ll test everything and get back to you.

[Posted on Feb 14](/2325709/projects/19095668/messages/112088722#comment_968017176)

[![Josh Mings](https://asset1.basecamp.com/2325709/people/18698286/photo/avatar.96.gif "Josh Mings")](/2325709/people/18698286)

**Josh Mings**   
One thing we may need to do is prevent those tags from firing on the staging sites, so we don't get any test data into the production sites once it's live. The staging sites include:  
  
<https://staging.keyshot.com>  
<https://staging-account.keyshot.com/>  
<https://staging-drive.keyshot.com/>  
<https://staging-webviewer.keyshot.com/>

[Posted on Feb 16](/2325709/projects/19095668/messages/112088722#comment_968065603)

[![Fathy Elsayed](https://asset1.basecamp.com/2325709/people/18538829/photo/avatar.96.gif "Fathy Elsayed")](/2325709/people/18538829)

**Fathy Elsayed**   
Noted. We’ll block those tags on the staging domains (via hostname rules in GTM).

[Posted on Feb 16](/2325709/projects/19095668/messages/112088722#comment_968066807)

[![Josh Mings](https://asset1.basecamp.com/2325709/people/18698286/photo/avatar.96.gif "Josh Mings")](/2325709/people/18698286)

**Josh Mings**   
Ok, we're live! Those events are only firing on traffic from account.keyshot.com. I'm not seeing utm's passed. However, the user email is still set, which is capturing the ad activity *prior* to signing up. We're now getting source data and ip data, which allows us to set the country.  
  
In the image attached, previously, the Country would have been mostly empty, and all the Record Source Integration would have had Original and Latest Source of Integration.

[Posted on Feb 19](/2325709/projects/19095668/messages/112088722#comment_968312432)

[![](https://asset1.basecamp.com/2325709/projects/19095668/attachments/520230333/7c839b02-0dc6-11f1-9992-0242ac120003/thumbnail.png)


Screenshot 2026-02-19 130409.png

Project: KeyShot | Performance Marketing

Added by Josh M. on Feb 19
 · 

567 KB](https://asset1.basecamp.com/2325709/projects/19095668/attachments/520230333/Screenshot%202026-02-19%20130409.png)

[10 comments](/2325709/projects/19095668/messages/112088722)

[Label...](#)

Feb 19

567 KB

Josh M.

[![Fathy Elsayed](https://asset1.basecamp.com/2325709/people/18538829/photo/avatar.96.gif "Fathy Elsayed")](/2325709/people/18538829)

**Fathy Elsayed**   

Hi Josh, thanks for the update — this is a great step forward.

We’ve updated the GTM tags to exclude the staging domains as discussed. We’ll run tests on our end to confirm the data is flowing as expected and will get back to you with any feedback or fixes, especially around the UTM passing.

[Posted on Feb 19](/2325709/projects/19095668/messages/112088722#comment_968317836)

[![Josh Mings](https://asset1.basecamp.com/2325709/people/18698286/photo/avatar.96.gif "Josh Mings")](/2325709/people/18698286)

**Josh Mings**   
Thanks, Fathy, I checked this morning and looks like the automated tests on staging are still coming through. Can you check the GTM setup? Here's the URL that shows the form submission.  
  
<https://staging-account.keyshot.com/account-settings>

[Posted on Feb 23](/2325709/projects/19095668/messages/112088722#comment_968439639)

[![](https://asset1.basecamp.com/2325709/projects/19095668/attachments/520312622/f92277be-10c8-11f1-b93e-0242ac120003/thumbnail.png)


Screenshot 2026-02-23 090417.png

Project: KeyShot | Performance Marketing

Added by Josh M. on Feb 23
 · 

422 KB](https://asset1.basecamp.com/2325709/projects/19095668/attachments/520312622/Screenshot%202026-02-23%20090417.png)

[10 comments](/2325709/projects/19095668/messages/112088722)

[Label...](#)

Feb 23

422 KB

Josh M.

[![Fathy Elsayed](https://asset1.basecamp.com/2325709/people/18538829/photo/avatar.96.gif "Fathy Elsayed")](/2325709/people/18538829)

**Fathy Elsayed**   
Hi Josh, I updated the tags with a second layer of URL exclusion for the mentioned URL and similar ones.

[Posted on Feb 23](/2325709/projects/19095668/messages/112088722#comment_968444887)

[![Josh Mings](https://asset1.basecamp.com/2325709/people/18698286/photo/avatar.96.gif "Josh Mings")](/2325709/people/18698286)

**Josh Mings**   
Awesome. Thanks, Fathy.

[Posted on Feb 23](/2325709/projects/19095668/messages/112088722#comment_968445253)

![](https://asset1.basecamp.com/people/19154717/photo/avatar.96.gif "Mirak Ozoglu")

Add a comment or upload a file…
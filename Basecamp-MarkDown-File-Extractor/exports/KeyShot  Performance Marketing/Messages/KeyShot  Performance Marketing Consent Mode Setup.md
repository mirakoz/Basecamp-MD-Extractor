---
title: 'KeyShot | Performance Marketing: Consent Mode Setup'
url: https://basecamp.com/2325709/projects/19095668/messages/108024947
author: Unknown
date: Unknown
type: basecamp-export
---

# KeyShot | Performance Marketing: Consent Mode Setup

# [KeyShot | Performance Marketing](/2325709/projects/19095668)

KeyShot | Performance Marketing: Consent Mode Setup

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

### Consent Mode Setup

Posted by Josh Mings on Jun 28, 2024

[![Josh Mings](https://asset1.basecamp.com/2325709/people/18698286/photo/avatar.96.gif "Josh Mings")](/2325709/people/18698286)

Hi Burak and Fathy, I thought I messaged about this but not finding it. Can you assist in setting up consent mode alongside GTM and HubSpot on keyshot.com please. Here are some references:  
  
<https://developers.google.com/tag-platform/security/guides/consent>  
[https://knowledge.hubspot.com/privacy-and-consent/support-google-consent-mo…](https://knowledge.hubspot.com/privacy-and-consent/support-google-consent-mode-v2#external-site "https://knowledge.hubspot.com/privacy-and-consent/support-google-consent-mode-v2#external-site")  
[https://developers.hubspot.com/docs/api/events/implement-google-consent-mod…](https://developers.hubspot.com/docs/api/events/implement-google-consent-mode "https://developers.hubspot.com/docs/api/events/implement-google-consent-mode")  
  
Please note the following:  
- We have a banner for EU/EEA/UK set up in HubSpot and active  
- We already have GTM installed on the keyshot.com domain  
  
Here is a link to the banners in HubSpot:  
[https://app.hubspot.com/settings/2757257/data-privacy/cookies-v2/0/policies…](https://app.hubspot.com/settings/2757257/data-privacy/cookies-v2/0/policies/www.keyshot.com "https://app.hubspot.com/settings/2757257/data-privacy/cookies-v2/0/policies/www.keyshot.com")  
  
The Consent mode setup is straightforward enough but I'm not sure how you prefer to add it (or if you've done so already in GTM). Please let me know how you go about adding it, when it is active, or if you need any other information.  
  
Thank you,  
Josh

#### Discuss this message

[![Fathy Elsayed](https://asset1.basecamp.com/2325709/people/18538829/photo/avatar.96.gif "Fathy Elsayed")](/2325709/people/18538829)

**Fathy Elsayed**   
Hi Josh, thanks for the references. let us initiate the setup process and get back to you with what exactly is needed to get this done.   
  
Regards,  
Fathy

[Posted on Jun 28, 2024](/2325709/projects/19095668/messages/108024947#comment_930552622)

[![Mucahit Yilmaz](https://asset1.basecamp.com/2325709/people/18561789/photo/avatar.96.gif "Mucahit Yilmaz")](/2325709/people/18561789)

**Mucahit Yilmaz**   

Hi Josh,

Can you complete the integration steps for GA4 and GTM on this page? [https://app.hubspot.com/settings/2757257/website/pages/all-domains/integrat…](https://app.hubspot.com/settings/2757257/website/pages/all-domains/integrations "https://app.hubspot.com/settings/2757257/website/pages/all-domains/integrations")

Our account doesn't have access to this setting.

For reference [https://knowledge.hubspot.com/privacy-and-consent/support-google-consent-mo…](https://knowledge.hubspot.com/privacy-and-consent/support-google-consent-mode-v2#external-site:~:text=and%20UK%20countries.-,Integrate,-with%20Google%20Analytics "https://knowledge.hubspot.com/privacy-and-consent/support-google-consent-mode-v2#external-site:~:text=and%20UK%20countries.-,Integrate,-with%20Google%20Analytics")

Thank you,

Mucahit

[Posted on Jul 1, 2024](/2325709/projects/19095668/messages/108024947#comment_930662101)

[![Josh Mings](https://asset1.basecamp.com/2325709/people/18698286/photo/avatar.96.gif "Josh Mings")](/2325709/people/18698286)

**Josh Mings**   
Done.

[Posted on Jul 1, 2024](/2325709/projects/19095668/messages/108024947#comment_930681628)

[![Mucahit Yilmaz](https://asset1.basecamp.com/2325709/people/18561789/photo/avatar.96.gif "Mucahit Yilmaz")](/2325709/people/18561789)

**Mucahit Yilmaz**   
It seems we need to update the GTM JavaScript code to continue with this setup. Can you update this code using the instructions found here? [https://developers.hubspot.com/docs/api/events/implement-google-consent-mod…](https://developers.hubspot.com/docs/api/events/implement-google-consent-mode "https://developers.hubspot.com/docs/api/events/implement-google-consent-mode")   
Specifically, refer to the section titled "Implement advanced Google consent mode v2 manually."  
  
I ask for advanced setup and not the basic one because if I understand correctly, using the basic setup might result in losing some data sent to Google products like GA4 or Ads. Under title "Implement advanced Google consent mode v2 manually" it says "When you implement consent mode on your website or app in advanced mode, Google tags are always loaded. Default consent is set (typically to denied) using the Consent Mode API. While consent is denied, Google tags will send cookieless pings. When the user interacts with the HubSpot cookie banner, the consent state updates. If consent is granted, Google tags send full measurement data. "

[Posted on Jul 3, 2024](/2325709/projects/19095668/messages/108024947#comment_930869075)

[![Josh Mings](https://asset1.basecamp.com/2325709/people/18698286/photo/avatar.96.gif "Josh Mings")](/2325709/people/18698286)

**Josh Mings**   
Hi Mucahit, I'm really looking to you and ALM's expertise here. I can update it but I would need to investigate all the tags and configuration you have set up in GTM and GA4. You and the team are familiar with that already. We already have GTM across the site so it's just a matter of adding the consent capture and listener.  We're using HubSpot for the consent banner but I would reference the Google docs on implementing this to ensure it's done correctly.  
  
<https://developers.google.com/tag-platform/security/guides/consent>

[Posted on Jul 4, 2024](/2325709/projects/19095668/messages/108024947#comment_930921024)

[![Mucahit Yilmaz](https://asset1.basecamp.com/2325709/people/18561789/photo/avatar.96.gif "Mucahit Yilmaz")](/2325709/people/18561789)

**Mucahit Yilmaz**   

Sure Josh, we are looking into it. We've added the listener and set up the default consent in the European Economic Area yesterday. We are now working on updating the consent.

[Posted on Jul 5, 2024](/2325709/projects/19095668/messages/108024947#comment_930980640)

[![Mucahit Yilmaz](https://asset1.basecamp.com/2325709/people/18561789/photo/avatar.96.gif "Mucahit Yilmaz")](/2325709/people/18561789)

**Mucahit Yilmaz**   
Hi Josh, setup is completed and published on gtm. We've updated consent settings for meta, linkedin, reddit, pinterest tags as well. Attached screenshot shows tags we didn't updated yet.

[Posted on Jul 8, 2024](/2325709/projects/19095668/messages/108024947#comment_931066200)

[![](https://asset1.basecamp.com/2325709/projects/19095668/attachments/497443892/7703f4c0-3d1f-11ef-ae55-0242ac110005/thumbnail.png)


2024-07-08 144429.png

Project: KeyShot | Performance Marketing

Added by Mucahit Y. on Jul 8, 2024
 · 

44 KB](https://asset1.basecamp.com/2325709/projects/19095668/attachments/497443892/2024-07-08%20144429.png)

[7 comments](/2325709/projects/19095668/messages/108024947)

[Label...](#)

Jul 8, 2024

44 KB

Mucahit Y.

![](https://asset1.basecamp.com/people/19154717/photo/avatar.96.gif "Mirak Ozoglu")

Add a comment or upload a file…

[By-the-minute history for this message...](#)

---

## Comments

#### Discuss this message

[![Fathy Elsayed](https://asset1.basecamp.com/2325709/people/18538829/photo/avatar.96.gif "Fathy Elsayed")](/2325709/people/18538829)

**Fathy Elsayed**   
Hi Josh, thanks for the references. let us initiate the setup process and get back to you with what exactly is needed to get this done.   
  
Regards,  
Fathy

[Posted on Jun 28, 2024](/2325709/projects/19095668/messages/108024947#comment_930552622)

[![Mucahit Yilmaz](https://asset1.basecamp.com/2325709/people/18561789/photo/avatar.96.gif "Mucahit Yilmaz")](/2325709/people/18561789)

**Mucahit Yilmaz**   

Hi Josh,

Can you complete the integration steps for GA4 and GTM on this page? [https://app.hubspot.com/settings/2757257/website/pages/all-domains/integrat…](https://app.hubspot.com/settings/2757257/website/pages/all-domains/integrations "https://app.hubspot.com/settings/2757257/website/pages/all-domains/integrations")

Our account doesn't have access to this setting.

For reference [https://knowledge.hubspot.com/privacy-and-consent/support-google-consent-mo…](https://knowledge.hubspot.com/privacy-and-consent/support-google-consent-mode-v2#external-site:~:text=and%20UK%20countries.-,Integrate,-with%20Google%20Analytics "https://knowledge.hubspot.com/privacy-and-consent/support-google-consent-mode-v2#external-site:~:text=and%20UK%20countries.-,Integrate,-with%20Google%20Analytics")

Thank you,

Mucahit

[Posted on Jul 1, 2024](/2325709/projects/19095668/messages/108024947#comment_930662101)

[![Josh Mings](https://asset1.basecamp.com/2325709/people/18698286/photo/avatar.96.gif "Josh Mings")](/2325709/people/18698286)

**Josh Mings**   
Done.

[Posted on Jul 1, 2024](/2325709/projects/19095668/messages/108024947#comment_930681628)

[![Mucahit Yilmaz](https://asset1.basecamp.com/2325709/people/18561789/photo/avatar.96.gif "Mucahit Yilmaz")](/2325709/people/18561789)

**Mucahit Yilmaz**   
It seems we need to update the GTM JavaScript code to continue with this setup. Can you update this code using the instructions found here? [https://developers.hubspot.com/docs/api/events/implement-google-consent-mod…](https://developers.hubspot.com/docs/api/events/implement-google-consent-mode "https://developers.hubspot.com/docs/api/events/implement-google-consent-mode")   
Specifically, refer to the section titled "Implement advanced Google consent mode v2 manually."  
  
I ask for advanced setup and not the basic one because if I understand correctly, using the basic setup might result in losing some data sent to Google products like GA4 or Ads. Under title "Implement advanced Google consent mode v2 manually" it says "When you implement consent mode on your website or app in advanced mode, Google tags are always loaded. Default consent is set (typically to denied) using the Consent Mode API. While consent is denied, Google tags will send cookieless pings. When the user interacts with the HubSpot cookie banner, the consent state updates. If consent is granted, Google tags send full measurement data. "

[Posted on Jul 3, 2024](/2325709/projects/19095668/messages/108024947#comment_930869075)

[![Josh Mings](https://asset1.basecamp.com/2325709/people/18698286/photo/avatar.96.gif "Josh Mings")](/2325709/people/18698286)

**Josh Mings**   
Hi Mucahit, I'm really looking to you and ALM's expertise here. I can update it but I would need to investigate all the tags and configuration you have set up in GTM and GA4. You and the team are familiar with that already. We already have GTM across the site so it's just a matter of adding the consent capture and listener.  We're using HubSpot for the consent banner but I would reference the Google docs on implementing this to ensure it's done correctly.  
  
<https://developers.google.com/tag-platform/security/guides/consent>

[Posted on Jul 4, 2024](/2325709/projects/19095668/messages/108024947#comment_930921024)

[![Mucahit Yilmaz](https://asset1.basecamp.com/2325709/people/18561789/photo/avatar.96.gif "Mucahit Yilmaz")](/2325709/people/18561789)

**Mucahit Yilmaz**   

Sure Josh, we are looking into it. We've added the listener and set up the default consent in the European Economic Area yesterday. We are now working on updating the consent.

[Posted on Jul 5, 2024](/2325709/projects/19095668/messages/108024947#comment_930980640)

[![Mucahit Yilmaz](https://asset1.basecamp.com/2325709/people/18561789/photo/avatar.96.gif "Mucahit Yilmaz")](/2325709/people/18561789)

**Mucahit Yilmaz**   
Hi Josh, setup is completed and published on gtm. We've updated consent settings for meta, linkedin, reddit, pinterest tags as well. Attached screenshot shows tags we didn't updated yet.

[Posted on Jul 8, 2024](/2325709/projects/19095668/messages/108024947#comment_931066200)

[![](https://asset1.basecamp.com/2325709/projects/19095668/attachments/497443892/7703f4c0-3d1f-11ef-ae55-0242ac110005/thumbnail.png)


2024-07-08 144429.png

Project: KeyShot | Performance Marketing

Added by Mucahit Y. on Jul 8, 2024
 · 

44 KB](https://asset1.basecamp.com/2325709/projects/19095668/attachments/497443892/2024-07-08%20144429.png)

[7 comments](/2325709/projects/19095668/messages/108024947)

[Label...](#)

Jul 8, 2024

44 KB

Mucahit Y.

![](https://asset1.basecamp.com/people/19154717/photo/avatar.96.gif "Mirak Ozoglu")

Add a comment or upload a file…
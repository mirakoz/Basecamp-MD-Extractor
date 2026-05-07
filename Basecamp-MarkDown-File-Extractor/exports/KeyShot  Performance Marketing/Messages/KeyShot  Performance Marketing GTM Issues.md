---
title: 'KeyShot | Performance Marketing: GTM Issues'
url: https://basecamp.com/2325709/projects/19095668/messages/108610667
author: Unknown
date: Unknown
type: basecamp-export
---

# KeyShot | Performance Marketing: GTM Issues

# [KeyShot | Performance Marketing](/2325709/projects/19095668)

KeyShot | Performance Marketing: GTM Issues

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

### GTM Issues

Posted by Josh Mings on Sep 16, 2024

[![Josh Mings](https://asset1.basecamp.com/2325709/people/18698286/photo/avatar.96.gif "Josh Mings")](/2325709/people/18698286)

Hi Burak and Fathy, please see below.  **Console errors**  
See attached. There are multiple console errors on site. I've done a quick analysis and have identified some issues. Please evaluate and address:  

* In the CustomEvents\_DOM tag, the script needs to be updated to remove:

  ```
  innerText.trim() + " - Annual";
  ```
* We no longer advertise with Meta. Please pause and add all Facebook tags to the archive folder.
* I've reached out to ListneLayer on the datalayer.min.js consent objects appearring.
* Please address any other updates that are needed regarding page/products
* Please pause and archive any tags that are no longer being used.

  
**Linkedin**  
The site had duplicate *Linkedin Insight* tags (in Wordpress and GTM). I've removed the one in Wordpress. Please confirm GTM tag is firing correctly.  
  
**HubSpot**  
The site had duplicate *HubSpot* tags (in Wordpress and GTM. The tag should be set up in GTM so it is used across our properties. However, the tag is different on each. Please evaluate and address: In Wordpress, the following tag is used:  

```
<!-- Start HubSpot -->
```

```
<script type="text/javascript" id="hs-script-loader" async defer src="//js.hs-scripts.com/2757257.js"></script>
```

```
<!-- Setting content type -->
```

```
<script>
```

```
var _hsq = window._hsq = window._hsq || [];
```

```
_hsq.push(['setContentType', 'site-page']);
```

```
</script>
```

```
<!-- End HubSpot -->
```

[![](https://asset1.basecamp.com/2325709/projects/19095668/attachments/500456473/8b296726-7449-11ef-9431-0242ac110005/thumbnail.png)


Screenshot 2024-09-16 at 12.56.40.png

Project: KeyShot | Performance Marketing

Added by Josh M. on Sep 16, 2024
 · 

223 KB](https://asset1.basecamp.com/2325709/projects/19095668/attachments/500456473/Screenshot%202024-09-16%20at%2012.56.40.png)

[1 comment](/2325709/projects/19095668/messages/108610667)

[Label...](#)

Sep 16, 2024

223 KB

Josh M.

[![](https://asset1.basecamp.com/2325709/projects/19095668/attachments/500456474/8b87dcd4-7449-11ef-9f82-0242ac110005/thumbnail.png)


Screenshot 2024-09-16 at 12.56.54.png

Project: KeyShot | Performance Marketing

Added by Josh M. on Sep 16, 2024
 · 

117 KB](https://asset1.basecamp.com/2325709/projects/19095668/attachments/500456474/Screenshot%202024-09-16%20at%2012.56.54.png)

[1 comment](/2325709/projects/19095668/messages/108610667)

[Label...](#)

Sep 16, 2024

117 KB

Josh M.

[View all of these files at once](/2325709/projects/19095668/messages/108610667/image_attachments)
•
[Download all of these files](/2325709/attachment_exports?attachable_id=108610667&attachable_type=Message)
Downloading...

#### Discuss this message

[![Fathy Elsayed](https://asset1.basecamp.com/2325709/people/18538829/photo/avatar.96.gif "Fathy Elsayed")](/2325709/people/18538829)

**Fathy Elsayed**   
Hi Josh, We've addressed all the issues mentioned. Please let us know if you are still seeing them.   
  
For the 2checkout pages, we still can't see the GTM code added, this has a major impact on the Google ads running campaigns performance.  
  
Best,  
Fathy

[Posted on Sep 18, 2024](/2325709/projects/19095668/messages/108610667#comment_936282037)

![](https://asset1.basecamp.com/people/19154717/photo/avatar.96.gif "Mirak Ozoglu")

Add a comment or upload a file…

[By-the-minute history for this message...](#)

---

## Comments

1 comment
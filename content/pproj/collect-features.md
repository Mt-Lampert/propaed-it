---
title: "Collect Features"
date: 2019-10-12T11:41:16+02:00
draft: true
---


Collecting Features begins with collecting **Aspects** of the project you want to build. Let's do it using the inevitable example of building a task manager. Let's say a good task manager has the following aspects:

* "Dashboard"
* "Checklists"
* "Assignments"
* "Messages"
* "Projects"
* "Users"
* "Teams"

Notice that all these aspects are *plurals* unless they are as singular as the dashboard. Now the thing about 'plural' stuff is that in IT it usually must be 

* Created / Added
* Read / Displayed / Listed / Used
* Updated / Modified whenever necessary
* Deleted whenever necessary

*Singular* aspects usually needn't be created or deleted because they are always there as long as the project is there. In a task manager the dashboard needn't be created or deleted as long as the task manager is running. However, those singular things need to be 

* Initialized at startup
* Tidied up at Shutdown.

And this at last brings us to our **features** where we combine the aspects we found with the verbs we found:

* "Initializing Dashboard"
* "Display Dashboard"
* "Tidying up Dashboard"
* "Creating a Checklist"
* "Displaying a Checklist"
* "Updating a Checklist"
* "Deleting a Checklist"
* "Creating an Assignment"
* "Displaying an Assignment"
* "Listing Assignments"
* "Updating an Assignment"
* "Deleting an Assignment"
* ... 

You get the idea. These are the features we have to collect.







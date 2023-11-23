![AmIResponsive](https://res.cloudinary.com/dg4yefryk/image/upload/v1691243660/responsive_vwenph.png)

See live site [here](https://knits-knots-3cc8ac17064e.herokuapp.com/).



# Why Knits&Knots?
As a passionate hobbymaker, I often scour the internet for webshops with good quality materials for my crochet or cross-stitch projects, and have learned with time which websites not only feel serious, but which provide an easy aestethic to shop at.
Many websites I've come across feel cluttered with both threads and patterns and accessories and a wide range of hooks and knitting needles and embroidery frames, and I don't want to offer another busy 'have-it-all' website, because I want the focus to be on the materials themselves, not the tools.

The goal of my webpage is to offer a minimalistic webstore for crafters who already have a collection of crochet hooks in all sizes and an abundance of embroidery needles, for those of us who enjoy browsing a clean page with the must-haves of yarns and threads. In addition, I'm offering a free videocall for members who, like I have in the past, all these cool tools from a starter pack and no idea where to go from there.

It is, all in all, a webshop for knitters and knotters.

#

- [Introduction](#introduction)
    - [User Goals](#user-goals)
    - [Site Goals](#site-goals)
- [Agile and User stories](#agile-and-user-stories)
- [Scope](#scope)
- [Wireframes](#wireframes)
- [Marketing Strategies](#marketing-strategies)
- [Design](#design)
    - [Colors](#colors)
    - [Fonts](#fonts)
- [Features](#features)
- [Structure](#structure)
- [CRUD](#crud)
- [Testing](#testing)
    - [Validator](#validator-testing)
    - [Code](#code)
    - [No errors](#no-errors)
    - [Errors](#errors)
        - [Accessability](#accessability)
    - [Manual testing](#manual-testing)
- [Bugs](#bugs)
- [Future implements - nice to have](#future-implements---nice-to-haves)
- [Deployment](#deployment)
- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks](#frameworks)
    - [Tools](#tools)
    - [Libraries](#libraries)
    - [Packages](#packages)
- [Resourses](#resourses)
    - [Assisting](#assisting)
    - [Images](#images)
    - [Icons](#icons)
    - [Sources for example posts](#sources-for-example-posts)
    - [Credits](#credits)

# Introduction

## User goals
- To easily browse handicraft materials
- To have an account to save products for later purchase
- To be provided with information about products in regards to material and care
- To purchase quality materials for my projects

## Site goals
Knits&Knots is a one-stop Business to Consumer (B2C) shop for people who enjoy handicraft and want to find all different sorts of materials for their different projects at one place. It's aimed towards crafters who already have all the tools of the trade and wants to fill up on materials no matter what thread their project needs.

# Agile and User Stories
The baseline of my User Stories is collected in an Excel file that I then transferred into a GitHub Project that uses an agile approach with the help of a Kanban board method. This made it easy to visuallize and handle all user stories one at a time and add all details to each story to be set in one place. See [Here](https://github.com/users/AuroraStorm-sw/projects/7) for the full project.

Each User Story comprises an Epic, Acceptance criteria, and several tasks; each User Story is tagged accordingly. I collected all "must have" and "nice to have" tasks in the same User Story to keep it nice and neat.
To view all User Stories, please see the above link.

# Wireframes

When planning this website, I went with the idea of it being as simple as possible to stand out from cluttered, vivid websites that can feel overwhelming with too many things to look at. The idea is for the products to be in focus, and the design has developed in a few different directions from the base idea.

<details>
<summary>View Wireframes</summary>
<br>

Home page
![Home](https://knitsknots.s3.eu-north-1.amazonaws.com/documentation/readme_images/wireframe-home-page.PNG)

![Products](https://knitsknots.s3.eu-north-1.amazonaws.com/documentation/readme_images/wireframe-products-page.PNG)

Product detail
![Product detail](https://knitsknots.s3.eu-north-1.amazonaws.com/documentation/readme_images/wireframe-products-detail-page.PNG)

![Products]()
![Products]()
![Products]()
![Products]()
![Products]()

</details>
<br>

# Marketing Strategies


1. Who are your users?
    - Handicraft enthusiasts who want to refill material

2. Which online platforms would you find lots of your users?
    - Instagram
    - Facebook
    - TikTok
    - Pinterest
    - Etsy
    - Reddit

3. Would your users use social media? If yes, which platforms do you think you would find them on?
    - Instagram
    - Facebook
    - TikTok
    - Pinterest

4. What do your users need? Could you meet that need with useful content? If yes, how could you best deliver that content to them?
    - Get a clear picture of what the materials look like
        - Instagram & TikTok reels talking about the products and showing what can be made with them
        - Break down products and talk about the material, gauge, and fibers

    - Get inspiration for new projects
        - Instagram & TikTok reels showing different projects used with the materials.

5. Would your business run sales or offer discounts? How do you think your users would most like to hear about these offers?
    - Newsletter updates with sales
    - Social media posts

6. What are the goals of your business? Which marketing strategies would offer the best ways to meet those goals?
    - Sell products
    - Assist customers to find the right product for their project
    - Get returning customers

7. Would your business have a budget to spend on advertising? Or would it need to work with free or low cost options to market itself?
    - Low cost options while staying active on social media to promote our store and the products, putting the energy into making reels and sending out newsletters, and use the profit to pay for ads on social media apps


# Design

My main design idea was to keep the webstore as simple and minimalistic as possible for two reasons; one, I view cluttered pages as unproffesional and disorienting, and two, I find it hard to focus and find my way around webstores that offer too much when I'm on a mission to find something specific, which is often materials.

The colors are simple and blend in with the background, adding some artistic feel with the swirly pattern without stealing any attention from the products. I kept the colors  gender neutral with greens and purples so not to indicate the craft is suited for one or another, instead welcoming everyone to pursue their creative passion.

## Colors
I based the colors around the background image and used [Coolors](https://coolors.co) to create a palette based on one of the nuances. 

![Palette](https://knitsknots.s3.eu-north-1.amazonaws.com/documentation/readme_images/palette.PNG)

From this palette, I focused on the colors #C5C0F1 and #66B100. They're both bright colors but used sparingly across the webstore, bringing some happiness and artistic vibe without overtaking the visual experience.

## Fonts

For fonts, I ended up with Autour One for the main headers. It has a touch of an artistic vibe with mildly squirly letters without coming off as childish.

![Autor](https://knitsknots.s3.eu-north-1.amazonaws.com/documentation/readme_images/autour-one-font.PNG)

For paragraphs, I went with Palanquin, which is a very simple and straight-forward font that lets the header stand out on its own.

![Palanquin](https://knitsknots.s3.eu-north-1.amazonaws.com/documentation/readme_images/palanquin-font.PNG)

# Features

- Home page
    - Navbar

    The navbar consists of a basic Bootstrap navbar with tabs and a dropdown for categories, including a hamburger menu for smaller viewports.
    Users can navigate between the home page and available categories, create a new ink, or sign out when logged in.
    Users without an account or who aren't logged in can navigate between the home page, available categories, sign in, or create an account.
    The logo also serves as a link back to the home page.

    ![Image]()

    - Intro

    The home page introduction consists of a few paragraphs of text explaining what the website is about and for whom, inspiring users to create their own Inks and leave feedback or ink drops (likes) on others'.

    ![Image]()

    - Inks

    After scouring the internet and Slack for inspiration for the structure of how the posts should be displayed, I ended up taking layout inspiration from [Kathrin's Haiku blog](https://github.com/Kathrin-ddggxh/woohoo-haiku), as they are of perfect size for cards displaying little information, compared to a lot of other blogs that need bigger cards that often include images. This Bootstrap card layout makes the posts responsive in all sizes and stacks prettily on smaller screens without sacrificing text.

    Adding to the layout, I found a watercolor-esque wallpaper that I faded to a lighter opacity for the background, adding to an inky feel.

    ![Image]()

    - Footer

    The footer is very basic and straightforward, offering links to social media.

    ![Image]()

- Create a new Ink
    - Write

    The layout for the form to write an Ink is kept very simplistic, as creating an Ink shouldn't feel like rocket science. It consists of an author input, category, title, an excerpt if the user feels like adding one, and the main content. Below are two buttons, one for submitting the Ink and one for canceling, which returns the user to the home page.

    ![Image]()

    - Edit Ink

    Similarly to the Create a New Ink page, the Edit page is simplistic. The user can update the title, excerpt, and main content. There are two buttons below, one for updating the Ink and one for canceling out of edit mode. This can only be accessed by the author of the Ink.

    ![Image]()

    - Delete Ink

    Should the user decide to delete an Ink, they'll be directed to a page where they are asked to confirm if they wish to delete it or not, giving them the option to go ahead and delete their Ink or cancel out and return to the home page.

    ![Image]()

- Category Archive

    - Category

    When browsing the category list, each Ink within that category is displayed similarly to those on the Home page, making it easy to browse between them.

    ![Image]()

- Account
    - Create account

    Like everything else, the create account section is kept as simplistic as possible to make the process quick and easy, with a basic structure.

    ![Image]()

    - Sign in

    As with Account Creation, signing in is just as easy, offering only what's needed. 

    ![Image]()
    

    - Sign out

    When the user signs out, they'll be directed to a page asking them if they're sure to sign out, giving them the option to proceed with the sigh out or cancel, returning them to the home page.

    ![Image]()


# Structure

## CRUD

- Create: A user can create an order for purchase.
- Read: A user can browse the products on the webpage.
- Update: A user can update their order with more or fewer products when browsing and in the shopping basket, and an authenticated user can update their profile information.
- Delete: A user can delete items from their shopping basket.

## Custom model

The basic structure of the website is based on [Code Institute Boutique Ado](https://github.com/Code-Institute-Solutions/Boutique-Ado) courseware walkthrough, though with 4 added custom models:

Wishlist: Allowing authorized users to save products to a wishlist connected to their account
Tags: Tags for users to browse through as sub-categories
Videocall: Allows authorized users to book a free videocall to get project or material help with email confirmation.
Contact: A contact form for user to reach out and ask questions or leave feedback with email confirmation.

# Testing

## Validator

## Code

[W3 HTML checker](https://validator.w3.org)

All website pages have been run through W3, with two coming out with seemingly false positive results. These two were the "Edit Ink" and "View Ink", and has been documented as a separate issue along side the debugging and re-validating, please see below.

## No errors

<details>
<summary>View all results with no errors.</summary>
<br>

- Sign in

![SignIn](https://res.cloudinary.com/dg4yefryk/image/upload/v1691147698/test-login_fl1u4l.png)

- Sign out

![SignOut](https://res.cloudinary.com/dg4yefryk/image/upload/v1691147698/test-sign-out_s9dhoi.png)

- Sign up

![SignUp](https://res.cloudinary.com/dg4yefryk/image/upload/v1691147698/test-signup_bftkjh.png)

 - Home page

![Home](https://res.cloudinary.com/dg4yefryk/image/upload/v1691147698/test-home_rwd4lx.png)

 - Add new Ink

![AddInk](https://res.cloudinary.com/dg4yefryk/image/upload/v1691147698/test-add-ink_tq3a5e.png)

 - View Ink post

![Category](https://res.cloudinary.com/dg4yefryk/image/upload/v1691147698/test-category_w6bujd.png)

- Delete Ink

![InkDelete](https://res.cloudinary.com/dg4yefryk/image/upload/v1691147698/text-delete_jhahvj.png)
</details>

## Errors

The errors have been documented in their separate Issue [Here #12](https://github.com/AuroraStorm-sw/Inspired-Ink/issues/12).

## [CI Python Linter](https://pep8ci.herokuapp.com/)

Each .py file has been passed through the linter with very few errors; those coming up were regarding trailing whitespace, missing space, and missing a new line at the end of the code. These were all easily fixed, and the files are now error-free.

![linter](https://res.cloudinary.com/dg4yefryk/image/upload/v1691147698/linter-test-model_hslsux.png)


## [JSHint]([https://jshint.com/])

![https://jshint.com/](https://res.cloudinary.com/dg4yefryk/image/upload/v1691180009/test-javascript_e99aqr.png)


### Accessibility

## [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)
![Lighthouse](https://res.cloudinary.com/dg4yefryk/image/upload/v1691159942/lighthouse_eipqg2.png)

## [Axe DevTools](https://chrome.google.com/webstore/detail/axe-devtools-web-accessib/lhdoppojpmngadmnindnejefpokejbdd)

![AxeDevtools](https://res.cloudinary.com/dg4yefryk/image/upload/v1691160050/axe-devtools_nary38.png)

## [WAVE](https://wave.webaim.org/)
![WAVE](https://res.cloudinary.com/dg4yefryk/image/upload/v1691164948/wave_dxpdvl.png)


## Manual testing

| Action           | Expected Result                                                                                                                                | Pass |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------|------|
| Account creation | I can create a new account with username and password and be notified that it's created successfully, or if not                               | Pass |
| Sign in          | I can sign in with my username and account and get notified that I've been successfully signed in                                              | Pass |
| Sign out         | When signed in, I can sign out of the webpage, be asked if I'm sure I want to sign out and be notified that I've been successfully signed out | Pass |
| Navbar           | Each link in the navbar takes me to the correct corresponding page. There are different paged depending on if I am signed in or not.           | Pass |
| Create post      | When signed in, I can write an 'Ink', a creative text of my choice, and submit it. I'll be notified that it's successfully submitted.     | Pass |
| Edit post        | When signed in, I can edit my own Inks and be notified that it has been successfully edited                                                  | Pass |
| Delete post      | When signed in, I can delete my own posts, be asked if I'm sure I want to delete them, and be notified that it has been successfully deleted     | Pass |
| Comment on post  | When signed in, I can leave feedback on others' posts. My comment is then visible beneath the post.                                            | Pass |
| Like/unlike post | When signed in, I can like and unlike others' posts. The icon changes                                                                          | Pass |
| Category         | I can browse different categories via the navbar                                                                                               | Pass |
| Pagination       | I can browse through multiple pages on the home page if there are more than six posts                                                          | Pass |
| Links            | All of the links throughout the page are fully functional                                                                                      | Pass |
| Buttons          | All of the buttons direct me to their designated function                                                                                      | Pass |
| Footer           | I can reach the different social media sites via the footer, and they all open in new tabs.                                                   | Pass |


## Responsiveness

The deployed app has been tested across these web browsers with full responsiveness:
- Firefox
- Google Chrome
- Microsoft Edge

It has also been tested on Samsung mobile in physical form, and various viewports with the help of developer tools in the browser.

When creating an account on Opera web browser, the user got a "Forbidden" error screen, but was still able to use the website as signed in after returning to the previous page. Upon searching for solutions online, non came up related to the Opera browser.

![OperaError](https://res.cloudinary.com/dg4yefryk/image/upload/v1691245409/403-opera_e5eiq7.png)

[AmIResponsive](https://ui.dev/amiresponsive) was used as a guideline to see responsiveness across different viewports.

# Bugs
1. Lingering 'missing data' in the category table after migrating the category model and category addition to Post without creating a category index.
Solution: Reset the database to remove the error and recreate the superuser.

2. Static files are not loading on Heroku.
Solution: Through tutor support, they found a spelling error in loading style.css in base.html after much trial and error.

3. "Back" button on view_ink.html shows up on a white, separate line when a user isn't signed in.
Solution: Wrap the section around an extra top div so the button doesn't get its own line when the feedback section isn't visible to unauthorized users.

4. After changing DEBUG from True to False, sometimes needs to change name of style.css file for the new styling to get added to the website, even after hard refreshing the webpage.
Solution: Still debugging at time of project submission, no solution discovered in time.

5. Account creation not fully functional on Opera Web browser, causing an 403 Forbidden error message.
Solution: No information about this specific error has come up when searching for information online. The signup form comes with a csrf token. Unclear if the error is caused by the webpage itself or by Allauth.

6. The text "Body*" showing next to the main textcontent input when creating an Ink. The text was included in the form, and I wasn't able to remove it.
Solution: Hiding the text with CSS, using font-size: 0 on that specific field.


# Future implements - nice to haves

- Add a word counter to the Ink posts so users can see how long the posts are in the post overview. This idea was put to the side due to the deadline.
- Add a short backstory about each writing style's origin on the category pages.
- Add function for user to view all their own Inks and others' Inks by clicking on their username
- Change so that users can't like their own Inks

# Deployment

Github

Steps I took to deploy my website;

This project was used with the [Code Institute Full Template](https://8000-aurorastorm-inspiredink-han0133genl.ws-eu102.gitpod.io/lie-to-me/).

1. Go to the repository for Inspired-Ink
2. Click the Settings tab and locate the Pages tab
3. Select to deploy from the main branch
4. A few minutes later, upon refreshing the page, my site was live

For anyone wishing to Fork this repository, then do as follows;

1. Log in to GitHub and find your way to the GitHub repository you want, in this case, my Inspired Ink project
2. Up in the right corner of the repository page, on the row of buttons just beneath the user icon, you'll find the "Fork" button.
3. Click the "Fork" button, and you will now have created a copy of the repository to your GitHub account.

To clone this repository, then do as follows;

1. Log in to GitHub and find your way to the GitHub repository you want, and click the "<> Code" button in the upper right above the files
2. Copy the link
3. Open Gitpod and select which directory you want the clone to be created into.
4. Type in "git clone" in your Gitpod terminal and paste the link copied from GitHub and the close will be created.

Deploying the app in Heroku:

To properly deploy with Heroku, I've used [Code Institutes Django Blog Cheat Sheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf), describing all steps for installing Django and supporting libraries.

The instructions below are for the basic Heroku app setup. For specific Django settings and instructions, please refer to the Cheat Sheet.

1. Log in to Heroku or create a new account by following the instructions on the page
2. On the main page near the top, click "New" and select "Create new app."
3. Pick your unique app name and select your region
4. Click the "Create App" button
5. On the next page, move to the "Settings" tab and find "Config Vars."
6. Click "Reveal Config Vars" and add relevant config vars and their keys, then click "Add."
7. Scroll back up and click the "Deploy" tab
8. Here, you select "GitHub" as the deployment method and search for your repository to link them together
9. Scroll down the page and select if you want to "Enable Automatic Deploys" to deploy your pushes from GitHub to Heroku automatically.

# Technologies Used

## Languages
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)

## Frameworks
- [Django](https://www.djangoproject.com/) - The main Python framework used to develop this project.
- [Bootstrap](https://getbootstrap.com/) - For general layouts and responsiveness across the site.
- [ElephantSQL](https://www.elephantsql.com/) - The production database used for the project.
- [GitHub](https://github.com/) - Used to host the source code.
- [Gitpod](https://gitpod.io/) - Used to commit, comment, and push code throughout the project.
- [Heroku](https://www.heroku.com) - Used for app deployment.
- [Balsamiq](https://balsamiq.com/) - For creating wireframes for the project.
- [Cloudinary](https://console.cloudinary.com) - Stores all static files and images.

## Tools
- [JsHint](https://jshint.com/) - For validating Javascript code.
- [CI Python Linter](https://pep8ci.herokuapp.com/#) - For validating Python code.
- [W3C HTML Validator](https://validator.w3.org/) - For validating HTML code.
- [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) - For validating CSS code.
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) - Developer tool used throughout the project for bug fixing and error searching.
- [Axe DevTools](https://chrome.google.com/webstore/detail/axe-devtools-web-accessib/lhdoppojpmngadmnindnejefpokejbdd) - A developer tool for validating accessibility.
- [HTMLHint](https://htmlhint.com/) - Static code analysis tool for HTML.
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/) - For accessability validation.
- [WAVE](https://wave.webaim.org/) - For accessibility and contrast validation.
- [Grammarly](https://app.grammarly.com/) - Used to spell and grammar check the ReadMe.

## Libraries
- Gunicorn - The server used for running Django on Heroku.
- pyscopg2 - Used to connect to PostgreSQL.
- Cloudinary - Used to host static files and images.
- Whitenoise - Helps resolve issues with Heroku not rendering custom CSS stylesheets.

## Packages

- Django - An MVP, model-template-view, Python-based web framework for building projects.
- django-allauth - Used for account registration, managing signing in and out, and authentication.
- cloudinary_storage - Storage backend for Cloudinary that is used for static storage.
- django_summernote - Integrates Summernote WYSIWYG editor into Django projects. This package was installed but ended up not being used in the project.
- crispy_forms - Makes styling Django forms easier.

# Resourses

## Assisting
- [Table Converter](https://tableconvert.com/) - For Manual Testing structuring.
- [Tinypng](https://tinypng.com/) - For compressing background image.
- [Coolors](https://coolors.co) - For generating a color palette.
- [Google Fonts](https://fonts.google.com) - For browsing and implementing fonts.
- [AmIResponsive](https://ui.dev/amiresponsive) - For checking responsiveness across several viewports.

## Images
- [Background image](https://www.pexels.com/photo/empty-brown-canvas-235985/)
- [Quote image](https://abstract.desktopnexus.com/get/1737801/?t=146uo7bue09b2o59gjgv030rd364ccdb5086d33)
- [Ink Card Image](https://wallpapercave.com/w/wp1938057)

## Icons
- https://icon-sets.iconify.design/mdi/ink/
- https://icon-sets.iconify.design/mdi/ink-plus/
- https://icon-sets.iconify.design/mdi/ink-plus-outline/
- https://icon-sets.iconify.design/material-symbols/comment/

## Sources, for example, posts
- [To Atthis the Inconstant by Sappho](https://ozofe.com/sappho/to-atthis-the-inconstant/)
- [On Aging by Maya Angelou](https://ozofe.com/maya-angelou/on-aging/)
- [In a station of the metro by Ezra Pond](https://reedsy.com/discovery/blog/haiku-poem-examples)
- [Part of the lyrics to War by Poets Of The Fall](https://www.songlyrics.com/poets-of-the-fall/war-lyrics/)
- [The Story of an Hour by Kate Chopin](https://americanliterature.com/author/kate-chopin/short-story/the-story-of-an-hour ) 
- [Lyric part of Lie to Me by Riell](https://genius.com/Riell-lie-to-me-lyrics)
- [Scarlet Stockings by Louisa May Alcott](https://americanliterature.com/author/louisa-may-alcott/short-story/scarlet-stockings)

Any Ink not included in the list is written by me or website users.

# Credits

- [Very Academy](https://www.youtube.com/watch?v=S9-Bt1JgRjQ&list=PLOLrQ9Pn6cawWd-5UZM6CIm0uqFXeBcTd&index=4) - Youtube video guidance on how to add a category model and view for the custom model.

- [Codemy.com](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) - A playlist of Youtube videos going through all stages of building a Django blog that I used to browse through to get tips and tricks on how to structure models, views, and URLs.

- [StackOverflow](https://stackoverflow.com/) - A forum used throughout the project when searching for solutions for errors or ideas on views or how to add specific functions to the website. Throughout the project, sources have been added to each corresponding piece of code in comments.

- [Slack](https://slack.com/) - Many answers to errors and frustrations have been found when browsing issues across different channels. Throughout the project, sources have been added to each corresponding piece of code in comments.

- [Code Institute Courseware](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/dabfed30d1fc4d078b6de270117dbe50/) - Code Institute courseware used for the basic structure of the Ink and Feedback/Comment models.

- [Code Institute Template](https://github.com/Code-Institute-Org/gitpod-full-template) - the template used as a base for the project.

- [Kathrin's Haiku blog](https://github.com/Kathrin-ddggxh/woohoo-haiku) - For the shape and Bootstrap template of the Ink cards on the Home and Category page, including the 'hover transformation' effect.

- Code Institutes Tutor Support where amazing in helping me sort out some mind-boggling issues, like why my static files weren't loading on Heroku and when I had to reset my database, and they did so with such patience and clear guidance.
Many thanks to Sarah, Rebecca, Martin, Ed, and Joshua for code reparing, typo-hunting, and for their support throughout this journey. I would not have any hair left on my head if it weren't for them helping me with these frustrating issues.

- Fellow coders on Slack were of great help in pointing me in the right direction when I felt lost or when the result of my code didn't make any sense. The outline of the ReadMe has been inspired by different Portfolio 4 projects in the peer-per-view channel, as well as my own previous projects.

- My amazing flatmate Erik, who helped me with a fresh pair of eyes when I couldn't find errors across the code and also supplied me with snacks to help me keep my sanity throughout the project.

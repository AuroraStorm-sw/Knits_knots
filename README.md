![AmIResponsive](/documentation/responsiveness/amiresponsive.PNG)

See live site [here](https://knits-knots-3cc8ac17064e.herokuapp.com/).



# Why Knits&Knots?
As a passionate hobbymaker, I often scour the internet for webshops with good quality materials for my crochet or cross-stitch projects, and have learned with time which websites not only feel serious, but which provide an easy aestethic to shop at.
Many websites I've come across feel cluttered with both threads and patterns and accessories and a wide range of hooks and knitting needles and embroidery frames, and I don't want to offer another busy 'have-it-all' website, because I want the focus to be on the materials themselves, not the tools.

The goal of my webpage is to offer a minimalistic webstore for crafters who already have a collection of crochet hooks in all sizes and an abundance of embroidery needles, for those of us who enjoy browsing a clean page with the must-haves of yarns and threads. In addition, I'm offering a free videocall for members who, like I have in the past, all these cool tools from a starter pack and no idea where to go from there.

It is, all in all, a webshop for knitters and knotters.


## Introduction

### User goals
- To easily browse handicraft materials
- To have an account to save products for later purchase
- To be provided with information about products in regards to material and care
- To purchase quality materials for my projects

---

### Site goals / Marketing Strategy
Knits&Knots is a one-stop Business to Consumer (B2C) shop for people who enjoy handicraft and want to find all different sorts of materials for their different projects at one place. It's aimed towards crafters who already have all the tools of the trade and wants to fill up on materials no matter what thread their project needs.

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

### Database: [ERD MAP](/documentation/database/pp5-erd.pdf)

### Facebook page
![Facebook1](/documentation/Facebook/fb-1.PNG)
![Facebook1](/documentation/Facebook/fb-2.PNG)

---

## Structure

### CRUD

- Create: A user can create an order for purchase.
- Read: A user can browse the products on the webpage.
- Update: A user can update their order with more or fewer products when browsing and in the shopping basket, and an authenticated user can update their profile information.
- Delete: A user can delete items from their shopping basket.

### Custom model

The basic structure of the website is based on [Code Institute Boutique Ado](https://github.com/Code-Institute-Solutions/Boutique-Ado) courseware walkthrough, though with 4 added custom models:

- Wishlist: Allowing authorized users to save products to a wishlist connected to their account
- Tags: Tags for users to browse through as sub-categories
- Videocall: Allows authorized users to book a free videocall to get project or material help with email confirmation.
- Contact: A contact form for user to reach out and ask questions or leave feedback with email confirmation.

### Agile Methodology

![Agile](/documentation/agile/agile.PNG)

The baseline of my User Stories is collected in an Excel file that I then transferred into a GitHub Project that uses an agile approach with the help of a Kanban board method.

The first Kanban board I created with this product became unavailable to display for anyone other than me on my Github page. After trying to solve the issue with the help of my mentor, we concluded that the only way to solve the issue was by creating a newe Kanban board and add new issues. These are therefore all created and closed at the same time, since I've already worked along the previous board. My former Kanban project is still connected to the repository in order to turn the issue to GitHub, marked BUGGED, and the new Kanban board is now connected to the repository.

See [Here](https://github.com/users/AuroraStorm-sw/projects/12/) for the full Kanban project.


### Wireframes

When planning this website, I went with the idea of it being as simple as possible to stand out from cluttered, vivid websites that can feel overwhelming with too many things to look at. The idea is for the products to be in focus, and the design has developed in a few different directions from the base idea.

<details>
<summary>View Wireframes</summary>
<br>

When brainstorming the website structure, I built basic wireframes for the home page, product page, and product detail, getting an idea of what feeling the website should have. A few structures are inspired by Code Institutes Boutique Ado walkthrough, mainly the profile, shopping basket, and checkout page, that I adjusted to fit my website.

The other pages I build as I went on, making changes throughout the process to fit the vibe, though focusing on functionality first.

Home page
![Home](https://knitsknots.s3.eu-north-1.amazonaws.com/documentation/readme_images/wireframe-home-page.PNG)

![Products](https://knitsknots.s3.eu-north-1.amazonaws.com/documentation/readme_images/wireframe-products-page.PNG)

Product detail
![Product detail](https://knitsknots.s3.eu-north-1.amazonaws.com/documentation/readme_images/wireframe-products-detail-page.PNG)


</details>
<br>

---

## Design

My main design idea was to keep the webstore as simple and minimalistic as possible for two reasons; one, I view cluttered pages as unproffesional and disorienting, and two, I find it hard to focus and find my way around webstores that offer too much when I'm on a mission to find something specific, which is often materials.

The colors are simple and blend in with the background, adding some artistic feel with the swirly pattern without stealing any attention from the products. I kept the colors  gender neutral with greens and purples so not to indicate the craft is suited for one or another, instead welcoming everyone to pursue their creative passion.

### Colors
I based the colors around the background image and used [Coolors](https://coolors.co) to create a palette based on one of the nuances. 

![Palette](https://knitsknots.s3.eu-north-1.amazonaws.com/documentation/readme_images/palette.PNG)

From this palette, I focused on the colors #C5C0F1 and #66B100. They're both bright colors but used sparingly across the webstore, bringing some happiness and artistic vibe without overtaking the visual experience.

### Fonts

For fonts, I ended up with Autour One for the main headers. It has a touch of an artistic vibe with mildly squirly letters without coming off as childish.

![Autor](https://knitsknots.s3.eu-north-1.amazonaws.com/documentation/readme_images/autour-one-font.PNG)

For paragraphs, I went with Palanquin, which is a very simple and straight-forward font that lets the header stand out on its own.

![Palanquin](https://knitsknots.s3.eu-north-1.amazonaws.com/documentation/readme_images/palanquin-font.PNG)

### Features

[Front Page](/documentation/webpage_images/Front-page.pdf)

[Products](/documentation/webpage_images/Products.pdf)

[Profile](/documentation/webpage_images/Profile.pdf)

[Shopping Basket](/documentation/webpage_images/Shopping-basket.pdf)

[Videocall](/documentation/webpage_images/Videocall.pdf)

[Confirmation Emails](/documentation/webpage_images/Confirmation-emails.pdf)

## Testing

### Validator

### Code

#### [W3 HTML checker](https://validator.w3.org)

[W3 HTML Testing Results No Bugs](/documentation/testing/w3-html-checker-no-bugs.pdf)

[W3 HTML Testing Results Bugs](/documentation/testing/w3-html-checker-bugs.pdf)

#### [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

CSS code was checked by pasting the raw code from Styles.css into the validator textarea.

![CSS Validator](/documentation/testing/w3c-validator.png)

#### [CI Python Linter](https://pep8ci.herokuapp.com/)

[CI Python Linter Results](/documentation/testing/python-linter.pdf)


#### [JSHint]([https://jshint.com/])

[JSHint Testing Results](/documentation/testing/jshint.pdf)

## Accessibility

### [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)
[Lighthouse Testing Results](/documentation/testing/lighthouse.pdf)

### [Axe DevTools](https://chrome.google.com/webstore/detail/axe-devtools-web-accessib/lhdoppojpmngadmnindnejefpokejbdd)

![AxeDevtools](/documentation/testing/axe-dev-tools.PNG)

### [WAVE](https://wave.webaim.org/)
[WAVE Testing Results](/documentation/testing/wave.pdf)


## Manual testing

| Action                 | Expected Result                                                                                                                                          |      |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|------|
| Home navigation        | When clicking the logo, I'll be taken back to the home page                                                                                              | Pass |
| Account creation       | I can create a new account with username and password, and be notified that it's created successfully, or if not                                         | Pass |
| Email confirmation     | I'll be sent an email to verify my email address                                                                                                         | Pass |
| Sign in                | I can sign in with my username and accound and get notified that I've been successfully signed in                                                        | Pass |
| Sign out               | When signed in, I can sign out of the webpage, be asked if I'm sure I want to sign out, and be notified that I've been successfully signed out           | Pass |
| Navbar                 | Each link in the navbar takes me to the correct corresponding page.                                                                                      | Pass |
| Browsing               | When browsing products, I can sort them by price and category.                                                                                           | Pass |
| Search bar             | I can search for products with the search bar                                                                                                            | Pass |
| Category               | All categories show the appropriate products                                                                                                             | Pass |
| Tags                   | All tags work properly and displays the tagged products                                                                                                  | Pass |
| About us               | The about us page offers relevant information about the company                                                                                          | Pass |
| FAQ                    | The FAQ page offers answers to relevant information about returns, orders, deliveries, and products                                                      | Pass |
| Contact                | At the contact page, I can post a question or feedback to the company. I'll get a confirmation that my email was sent and recieve a confirmation email   | Pass |
| Products               | I can browse through all the products and click on them to get more information                                                                          | Pass |
| Product detail         | When clicking on a product, I can read more information about it, see the price, and choose to add a number of it to the basket or add it to my wishlist | Pass |
| Wishlist               | When clicking "Add to wishlist" on a product, I geta notification that the product is added to my wishlist, where I can display it or remove it.         | Pass |
| Remove from wishlist   | When clicking "Remove from wishlist", the product disappears from my wishlist, and I get a notification.                                                 | Pass |
| Add to basket          | When clicking the 'Add to basket' button, I get a notification that the products have been added to my basket                                            | Pass |
| Checkout button        | When I click the 'Checkout Button', I'll be taken to the basket summary page so overview my added products                                               | Pass |
| Adjust quantity        | In the shopping basket, I can adjust the number of products which will update the price                                                                  | Pass |
| Delete product         | In the shopping basket, I can delete products which will update the price                                                                                |      |
| Secure checkout        | When I click the 'Secure checkout' button, I'll be taken to the checkout page                                                                            | Pass |
| Checkout form          | I can fill out the checkout form with my delivery information, and will be notified if I've missed any information.                                      | Pass |
| Checkout success       | After filling out my checkout form, I'll be notified that my order is successfully processed, and get a summary of my order                              | Pass |
| Checkout confirmation  | After processing my order, I'll recieve a confirmation email about my order and delivery history                                                         | Pass |
| Profile                | Upon registration, I'll have access to a profile                                                                                                         | Pass |
| Profile delivery info  | In my profile, I can view and update my delivery information                                                                                             | Pass |
| Order history          | In my profile, I can see my order history, and open it to view more details                                                                              | Pass |
| Videocall non-member   | If I'm not a member, I can read about getting a free videocall if I register on the website                                                              | Pass |
| Videocall member       | As a member, I can access a free videocall to get assisted with material or a handicraft                                                                 | Pass |
| Videocall booking      | As a member, I can book a videocall and be notified that the call is confirmed                                                                           | Pass |
| Videocall confirmation | If I book a videocall, I'll recieve a confirmation email with my booking information                                                                     | Pass |
| Newsletter             | I can subscribe to the newsletter via the form                                                                                                           | Pass |
| Product management     | As admin, I can add a new product to the store via the frontend                                                                                          | Pass |
| Product management     | As admin, I can edit a product via the frontend                                                                                                          | Pass |
| Product management     | As admin, I can delete a product via the frontend                                                                                                        |      |
|                        |                                                                                                                                                          |      |
| Footer                 | I can reach the different social medias sites via the footer, and they all open in new tabs.                                                             | Pass |



## Responsiveness

The deployed app has been tested across these web browsers with full responsiveness:
- Firefox
- Google Chrome
- Microsoft Edge

It has also been tested on Samsung mobile in physical form, and various viewports with the help of developer tools in the browser.

## Bugs
1. Removed Order App after realizing it never got used, but this caused a deployment error as the database was now missing the order module, and the deployed website couldn't be accessed.
Solution: Re-added the Order App and re-deployed the website due to lack of time to resolve the issue with the app removed. For now, the app will remain, and where there is time to solve the issue, the app will either be used or removed properly.

2. Static files are not loading on Heroku.
Solution: Through tutor support, found that I had ```AWS = True``` in my enc.py file which stopped static updates from being deployed. Removed it and the issue was solved.

3. When turning the phone number input in the profile page form to integers only, it came along with increase and decrease arrows.
Solution: Searched StackOverflow (See credits) and found a CSS solution to remove the arrows from the particular inputs.

4. Missing images on deployed heroku page after updating the images locally.
Solution: 

5. Unable to sign in as superuser with email, turned out to have accidentally added the same email for 2 different users
Solution: Delete 1 user, problem solved.

6. Images missing on heroku but showing on local and viceversa
Solution: Copy the media folder to static and keep the media folder on top level, will be further investigated in the future to successfully remove 1 folder.


## Future implements - nice to haves
- Add a pop-up for booking time for videocall form instead of writing it in manually
- Ensure a member can only book 1 videocall
- Style confirmation emails to be more aestethic
- Include discounts for members

## Deployment

### STRIPE Payment Setup:

Setup based on STRIPE tutorial from Code Institute

## Payment Configuration

1. Go to https://dashboard.stripe.com/register to create a Stripe account.
2. Visit the page for developers:

3. Choose your API keys.

The 'public key' and 'secret key' should be copied to the `env.py` file.

5. Update `settings.py` with the following setting:

```Python
  OS.ENVY = STRIPE_PUBLIC_KEY.acquire("STRIPE_PUBLIC_KEY")
  OS.ENVY = STRIPE_SECRET_KEY.return get("STRIPE_SECRET_KEY")
```
6. Put the stripe package in place:

```python
pip3 install stripe 
```
7. In the orders app, create an order model with the necessary fields filled in.
8. Set up a payment app.
9. Complete the payment app template by adding a payment form.
10. Add div to hold stripe element:

```html
  - Get public key: `stripe_public_key = settings.STRIPE_PUBLIC_KEY`
  - Get private key: `stripe_secret_key = settings.STRIPE_SECRET_KEY`
  - create intent: `intent = stripe.PaymentIntent.create(**kwargs)`
  - **kwargs for the payment intent should include:
    * `amount`: amount
    * `currency`: currency
    * `metadata`: metadata

```html
  <div id="stripe-element"></div>
```

11. Create a View to handle payment setup:
  - Get public key: `stripe_public_key = settings.STRIPE_PUBLIC_KEY`
  - Get private key: `stripe_secret_key = settings.STRIPE_SECRET_KEY`
  - create intent: `intent = stripe.PaymentIntent.create(**kwargs)`
  - **kwargs for the payment intent should include:
    * `amount`: amount
    * `currency`: currency
    * `metadata`: metadata
  - For the metadata, I have user id `userid: request.user.id`
  - Create context for the view with the following data:
      *  'my_profile': my_profile,
      *  'total_sum': total_sum,
      *  'client_secret': intent.client_secret,
      *  'stripe_public_key': stripe_public_key,

12. Include an additional js block in the payment template, where you must include the following: 
- stripe public key,
- csrf token
- payment.js script tag
- the stripe.js script tag.

13. Create variables for the payment element, payment form, stripe public key, and a variable from which you will obtain the "client secret" in the payment.js file.

14. Set up STRIPE element

16. Create an AJAX request to send collected data, and specify the URL for adding orders: `window.location.origin + '/orders/add/'`.

17. To manage order creation, you must add a view in the orders app views.py.

18. When a user hits the confirmation button, a payment intent is formed. The STRIPE element handles all potential failures and saves the user from having to click many times. To show the problem to the user, you must, however, set alerts.

19. In order to test the user's payment, you can create a test payment with the card data provided by STRIPE.

No auto authenticated: 4242424242424242

Authenticated: 4000002500003155

Error: 4000000000009995

20. After a payment is successfully made, create a success page and include js functionality to manage the redirection.

21. Set app STRIPE backend:
  - Go to [Stripe Docs. Stripe CLI](https://stripe.com/docs/stripe-cli)
  - Download the stripe-cli file based on the version of your OS.
  - Open the downloaded file and move the file `stripe` to the project's root directory.

  - Open the terminal and type:

  `./stripe login`

  - Hit enter, this will redirect you to the STRIPE dashboard. Here, you need to allow access to your local workspace.

  - Create a payment, and the intent will be created.

22. Create a function in the orders views to handle the payment confirmation, which will take payment data. Additionally, this function will be responsible for handling the email confirmation as well.

23. To run this function, add the following process provided by stripe:

```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
  def stripe_webhook(request):
      payload = request.body
      event = None
      try:
          event = stripe.Event.construct_from(
              json.loads(payload), stripe.api_key
          )
      except ValueError as e:
          return HttpResponse(status=400)
      # Handle the event
      if event.type == 'payment_intent.succeeded':
          payment_confirmation(event.data.object.client_secret)
      else:
          print('Unhandled event type {}'.format(event.type))
      return HttpResponse(status=200)
```

24. Add URL to the stripe_webhook function to urls.py

```python
    path('webhook/', stripe_webhook),
```

25. In the terminal type:

`./stripe listen --forward-to localhost:8000/payment/webhook/`

26. Remember to set app stripe data in Heroku configs:

  - Create a webhook in the stripe dashboard and set the hosted endpoint.

  - `STRIPE_PUBLIC_KEY`
  - `STRIPE_SECRET_KEY`
  - `STRIPE_WEBHOOK_SECRET`


For STRIPE styling options, check out the following documents [stripe/elements-examples](https://github.com/stripe/elements-examples).
---

### Github Deployment

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

## Technologies Used

### Languages
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks
- [Django](https://www.djangoproject.com/) - The main Python framework used to develop this project.
- [Bootstrap](https://getbootstrap.com/) - For general layouts and responsiveness across the site.

### Databases
- [ElephantSQL](https://www.elephantsql.com/) - The production database used for the project.

### Packages

- Gunicorn - The server used for running Django on Heroku.
- pyscopg2 - Used to connect to PostgreSQL.
- django-allauth - Used for account registration, managing signing in and out, and authentication.
- django_summernote - Integrates Summernote WYSIWYG editor into Django projects. This package is used for styling product descriptions.
- crispy_forms - Makes styling Django forms easier.


### Tools
- [GitHub](https://github.com/) - Used to host the source code.
- [Gitpod](https://gitpod.io/) - Used to commit, comment, and push code throughout the project.
- [Heroku](https://www.heroku.com) - Used for app deployment.
- [Balsamiq](https://balsamiq.com/) - For creating wireframes for the project.
- [AWS Bucket](https://aws.amazon.com/) - Stores all static files and images.
- [STRIPE](https://stripe.com/en-gb-se) - Payment system and webhooks.
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


### Resourses

### Assisting
- [Table Converter](https://tableconvert.com/) - For Manual testing structuring.
- [Coolors](https://coolors.co) - For generating a color palette.
- [Google Fonts](https://fonts.google.com) - For browsing and implementing fonts.
- [AmIResponsive](https://ui.dev/amiresponsive) - For checking responsiveness across several viewports.

### Generators
- Slogan generator - https://ahrefs.com/writing-tools/slogan-generator
- Logo designer - https://www.freelogodesign.org
- Background generator - https://bgjar.com
- Secret key generator - https://miniwebtool.com/django-secret-key-generator/
- Intro text generator - https://deepai.org/
- Company biography generator - https://writerbuddy.ai/free-tools/company-bio
- Private Policy generator - https://www.privacypolicygenerator.info
- Font generator - https://fontjoy.com/

### Images
- [Background image](https://www.pexels.com/photo/empty-brown-canvas-235985/)

### Icons

- [Iconify](https://iconify.design/)

### Images
All product images and descriptions have been taken from https://www.amazon.com/ where I searched for cotton yarn, bamboo yarn, cake yarn, sewing thread, macramé rope, and embroidery floss.

## Credits

### Github repos inspiration

- Wishlist and footer inspired by Clay&Fire
https://github.com/SamanthaBooth81/clay_and_fire

- General inspiration for model structure and template tags
https://github.com/IuliiaKonovalova/e-commerce
https://github.com/Kieran132/Runaway
https://github.com/rockroman/CI_PP5_Blade

### Troubleshooting

- Remove increment on forms inputs for phone number
https://stackoverflow.com/questions/28320349

- Button for scrolling back to the top of tha page
https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_scroll_to_top*/

- Previous page button:
https://stackoverflow.com/questions/2968425/

- Setting for Django version above 3.2 for Allauth to trust site CSRF token
https://stackoverflow.com/questions/70285834/

- Horizontal tab:
https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_full_page_tabs 

- Add all model fields to the admin page:
https://stackoverflow.com/questions/10543032/

- Center image:
https://www.w3schools.com/howto/howto_css_image_center.asp

- Shopping byutton:
https://css-tricks.com/css-link-hover-effects/#aa-the-sliding-highlight-link-hover-effect

- Displaying manytomanyfields:
https://stackoverflow.com/questions/3891321/question-on-django-displaying-many-to-many-fields

- DateInput form class:
https://stackoverflow.com/questions/3367091/

- Heroku total:
https://code-institute-room.slack.com/archives/C7HS3U3AP/p1637505402125700

- Contact form with email:
https://www.twilio.com/blog/build-contact-form-python-django-twilio-sendgrid
https://www.sitepoint.com/django-send-email/
https://www.geeksforgeeks.org/setup-sending-email-in-django-project/

- Booking date and time:
https://stackoverflow.com/questions/56885754/

- [Very Academy](https://www.youtube.com/watch?v=S9-Bt1JgRjQ&list=PLOLrQ9Pn6cawWd-5UZM6CIm0uqFXeBcTd&index=4) - Youtube video guidance on how to add a category model and view for the custom model.

- [Codemy.com](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) - A playlist of Youtube videos going through all stages of building a Django blog that I used to browse through to get tips and tricks on how to structure models, views, and URLs.

- [StackOverflow](https://stackoverflow.com/) - A forum used throughout the project when searching for solutions for errors or ideas on views or how to add specific functions to the website. Throughout the project, sources have been added to each corresponding piece of code in comments.

- [Slack](https://slack.com/) - Many answers to errors and frustrations have been found when browsing issues across different channels. Throughout the project, sources have been added to each corresponding piece of code in comments.

- [Code Institute Courseware](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/dabfed30d1fc4d078b6de270117dbe50/) - Code Institute courseware used for the basic structure of the Ink and Feedback/Comment models.

- [Code Institute Template](https://github.com/Code-Institute-Org/gitpod-full-template) - the template used as a base for the project.

- [Kathrin's Haiku blog](https://github.com/Kathrin-ddggxh/woohoo-haiku) - For the shape and Bootstrap template of the Ink cards on the Home and Category page, including the 'hover transformation' effect.

- My mentor Juliia who offered a lot of support and technical help, ensuring my project is as good as it can be for submission.

- Code Institutes Tutor Support helped me out with issues big and small throughout the project.

- My amazing flatmate Erik who provided mental support throughout the project when things felt difficult.

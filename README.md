# Crypto Course #
---
[**View the full project here**](https://cryptocourse.herokuapp.com/)
 
![Crypto Course Screenshot](README/images/sitescreenshot.png)
 
## Contents ##
---
 
- [Crypto Course](#crypto-course)
- [UX (User Experience)](#ux--user-experience-)
 * [User Stories](#user-stories)
 * [Strategy Goals](#strategy-goals)
   + [Business Goals](#business-goals)
   + [User Goals](#user-goals)
 * [Scope](#scope)
 * [**Skeleton**](#--skeleton--)
 * [**Surface**](#--surface--)
   + [**Colour & Styling**](#--colour---styling--)
     - [Colour Palette](#colour-palette)
   + [**Language/Tone**](#--language-tone--)
   + [**Styling Considerations**](#--styling-considerations--)
 * [Defensive Design](#defensive-design)
- [Technologies](#technologies)
 * [Languages and Frameworks](#languages-and-frameworks)
 * [Libraries](#libraries)
 * [Editors](#editors)
 * [Tools](#tools)
 * [Deployment Platform](#deployment-platform)
- [Features](#features)
 * [CRUD Functionality](#crud-functionality)
 * [Existiting Features per Apps](#existiting-features-per-apps)
 * [Testing](#testing)
 * [Future Features](#future-features)
- [Deployment](#deployment)
 * [Application Hosting](#application-hosting)
 * [**Heroku**](#--heroku--)
 * [Requirements](#requirements)
 * [Local Deployment](#local-deployment)
 * [Heroku Deployment](#heroku-deployment)
- [Credits and References](#credits-and-references)
 
## Crypto Course ##
---
 
This is my final Milestone Project for the Full Stack Web Development course provided by Code Institute. The objective for this assignment was to create a "full-stack site based around business logic used to control a centrally-owned dataset. You will set up an authentication mechanism and provide paid access to the site's data and/or activities based on the dataset, such as the purchase of a product/service." This web application is developed by using HTML, CSS, JavaScript, Python+Django, Postgres, Stripe and AWS.
 
A live version of the site can be found [here](https://cryptocourse.herokuapp.com/).
 
Crypto Course is a Full Stack Ecommerce web application for a cryptocurrency company. This application uses E-commerce functionality in the following ways:
- CRUD functionality for admin users to ADD, EDIT or DELETE products to sell products
- CRUD functionality for registered users to ADD, EDIT or DELETE their blog post comments for interactivity with the blog
- CRUD functionality for admin users to ADD, UPDATE or DELETE blog post to increase organic traffic to the site
- Authentication mechanism with confirmation emails using Allauth
- Payment system via Stripe
 
## UX (User Experience) ##
---
 
<a name="user-stories"></a>
### User Stories ###
 
Please click [here](README/userstories.pdf) to view User Stories for this project.
 
<a name="#strategy"></a>
### Strategy Goals ###
 
#### Business Goals ####
* To sell cryptocurrency courses and related merchandise.
* To become a platform where developers and investors can learn about cryptocurrency.
* To share blog posts that are SEO friendly which would lead to more organic traffic to the  site and increase revenue.
* To allow users to leave comments on blog posts to share their opinions.
* To create a stock of products to be sold online and keep track of the sales as an admin.
* To be able to create/update/delete products and their details as an admin
* To enable users to create an account for future purchases with saved records.
 
#### User Goals ####
 
* To navigate the web application easily and understand its purpose.
* To filter products and their information (name,price, size, category) fast and easy through a website search or through the navigation bar by categories.
* To be able to buy products online as a guest or a registered user.
* To receive a confirmation email to ensure purchase was successful.
* To be able to create/update my profile.
* To view my order history.
* To leave a comment on blog posts and share my opinions.
* To contact customer service through the contact page.
 
<a name="Scope"></a>
### Scope ###
 
The users should be able to conduct the following actions on the website:
 
* Use the navigation bar effectively on all devices including desktop and mobiles.
* Conduct a product search by category, description and name in the search bar and get relevant results.
* View individual product details when selected.
* Add/remove multiple items to/from the shopping bag.
* Get an update of the shopping basket status when adding or removing items.
* Purchase products securely through a payment platform.
* Create and Update profile  with personal information.
* View blog post comments as guest users, post comments as registered users.
 
As an Admin:
* Add, edit, delete a product and its details.
* Add, edit, delete a blog post and its details.
* Delete comments that violate the site policy.
* View order details
* View messages from users
* Manage user accounts
 
<a name="wireframes"></a>
 
### **Skeleton**
 
At this point I began creating wireframes, using the above structure considerations. I used [Balsamiq](https://balsamiq.com/) these below;
 
Please click [here](README/cryptocourse-wireframe.pdf) to see wireframes for this project.
 
<a name="design"></a>
 
### **Surface**
 
This is the sensory design section of a website, or how it looks, feels and sounds.
 
#### **Colour & Styling**
 
The site is created to allow users purchase cryptocurrency courses and related merchandise  to learn about cryptocurrency. This site also contains a blog section, which offers original coverage of the global blockchain and cryptocurrency news, provides opinions, reviews, guides, and introduces Crypto to people with an aim to help the general public understand and successfully use these technologies now and in the future. Hence this site is branded in a very simple classic design with black text on white background to ensure optimal legibility and minimal distraction. I chose to use a colour palette consisting of whites and black shades, with grey to highlight and  for the hoovering effects.
 
The resulting palette is below;
 
![Crypto Course Color Scheme](assets/README/images/color-palette.jpg)
 
##### Colour Palette
 
* White - #fff
* Black - #111
* Black- #000
* Dark gray- #A9A9A9
* Davy grey - #555
 
 
#### **Language/Tone**
 
I wanted the language to reflect a professional and educational atmosphere, whilst also reflecting a friendly and engaging style. Therefore content was written in this style, avoiding overloading of information or information that is too technical to understand.
 
Similarly, I wanted to use fonts that reinforce the identity of the site,  to match the cryptocurrency theme and also be easy to read. To achieve this I used [Google Fonts](https://fonts.google.com/);
 
* [Roboto](https://fonts.google.com/specimen/Roboto) - Roboto has a dual nature. It has a mechanical skeleton and the forms are largely geometric. At the same time, the font features friendly and open curves.
* [Sans Serif](https://fonts.google.com/?category=Sans+Serif) - This font is used as a fall back should the Roboto font fails.
 
#### **Styling Considerations**
 
During the pre-development phase, I listed out some styling ideas that I thought would be beneficial to the website. Many of these can be found in wireframes.
 
* Font Awesome Icons : with hover effects to highlight key info
* Navigation
* Sticky top Navigation Bar
* Mobile Side Nav: 'Burger' menu icon, expanding into side navbar on click
* Product Cards displaying products
* Visual Image showing product
* Visual Image to accompany blog content
* Forms for registration, login, logout, contact and checkout
 
### Defensive Design ###
 
1. All required form inputs display a warning message as a tooltip if the field is filled incorrectly.
2. If a non-registered user tries to access the profile, Product/ Blog Management page, they will be automatically redirected to the sign-in page.
3. Each time a form is submitted (search, product, shopping bag, comment, account), the user is notified of the action success/failure through a toast message.
4. Implementation of webhooks to create order status in the database and avoid any errors from the user during checkout.
5. Custom error pages redirecting to homepage.
6. Default images for blog posts and products if the image selected is broken or if no image was uploaded.
 
<a name="technologies"></a>
 
## Technologies ##
---
 
### Languages and Frameworks
<ul>
<li><a href="https://en.wikipedia.org/wiki/HTML">HTML</a> - Programming language providing content and structure of the website.</li>
<li><a href="https://en.wikipedia.org/wiki/CSS">CSS</a> - Programming language providing styling of the website.</li>
<li><a href="https://en.wikipedia.org/wiki/JavaScript">JavaScript</a> - Programming language used for various interactive elements of the website, including game logic, audio options etc.</li>
<li><a href="https://en.wikipedia.org/wiki/Python_(programming_language)">Python</a> - Programming language used to drive core site functionality including user login and push/retrieving database information.</li>
<li><a href="https://github.com/django/django">Django</a> - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.</li>
<li><a href="https://www.sqlite.org/index.html">SQLite</a> - SQLite is a C library that provides a lightweight disk-based database that doesn't require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language.</li>
</ul>
 
### Libraries
<ul>
<li><a href="https://fontawesome.com/">Font Awesome</a> - Library used for icons, such as social links and other images.</li>
<li><a href="https://fonts.google.com/">Google Fonts</a> - Font style library.</li>
<li><a href="https://jqueryui.com/">jQuery</a> - JavaScript library used for simplification of JS scripts and DOM manipulation.</li>
<li><a href="https://flask.palletsprojects.com/en/1.1.x/">Flask</a> - Micro-framework to simplify Python scripting and web server tasks.</li>
<li><a href="https://werkzeug.palletsprojects.com/en/1.0.x/">Werkzeug</a> - Python library to manage user management integrity.</li>
</ul>
 
### Editors
<ul>
<li><a href="https://github.com/">GitHub</a> - Remote code repository.</li>
<li><a href="https://gitpod.io/">GitPod</a> - IDE (Integrated Development Environment), for writing, editing and saving code.</li>
<li><a href="https://balsamiq.com/">Balsamiq</a> - Wireframes for visual design testing.</li>
</ul>
 
### Tools
<ul>
<li><a href="https://getbootstrap.com/">Bootstrap</a> -
Bootstrap is a free and open-source tool collection for creating responsive websites and web applications. </li>
<li><a href="https://jquery.com/">JQuery</a> -
Bootstrap is a free and open-source tool collection for creating responsive websites and web applications. </li>
<li><a href="https://developer.chrome.com/docs/devtools/">Chrome DevTools</a> - Chrome DevTools is a set of web developer tools built directly into the Google Chrome browser.</li>
<li><a href="http://ami.responsivedesign.is/">Am I Responsive?</a> - Responsive design demo in ReadMe summary.</li>
<li><a href="https://www.responsivedesignchecker.com/">Responsive Design Checker</a> - Check website response across device types.</li>
</ul>
 
### Deployment Platform
<ul>
<li><a href="https://www.heroku.com/">Heroku</a> - Remote hosting platform, for hosting of python driven websites and applications.</li>
</ul>
 
 
<a name="Features"></a>
 
## Features ##
---
The site allows users to register for an account, view and purchase products. Reigstered users are able to login/logout and to reate, upload and update their own profiles with saved records for future purchases or to view order history. Users are able to view blog posts and registered users are able to leave comments on blog posts. Admin is able to add, edit or delete products, blog posts and its comments. Admin is able to view any orders made and accounts registered.
 
### CRUD Functionality
- Add profile
- Edit profile
- Add Products
- Edit Products
- Delete Products
- Add items to bag
- Edit items quantity in bag
- Delete items in bag
- Add blog posts
- Edit blog posts
- Delete blog posts
- Add comments
- Edit comments
- Delete comments
 
<a name="existing"></a>
 
### Existing Features per Apps ###
 
**Responsiveness**
 
* This website was built with the use of Bootstrap, CSS and Media Queries to ensure responsiveness across all devices so users are able to consult the website from any of their devices.
 
* Responsiveness across different devices have been tested. Please read more in [TESTING.md](TESTING.md).
 
**Navigation bars**
 
* This feature enables the user to navigate the site easily and intuitively, as well as login/register their account.
 
* This project has two responsive navigation bars present on all pages:
1. Main navigation bar:
* Search bar - Users can search for products by name, description and category.
* Dropdown menu: Users can register for an account, signin and signout. When logged in as a registered user, the menu links to the profile app and the logout page. When logged in as an admin, the dropdown links to the product and blog management pages along with the profile app and the sign out page.
* Shopping bag: Update shopping bag once an item is added to the bag and displays the grand total price.
 
2. Product Categories/Blog/Contact navigation bar:
* This navigation bar displays the store's available products by different categories.
* The user can navigate to the blog section and the contact page.
 
**Home App**
 
* This features a landing page with a background video related to cryptocurrency taking up the full viewport. This feature is an attractive way to attract customers and keep them engaged and potentially learn something about cryptocurrency.
* The landing page includes a call to action button to visit the store where available products will be displayed.
 
**Shopping bag App**
 
* This feature enables the user to add/edit (quantity/size) /remove various products to/from the shopping bag, and view the grand total price and details of items in the bag.
* When a product is added to the shopping bag, a preview of the shopping bag is displayed in a toast and the total price/shipping price is updated.
 
**Checkout App**
 
* This feature enables the user to securely make purchases of the available products on the site using  **Stripe**.
* Guest users are allowed to make purchases to encourage sales as some users might feel it is too time consuming to create an account and be discouraged to make any purchases.  If logged in,  the profile and delivery details will be filled automatically from the records saved in their user profile.
* If profile detail is changed in the checkout form when logged in, the user has the option to check the Remember checkbox and all details will be updated in the profile app.
* The credit card details payment section is connected to the payment platform **Stripe** to ensure a secure payment procedure.
* Once the buy button is clicked it triggers a custom loading animated screen that will remain while Stripe checks the credit card details.
* If the payment fails, the user is redirected to the checkout form and informed of the error.
* If the payment succeeded, the user will be sent a confirmation email with the order details and the order number. Users will then be redirected to the checkout success page where order details will be displayed.
 
**Product App**
 
* This feature enables the user to view all products and individual's product details on the site. Admin is permitted to Add/Edit/Delete products to/from the database.
 
1. Products page:
* The user can browse by product categories through the navigation bar. Users can filter and search for products by entering a keyword to browse items more specifically.
* Sale's alert section is featured on this app to notify shoppers of any discounts that they could potentially use when the discount feature is implemented in the future.
* Shopping information displayed at the bottom of all the available products.
* The products displayed can be sorted out by name, price, rating and category.
 
2. Product detail page:
* This page displays individual product details including name, category, image, rating, description, price and sizes (if any)).
 
3. Product management:
* Only Admin is allowed access to the Product management page through the dropdown menu on the navigation bar to add a new product to the database by filling the add product form. Images can be uploaded directly or users can provide image url.
* Only Admin is allowed to edit or remove any product by clicking on relevant buttons in the products card. The edit button redirects Admin to edit product form whilst the delete button triggers a confirmation modal and permanently removes the product from the database when the action is confirmed.
 
**Profile App**
 
* This feature permits the user to create a custom profile on the website and have their details saved onto the database. Logged in users will be given registered user privileges (comment on blog posts and saved checkout details).
1. Registration
* Guest Users can register an account through the Register form page. They will be required to submit a valid email address, a username and a secured password.
* The email and password is required twice for confirmation and to avoid typos.
* A verification email will be sent to the user's email when the form is successfully submitted. That email contains a security link which redirects to a "confirmed email" page to show successful registration. The user record is stored onto the database and will be filled in automatically for any future purchases.
 
2. Signin in.
* Registered users can sign in through the sign in page through the link on the navigation bar. They will be required to fill in their email or username along with their password on the login form to be allowed access to registered user's privileges on the site.
* Registered Users can also reset their password if forgotten and will be sent a link to do so via email.
* Once the login form is submitted successfully, the user is redirected to their profile page containing their personal information.
 
3. Sign out
* Logged in users can easily sign out by accessing the logout page via the navigation bar and will be asked to confirm their intention to log out. The user is then redirected to the home page.
 
4. Profile Page:
* The profile page can only be accessed by the specific logged in user. It is personal and contains:
   - An editable personal details form including the shipping details which will be automatically filled in at checkout when signed in.
   - An order history with order number, date and order details. The order number redirects to the order confirmation page.
 
**Blog App**
 
* This feature allows the user to be informed of global blockchain and cryptocurrency news, provide opinions, reviews, guides and introduce Crypto to people with an aim to help the general public understand and successfully use these technologies now and in the future.
 
1. Blog page:
* The blog page can be accessed through the navigation menu and contains all blog posts. Users can access individual blog content by clicking the Read More button.
* Blog introduction section is featured on this app to inform users what this app can offer.
 
2. Blog detail page:
* The blog detail page displays the full blog post (title, image, content, author and published date) as well as the comment section. All users can read the blog post. Only logged in users are allowed to leave comments. Admin have the option to remove any comments that violate the site's policy.
 
3. Blog management:
* Admin have access to the Blog management page through the profile dropdown menu in the main navigation bar. Admin is permitted to add a blog post to the blog page/database by filling the add blog post form. Images can be selected directly from the user's computer or users can provide image urls.
* Only the admins can edit and/or delete any blog post by navigating to a blog detail page and clicking on the edit/delete buttons. The edit link redirects to an edit form while the delete link triggers a confirmation modal and deletes the post permanently when action is confirmed.
 
**Contact App**
 
* This feature allows the user to contact the site owner for customer service.
 
* The Contact page allows the send a message to the Admin by submitting a form on the contact page. The query is then stored in the database and two email alerts are sent: one to the user to confirm that the message was received and one to the admin to notify the reception of a new query. The email sent to the admin contains all details given by the user in the contact form.
* All site users can send a message to the site owner. No registration is required.
 
### Testing ###
The testing process can be seen in the [TESTING.md](testing.md) document.
 
<a name="future"></a>
 
### Future Features ###
 
* Stock feature to handle stocks of products
* Discount feature to allow users to receive discounts
* Direct Access to online course materials on the site once payment is made
* Chat function to allow registered users to connect with each other
* Favourite Product / Wishlist feature to allow users to save their favourite products for future purchases
* Review feature for the products
* Verified Purchases so that only customers who have previously purchased the item can review the specific item.
* Apple Pay payment feature to allow ease of checkout process to encourage more revenue
* Advanced styling on the site to make it more attractive
* Allow all registered users to add / edit blog posts
 
## Deployment ##
---
<a name="requirements"></a>
 
### Application Hosting
### **Heroku**
 
The site is hosted using [Heroku](https://www.heroku.com/), deployed directly from the master branch of GitHub. The deployed site will update automatically as new commits are pushed to the master branch.
 
This project can be viewed live on :http://cryptocourse.herokuapp.com/
 
### Requirements ###
 
* an IDE - I recommend using Gitpod.
* PIP3, for Python packages.
* Python3
* Git for version control.
* A Django Secret Key. You can generate your unique one here [here](https://djecrety.ir/).
* Stripe (account, test keys and webhooks) as a secure payment platform.
* AWS cloud storage and an S3 bucket for storage of static files.
* An email address STMP server password or passkey, I recommend using Gmail.
 
The project was set up on GitHub using the Code Institute Gitpod Template.
 
<a name="locald"></a>
 
### Local Deployment ###
 
<a name="herokud"></a>
 
**1. Clone from Github**
 
To deploy locally on your preferred Desktop IDE, you can clone the repository to your desktop by the following steps.
 
1. Go to [Crypto Course github page](https://github.com/tindyc/crypto_course).
2. Above the list of files, click on the **code** button.
3.
   - To clone the repository using **HTTPS,** under "Clone with HTTPS", click the paste icon.
   - To clone the repository using an **SSH key**, click Use SSH, then click the paste icon.
   - To clone a repository using **GitHub CLI,** click Use GitHub CLI, then click the paste icon.
4. Open your preferred Terminal interface.
5. Change the current working directory to the location where you want the cloned directory.
6. Type **git clone**, then paste the URL you copied earlier above. The example below is HTTPS for a Windows PC.
 
   ```bash
   git clone https://github.com/tindyc/crypto_course.git
   ```
 
7. Press Enter to create your local clone. more detailed instructions are available [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
 
**2. Install Python required modules**
 
* run the command below to install all the module required to run this project:
 
``pip3 install -r requirements.txt``
 
**3. Store environment variables**
 
* Using IDE or Gitpod, create env.py file in the root directory of the project and include the following:
 
```
import os
 
os.environ["STRIPE_PUBLIC_KEY"] = "YOUR_STRIPE_PUBLIC_KEY"
os.environ["STRIPE_SECRET_KEY"] = "YOUR_STRIPE_SECRET_KEY"
os.environ["STRIPE_WH_SECRET"] = "YOUR_STRIPE_WH_SECRET"
os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY_HERE"
os.environ["DEVELOPMENT"] = "True"
```
 
* Follow these instructions to fill in the values of each keys:
   - the SECRET_KEY
   - the STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY can be found on the Stripe Dashboard in the Developer's API section.
   - the STRIPE_WH_SECRET: Can be found in the Developer'sAPI section after creating a webhook.
 
**4. Migrate database models**
 
* Run the commands below to migrate the models and set up an SQLite database:
 
````
python3 manage.py makemigrations
python3 manage.py migrate
````
 
**5. Load categories and products**
 
* Run the command below in that exact order to load category then product fixtures:
 
````
python3 manage.py loaddata categories
python3 manage.py loaddata products
````
 
** Please note to load the categories data first before loading the products data. The products data are dependent on the categories data.
 
**6. Create Superuser**
 
* A superuser is required to access the admin panel in Django. Run the command below and follow the instructions after (email and password required):
 
````
python3 manage.py createsuperuser
````
 
**7. Run the app**
 
* Enter the command below to start running the project locally :
 
````
python3 manage.py runserver
````
 
 
### Heroku Deployment ###
 
**1. Signup and login to Heroku**
 
* Create an account on [Heroku](https://heroku.com/) or sign in to existing account.
* Create an app with a unique name and choose your location.
* Navigate to the Resource tab and create a free Postgres database. From the add-ons search bar, add the Heroku Postgres DB, select the free account, and then submit an order form to add it to the project.
 
**2. Prepare the database**
 
* The DATABASE_URL variable was automatically created in the Settings< Config Vars section. Copy its value and temporarily add it to your environment variables in your IDE or your env.py.
 
* From the Heroku app's dashboard, navigate to Settings and set the necessary configuration variables for the project. It should look like this:
 
| Key                   | Value                      |
|-----------------------|----------------------------|
| AWS_ACCESS_KEY_ID     | Your AWS Access Key        |
| AWS_SECRET_ACCESS_KEY | Your AWS Secret Access Key |
| DATABASE_URL          | Your Database URL          |
| EMAIL_HOST_PASS       | Your Email Password        |
| EMAIL_HOST_USER       | Your Email Address         |
| SECRET_KEY            | Your Secret Key            |
| STRIPE_PUBLIC_KEY     | Your Stripe Public Key     |
| STRIPE_SECRET_KEY     | Your Stripe Secret Key     |
| STRIPE_WH_SECRET      | Your Stripe WH Key         |
| USE_AWS               | TRUE                       |
 
* You can now make the migrations to start using Postgres:
``````
python3 manage.py makemigrations
python3 manage.py migrate
``````
* And load the category the product fixtures:
``````
python3 manage.py loaddata categories
python3 manage.py loaddata products
``````
 
**3. Create a Superuser for mew Postgres database**
 
* Run the following command to create a superuser to navigate to Django's admin panel:
 
``````
python3 manage.py createsuperuser
``````
 
**4. Create Procfile**
 
* Create a Procfile and add ``web: gunicorn crypto_course.wsgi:application`` then save.
* Push all changed files to Github by running the following commands:
```````
git add .
git commit -m "..."
git push
```````
 
**5. Remove DATABASE_URL variable**
 
* Delete the temporary DATABASE_URL from your environment variables or env.py.
 
**6. Install Heroku CLI and login**
 
* In case your environment doesn't have it already, run this command to install the Heroku CLI in your terminal:
 
``````
$ heroku login
``````
* To login from the CLI run the following command in your terminal:
```````
heroku login -i
```````
 
**7. Settings**
 
* Add the hostname of your Heroku App to "ALLOWED HOSTS" in settings.py. the Hostname can be found in the heroku settings < App Name .
 
**8. Connect repository to Heroku**
 
* 1. You can connect your Github repository directly in the Heroku app by selecting your repository in the Deploy tab < Deployment method. I recommend selecting the Automatic Deployment option for convenience. Click on Deploy.
 
* 2. Copy the Heroku git url in the Heroku app Setting tab and run the command below to connect your repository:
 
```````
$ git remote add heroku <your heroku git url>
```````
 
**9. Add static files to AWS S3**
* In your S3 Bucket, create a 'Media' folder and upload all your media files.
* Select to grant public access
* Click to upload your files
* Create a 'Static' folder in the same bucket
* Django will collect all static files and upload them to S3 as soon as the app is deployed to Heroku
 
**10. Push to Heroku**
 
* If you have decided to connect your Github repository to heroku and selected the automatic deployment option, commit and push will be pushed to Heroku.
 
* In other scenarios , use the following command:
 
```````
$ git push -u heroku master
```````
 
The app can now be open at https://< your-app-name >.herokuapp.com/
 
<a name="credits"></a>
 
## Credits and References ##
---
 
**Text Credits:**
 
All product details were taken from :
- [Udemy](https://www.udemy.com/topic/cryptocurrency/) for the online courses
- [Amazon](https://amazon.co.uk/) for the books
- [Ledger](https://www.ledger.com/) for the merchandise
 
All blog posts were taken on her official website:
- [Cointelegraph](https://cointelegraph.com/)
 
 
**Image Credits:**
 
Some products images were taken from:
- [Amazon](https://amazon.co.uk/) for the books
- [Ledger](https://www.ledger.com/) for the merchandise
 
-Product images for the online courses, blog post banner and sales banner were using [Canva](https://www.canva.com/).
 
**Video Credits:**
 
- [Cryptocurrency: The Future of Finance and Money](https://www.youtube.com/watch?v=IWeCQkIJNkY) for the landing page video.
 
**Code Tutorials Credits**
 
* This full stack project was developed following the tutorials of Code institute for the Boutique Ado project by Chris Zielinski.
 
* The video landing page was inspired by [Full Screen Video Landing Page Tutorial with HTML5 and CSS3](https://www.youtube.com/watch?v=a7i502YEBNQ) by w3newbie.
 
 
**Acknowledgements:**
 
* Thanks to my mentor, [Tim Nelson](https://github.com/TravelTimN) for his encouragement and expert advise on the development of this project.
* Thanks to all the tutors on Code institute for their constant support, time and patience.
* Thanks to those on the Slack community for answering my many questions 24:7!
* Thanks to my two sons - Chubby and Klaus, friends and family for the love and support, reviewing the app and offering constructive feedback.


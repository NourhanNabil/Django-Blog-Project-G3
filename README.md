# Django Blog


#### Landing Page Content:

- Header:
Will contain Two links `Login/Register`. If the user is already logged in,
then the link will be `Logout`. And If the logged-in user is an admin,
then there will be another link called `Manage Blog` that will redirect
the admin to the administration page to make the admin CRUD
Operations.
- Sidebar:
Will contain all the available `categories`.
(example: Sports, News, Politics, ...) with a button beside them be
`subscribe` or `unsubscribe` if the user is already subscribed to this
category.
when a category is chosen it will be redirected to a page that contains
all the posts belonging to this category. Sorted by date of publish
- Body:
Will have `top posts` sorted by publish date.
when clicking on the image of a post. it will redirect to the post’s
page.
- Footer: 
Will have a pagination part where each page will contain only the top
5 posts sorted by publish date.
When clicking on Next it will get me the next 5 posts.

#### Registration Page:
- It will be a form that takes:
    - Username
    - Email
    - Password
    - Password Confirmation (two must match)
    
#### Login Page:
- It will be a form that takes:
    - The form contains 2 fields. `Username & PW`.
    - Password will be shown in asterisks. when the user clicks on
        login, if he is blocked then redirect him back to the login page
        with a message (sorry you are blocked contact the admin)
    - if he isn’t blocked then he will be authenticated.
    - 
#### Post Page Content:
- Title
- Post Picture
- Content of the post
- The category that this post is under
- Comments section
- Tags related

#### Post Page Characteristics:
- Each comment shows the time of the comment and the
username who wrote the comment.
- Add comment Section. User must be signed in to can submit a
comment (enter the text and a submit button to submit the comment)
- If the comment contains inappropriate words, it will show like ******
- Like and dislike counter on the posts.

#### Normal user characteristics:
- He can see posts and categories
- Search by tag name, post title.
- If logged in he can like, dislike, comment, and reply to a comment on
a post.
- If blocked, he cannot log into the system on the login page
(Your account is locked, please contact an admin.)

#### Admin user characteristics:
- Admin users can make CRUD on posts.
- Admin user can make CRUD on categories
- Admin users can block or unblock users.
- Admin users can promote a normal user to an admin user so that he
will be able to log into the admin screen.
- Admin users can CRUD on forbidden words.
- The Admin page will contain links
( users, posts, categories, forbidden words ).
- When Admin clicks on the Posts Link, it would list all posts, with links
to edit, delete and create.
The same will be applied to categories, forbidden words.
- When Admin clicks on Users Link, it would list all the users, in case
The user is also an admin, his row will be colored red. Else it will be a
normal row. Or display is Admin equals to True.
- For normal users, there should be a button that enables the admin to
either lock or unlock this user from logging into the system. And for
the Admin users, this button is not available So, an admin cannot lock
another admin.

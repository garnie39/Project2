# Project 2: A+ SHOWCASE

For Project 2, I'm required to create 2 database's tables, use CRUD ops and implementation of the Flask session as well as Jinja templates with CSS stylesheet then deploy online.

[Check it out](https://garnie-project2.onrender.com/signup)

## Project Description
I have got inspired by a few of my friends who call themselves artist but feel it was too complicated to join in NFT for digital Coin purchase digital Art.
I thought it would be fun to try create the space where they can feel comfortable on selling their art online. I will walk you through:

### Firstly, You need to sign up in order for you to be able to interact inside:
![alt text](https://github.com/garnie39/Project2/blob/master/images/Screen%20Shot%202023-05-14%20at%205.54.08%20pm.png?raw=true)

### You will be directed to Login page:
![alt_text](https://github.com/garnie39/Project2/blob/master/images/Screen%20Shot%202023-05-14%20at%205.54.22%20pm.png?raw=true)

### Now you be able to see all posts on the Feed's page:
![alt_text](https://github.com/garnie39/Project2/blob/master/images/Screen%20Shot%202023-05-14%20at%203.30.21%20pm.png?raw=true)

### Of course! you create your post:
![alt_text](https://github.com/garnie39/Project2/blob/master/images/Screen%20Shot%202023-05-14%20at%206.09.36%20pm.png?raw=true)

### Or editing:
![alt_text](https://github.com/garnie39/Project2/blob/master/images/Screen%20Shot%202023-05-14%20at%206.10.13%20pm.png?raw=true)

### Even deleting:
![alt_text](https://github.com/garnie39/Project2/blob/master/images/Screen%20Shot%202023-05-14%20at%206.10.30%20pm.png?raw=true)

### Each of the post will show username who posted, like, however if image is for bid you won't be able to see edit/delete icon:
![alt_text](https://github.com/garnie39/Project2/blob/master/images/Screen%20Shot%202023-05-14%20at%205.55.40%20pm.png?raw=true)

### Everytime when user click on like the number will keep counting total numnber of likes however user click twice, it will reverse back:
![alt_text](https://github.com/garnie39/Project2/blob/master/images/Screen%20Shot%202023-05-14%20at%205.55.25%20pm.png?raw=true)

## Languages
* Python
  * Flask
  * SQL
* HTML
* CSS

## Project discovery
Throughout the project, I have done many research and discoveries many new thing such as
* Working on like and unlike function:
```Python
current_like = item['user_like']
    
    if "None" == current_like:
        current_like = ""
    if str(session['user_id']) in current_like:
        print(current_like)
        if str(session['user_id']) + "," in current_like:
            current_like = current_like.replace(str(session['user_id']) + ",", "")
        else:
            current_like = current_like.replace(str(session['user_id']), "")   
    else:
        if len(current_like) > 0:
            current_like += ","
        current_like += str(session['user_id'])
    print(current_like)
    
    like = common.sql_write("UPDATE showcase SET user_like=%s WHERE id=%s;", [current_like, id])
    result = post.get_post()
  ```
```html
{% if post['user_like'] %}
      <div class="heart-btn-filled">
        <a href="/likes/add/{{ post['id'] }}">
        <svg class="like_filled" fill="hsl(332, 80%, 51%)" height="25px" width="25px" viewBox="-4 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" data-darkreader-inline-fill="" style="--darkreader-inline-fill: #242424;"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <title>heart</title> <path d="M18.188 6.094c5.188 0 6.906 6 5.094 9.281-2.781 5.094-11.281 10.5-11.281 10.5s-8.531-5.406-11.281-10.5c-1.813-3.281-0.125-9.281 5.094-9.281 4.813 0 6.031 4.156 6.188 4.781 0.156-0.625 1.375-4.781 6.188-4.781z"></path></g></svg></a>
        <p class="totallike">{{ post['total_like'] }}</p>
      </div> 
      {% else %}
      <div class="heart-btn-unfilled">
        <a href="/likes/add/{{ post['id'] }}">
        <svg class="like_unfilled" width="25px" height="25px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <g id="Interface / Heart_01"> <path id="Vector" d="M12 7.69431C10 2.99988 3 3.49988 3 9.49991C3 15.4999 12 20.5001 12 20.5001C12 20.5001 21 15.4999 21 9.49991C21 3.49988 14 2.99988 12 7.69431Z" stroke="rgb(87, 50, 154)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g> </g></svg></a>
        <p class="totallike">{{ post['total_like'] }}</p>
      </div> 
      {% endif %}
```
* How to add icon without using Javascript
```html
<a href="/form/edit/{{ post['id'] }}"><svg class="edit" width="25px" height="25px" stroke-width="1.5" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M13.0207 5.82839L15.8491 2.99996L20.7988 7.94971L17.9704 10.7781M13.0207 5.82839L3.41405 15.435C3.22652 15.6225 3.12116 15.8769 3.12116 16.1421V20.6776H7.65669C7.92191 20.6776 8.17626 20.5723 8.3638 20.3847L17.9704 10.7781M13.0207 5.82839L17.9704 10.7781" stroke="rgb(87, 50, 154)" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
```
## Future improvement
Due to tight time limited, I couldn't be able to do as much as I expected for this project but here are the development list that I would like to continue in the future:
1. Complete the function for user to purchase coins on their preferences payment methods.
2. Allow user to upload their image from their local laptop and to make sure on size limit to support the website to run smoothly.
3. Add in time limit for "Bid" post and the post's created at time.
4. Allow user to add comment on the post.
5. Make an individual page for each post for user to enjoy in the biger screen and to see details on the post clearly.

## Credit
I won't be able to complete this project with out help from GA's team, so I would like to use this space to thank Vishal, Beiwei, Adora, Chelsie and the team for being so patient on guiding me throughout the project.

## Resource
[Like button](https://www.youtube.com/watch?v=B8nOgu4nvD8&t=175s)
[SVG icon](https://chenhuijing.com/blog/the-many-methods-for-using-svg-icons/#👟)
[Upload from local](https://geekpython.in/render-images-from-flask)

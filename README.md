# Coffee Shop Full Stack

This project is mainly target for user authentication and authorization with Auth0 and RBAC flow. UI is writtern by angular and This is include following functinality:

- Barista Role
  - Can see the menu of coffee
  - Can see the detail of coffee
- Manager Role
  - Can create the new coffee type
  - Can edit the coffee
  - Can delete the coffee
  - Can see the coffee menu

### AUTH0 Account

```Python3
AUTH0_DOMAIN = 'lwincoffeeshop.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'coffeeshop'
```

### Manager Account

```Python3
Username = manager@testing.com
Password = Lwinmoe!23
Token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxhX1RlS212WHpELUZNZzhGVzlfZSJ9.eyJpc3MiOiJodHRwczovL2x3aW5jb2ZmZWVzaG9wLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MTM0MmRhNThmZmI3NDAwNzFkYTBiODkiLCJhdWQiOiJjb2ZmZWVzaG9wIiwiaWF0IjoxNjMwOTE2NTI1LCJleHAiOjE2MzA5MjM3MjUsImF6cCI6IjB0djBMZXByQTljdzZBWkFiUFRFTjFlbW9CVFRpdllBIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.1TNQoEeMkGmdQ8jCRWuv7CK6eMLnimcXB-DhcJz0BKzfXoDidGfu1jMtOdQRJ76iPtMDPhSh9rRVlWgq8wlImBPMophpVtWIXfQy4_sd1xW8PPUfO_KkwCchZEjmaBTT6FbiBL4KXJKCxfrChMOBjp-Rq2lWGZboJfiC91qzYFF4f-tRwvZwfVc-1P7t3xi8BKGF_BdlV2L0KY_2HUXmsVUALoW1AjvJFcbBw6hQKsEpO9BmcopnBKcE_JnJJ6k8Sm0PWN2StTM5iDLVQBEPS7Q0VwSDPrvOo7qTsArHlwOsazcBhzR4fc4yl3BRfwocY3No52XiFg5-bbi2uyUzaw'
```

### Barista Account

```Python3
Username = user@testing.com
Password = Lwinmoe!23
Token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxhX1RlS212WHpELUZNZzhGVzlfZSJ9.eyJpc3MiOiJodHRwczovL2x3aW5jb2ZmZWVzaG9wLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MTM0MmQ3MjY5MDk3ODAwNmMzZGZjNmQiLCJhdWQiOiJjb2ZmZWVzaG9wIiwiaWF0IjoxNjMwOTE2MzI5LCJleHAiOjE2MzA5MjM1MjksImF6cCI6IjB0djBMZXByQTljdzZBWkFiUFRFTjFlbW9CVFRpdllBIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.vs6jUJcX42Paw9SpmqPN4N0NrfXMlvTybLdpoiZd-d-AratoBymkBHPAmppDQZfu27clreQ3djzrIszH3NZ2zlrg_Q-Fj4371R34ZGMxVRCa7jAsyHQVWYtdFJafdUgA5e8xGbzeIqHLUL2bQxuKk4m5wr1oDKDFbLHRhQsT1qsXGZIqviQ6WTm3zXtgvdAcIpwAB3KLkE68QRJ9S8md7WFT1Com1ZwP1e9YguqMRW-lbyY3vQ3vZxfufmw70iORf0gnils9ipUv4GvYRNv159i1ukx-5wm1XIjsUgovZKT4B89f9Q2_akgLMxKTh5M_dxyW8SlYYu59aVHAmRPduw'
```

## Full Stack Nano - IAM Final Project

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. But they need help setting up their menu experience.

You have been called on to demonstrate your newly learned skills to create a full stack drink menu application. The application must:

1. Display graphics representing the ratios of ingredients in each drink.
2. Allow public users to view drink names and graphics.
3. Allow the shop baristas to see the recipe information.
4. Allow the shop managers to create new drinks and edit existing drinks.

## Tasks

There are `@TODO` comments throughout the project. We recommend tackling the sections in order. Start by reading the READMEs in:

1. [`./backend/`](./backend/README.md)
2. [`./frontend/`](./frontend/README.md)

## About the Stack

We started the full stack application for you. It is designed with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask server with a pre-written SQLAlchemy module to simplify your data needs. You will need to complete the required endpoints, configure, and integrate Auth0 for authentication.

[View the README.md within ./backend for more details.](./backend/README.md)

### Frontend

The `./frontend` directory contains a complete Ionic frontend to consume the data from the Flask server. You will only need to update the environment variables found within (./frontend/src/environment/environment.ts) to reflect the Auth0 configuration details set up for the backend app.

[View the README.md within ./frontend for more details.](./frontend/README.md)

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
Token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxhX1RlS212WHpELUZNZzhGVzlfZSJ9.eyJpc3MiOiJodHRwczovL2x3aW5jb2ZmZWVzaG9wLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MTM0MmRhNThmZmI3NDAwNzFkYTBiODkiLCJhdWQiOiJjb2ZmZWVzaG9wIiwiaWF0IjoxNjMwODQ3NDE4LCJleHAiOjE2MzA4NTQ2MTgsImF6cCI6IjB0djBMZXByQTljdzZBWkFiUFRFTjFlbW9CVFRpdllBIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.mF4QFGu-aEVkGNIX8FPxH_uxzoTtXIuWUWqPkypKbtxR5DRE8-KZJAHp5xZ4aRKcQCPQu3tWqAZxUfhO5-mrDicxMBtY_Pi-gNV8mBndDbBp1pULnHbwdnVcAHMsJr6QqXky3zTUFvQ2ay46WHERjBbruP8WJ2GbHzh0JLwvhnYkZnJe2KpUbDq_ODNoI9ZZ2Yap78a2x-9jRR_sJM9ywVQ87XUWurHUcAyxHAD1tLIM-jFiTe-AyJBbvJ_LIUb1XXajuvAiDJ4fvx-MvQ0TMYAg_pBbO8OnsFJe7obXeuPEnDNhYV5L2JL8cpFUl0Bz1Zk4-9-mZPPe6Kju3hmn2g'
```

### Barista Account
```Python3
Username = user@testing.com
Password = Lwinmoe!23
Token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxhX1RlS212WHpELUZNZzhGVzlfZSJ9.eyJpc3MiOiJodHRwczovL2x3aW5jb2ZmZWVzaG9wLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MTM0MmQ3MjY5MDk3ODAwNmMzZGZjNmQiLCJhdWQiOiJjb2ZmZWVzaG9wIiwiaWF0IjoxNjMwODQyNDAxLCJleHAiOjE2MzA4NDk2MDEsImF6cCI6IjB0djBMZXByQTljdzZBWkFiUFRFTjFlbW9CVFRpdllBIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.tPeO3u_tw7PboPT8oSfNWkOqpNc4vPKlvgeRNiss_d-yxJIWGfP7q4Qk8QgTU_DQCdWrqEMPxfZGi0eTaUiK4rBEQRDt2p0JORWvI92LUn9UY1FwELbshP7XSYfC-HtiIdkRDGSK1axv3orFl6TSYKwUcF10msLWCycrmya75lloc6EkTaq5Vzm-NnCmH907_Ru7Pfq3B9OHvKlNUGErTpPUw558Zj0XoyM1Zf1DrH_TypWuSg8EDttcVEtJl6L-I5C8p6pNhjy4vIcQAB90kHlybT0UTLM1i8VfZVoLOfHkEgJ-wwHtum5Ypom9jZY_m2I--GAJoVT27MIZPVt12w'
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

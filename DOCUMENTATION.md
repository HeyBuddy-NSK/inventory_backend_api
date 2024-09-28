#### **API Endpoints Documentation**

1. **User Registration**
   - **Endpoint**: `/api/register/`
   - **Method**: `POST`
   - **Description**: Register a new user.
   - **Request Body**:
     ```json
     {
         "username": "testuser",
         "password": "password123"
     }
     ```
   - **Response**: `201 Created`

2. **User Login**
   - **Endpoint**: `/api/token/`
   - **Method**: `POST`
   - **Description**: Obtain JWT token for authentication.
   - **Request Body**:
     ```json
     {
         "username": "testuser",
         "password": "password123"
     }
     ```
   - **Response**: `200 OK` with access and refresh tokens.

3. **Get All Items**
   - **Endpoint**: `/api/items/`
   - **Method**: `GET`
   - **Headers**: 
     - Authorization: `Bearer <access_token>`
   - **Response**: List of items.

4. **Create Item**
   - **Endpoint**: `/api/items/`
   - **Method**: `POST`
   - **Headers**: 
     - Authorization: `Bearer <access_token>`
   - **Request Body**:
     ```json
     {
         "name": "Laptop",
         "description": "High-end laptop",
         "item_id": "LP123",
         "price": 1500,
         "quantity": 5
     }
     ```
   - **Response**: `201 Created`

5. **Update Item**
   - **Endpoint**: `/api/items/<id>/`
   - **Method**: `PUT`
   - **Headers**: 
     - Authorization: `Bearer <access_token>`
   - **Request Body**:
     ```json
     {
         "name": "Updated Laptop",
         "description": "Updated gaming laptop",
         "item_id": "LP123",
         "price": 1600,
         "quantity": 3
     }
     ```
   - **Response**: `200 OK`

6. **Delete Item**
   - **Endpoint**: `/api/items/<id>/`
   - **Method**: `DELETE`
   - **Headers**: 
     - Authorization: `Bearer <access_token>`
   - **Response**: `204 No Content`

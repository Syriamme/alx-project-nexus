# E-Commerce Backend - ProDev BE

## Overview
The E-Commerce Backend project simulates a real-world development environment, emphasizing scalability, security, and performance. This backend system supports an e-commerce product catalog, handling product data management, user authentication, and APIs for filtering, sorting, and pagination.

## Project Goals
- **CRUD APIs:** Build APIs for managing products, categories, and user authentication.
- **Filtering, Sorting, Pagination:** Implement robust logic for efficient product discovery.
- **Database Optimization:** Design a high-performance database schema to support seamless queries.

## Technologies Used
- **Django:** For building a scalable backend framework.
- **MySQL:** As the relational database for optimized performance.
- **JWT:** For secure user authentication.
- **Swagger/OpenAPI:** To document and test APIs.

## Key Features
### 1. CRUD Operations
- Create, read, update, and delete operations for products and categories.
- User authentication and management features using JWT.

### 2. API Features
- **Filtering and Sorting:** Allow users to filter products by category and sort by price.
- **Pagination:** Implement paginated responses for large product datasets.

### 3. API Documentation
- Use Swagger or Postman to generate API documentation.
- Publish hosted API docs for easy frontend consumption.

## Implementation Process
### Git Commit Workflow
- `feat: set up Django project with MySQL`
- `feat: implement user authentication with JWT`
- `feat: add product APIs with filtering and pagination`
- `feat: integrate Swagger documentation for API endpoints`
- `perf: optimize database queries with indexing`
- `docs: add API usage instructions in Swagger`

## Setup and Installation
1. **Clone the Repository:**
```bash
git clone https://github.com/your-repository/ecommerce-backend.git
cd ecommerce-backend
```

2. **Create and Activate Virtual Environment:**
```bash
python3 -m venv env
source env/bin/activate
```

3. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set Up MySQL Database:**
```sql
CREATE DATABASE ecommerce_db;
```

5. **Configure `.env` File:**
```env
DB_NAME=ecommerce_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306
SECRET_KEY=your_secret_key
```

6. **Apply Migrations:**
```bash
python manage.py migrate
```

7. **Run the Server:**
```bash
python manage.py runserver
```

## API Endpoints
### Authentication
- **POST** `/api/auth/register/` – Register a new user
- **POST** `/api/auth/login/` – Log in and receive JWT token

### Products
- **GET** `/api/products/` – List products with filtering, sorting, and pagination
- **POST** `/api/products/` – Create a new product
- **GET** `/api/products/<id>/` – Retrieve a single product
- **PUT** `/api/products/<id>/` – Update a product
- **DELETE** `/api/products/<id>/` – Delete a product

### Categories
- **GET** `/api/categories/` – List all categories
- **POST** `/api/categories/` – Create a new category
- **GET** `/api/categories/<id>/` – Retrieve a single category
- **PUT** `/api/categories/<id>/` – Update a category
- **DELETE** `/api/categories/<id>/` – Delete a category

## API Documentation
- Swagger Documentation: [Hosted Swagger API Docs](http://localhost:8000/swagger/)

## Evaluation Criteria
1. **Functionality:**
   - CRUD APIs for products, categories, and user authentication.
   - Effective filtering, sorting, and pagination logic.
2. **Code Quality:**
   - Clean, maintainable, and well-documented code.
   - Proper database indexing for high-performance queries.
3. **User Experience:**
   - Comprehensive and user-friendly API documentation.
   - Secure authentication implementation.
4. **Version Control:**
   - Frequent and descriptive Git commit messages.
   - Well-organized repository structure.

## Contributing
1. Fork the repository.
2. Create a new branch (`feature/your-feature-name`).
3. Commit your changes (`git commit -m "feat: add new feature"`).
4. Push to your branch (`git push origin feature/your-feature-name`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License.

## Contact
For any questions or feedback, feel free to reach out via email at [roridaniel01@gmail.com]


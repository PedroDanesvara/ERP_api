# 💻📱  Enterprise Resource Planning (ERP API)

Repository referring to an ERP API built in Python using DjangoREST as a framework for building the REST API.


## ⛏️ Installation

Run the project with Python

```bash
  python -m venv venv
  .\venv\Scripts\activate
  pip install -R requirements.txt
  py manage.py runserver
```
    
## 💎 Stacks used

<!-- **Front-end:** ReactJS, TypeScript, React-Router, Redux, Material UI, Axios -->

**Back-end:** Django, Django Rest Framework, Simple JWT


## 📋 API Documentation - Authentication

#### Authentication - Create an Account

```http
  POST /api/v1/auth/signup
```

| Parameter   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `name` | `string` | **Required** |
| `email` | `string` | **Required** |
| `password` | `string` | **Required** |

#### Authentication - Login

```http
  POST /api/v1/auth/signin
```

| Parameter   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `email` | `string` | **Required** |
| `password` | `string` | **Required** |

#### Authentication - Get A User - (_Authentication Required_)

```http
  GET /api/v1/auth/user
```

| Parameter   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `Authorization` | `string` | **Required**. Access Token |


## 📋 API Documentation - Companies - Employees

#### Employees - List Employees of a Company - (_ Authentication Required _)

```http
  GET /api/v1/companies/employees
```

#### Employees - Create An Employee - (_Authentication Required_)

```http
  POST /api/v1/companies/employees
```

| Parameter   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `name` | `string` | **Required** |
| `email` | `string` | **Required** |
| `password` | `string` | **Required** |

#### Employees - Get An Employee - (_Authentication Required_)

```http
  GET /api/v1/companies/employees/${id}
```

| Parameter   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Required**. employee ID |

#### Employees - Edit An Employee - (_Authentication Required_)

```http
  PUT /api/v1/companies/employees/${id}
```

| Parameter   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Required**. employee ID |
| `groups` | `string` | **Optional**. String with a list of ids of different groups |
| `name` | `string` | **Optional** |
| `email` | `string` | **Optional** |

#### Employees - Delete An Employee - (_Authentication Required_)

```http
  DELETE /api/v1/companies/employees/${id}
```

| Parameter   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Required**. employee ID |

## 📋 API Documentation - Companies - Groups / Permissions

#### Groups / Roles - Groups of a Company - (_Authentication Required_)

```http
  GET /api/v1/companies/groups
```

#### Groups / Roles - Create a Group - (_Authentication Required_)

```http
  POST /api/v1/companies/groups
```

| Parameter   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- | 
| `name` | `string` | **Required** | 
| `permissions` | `string` | **Required**. String with a list of IDs of various permissions |

#### Groups / Roles - Get A Group - (_Authentication Required_)

```http
  GET /api/v1/companies/groups/${id}
```

| Parameter   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- | 
| `id` | `number` | **Required**. group ID |

#### Groups / Roles - Edit a Group - (_Authentication Required_)

```http
  PUT /api/v1/companies/groups/${id}
```

| Parameter   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Required**. group ID |
| `name` | `string` | **Optional** | 
| `permissions` | `string` | **Optional**. list of permissions IDs |

#### Groups / Roles - Delete a Group - (_ Authentication Required _)

```http
  DELETE /api/v1/companies/groups/${id}
```

| Parameter   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Required**. group ID |

#### Permissions - Available Permissions - (_Authentication Required_)

```http
  GET /api/v1/companies/permissions
```

## 📋 API Documentation - Companies - Tasks

#### Tasks - Company Tasks - (_ Authentication Required _)

```http
  GET /api/v1/companies/tasks
```

#### Tasks - Create A Task - (_Authentication Required_)

```http
  POST /api/v1/companies/tasks
```

| Parameter   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- | 
| `employee_id` | `number` | **Required**. employee ID | 
| `status_id` | `number` | **Required**. taks status ID |
| `title` | `string` | **Required** |
| `description` | `string` | **Optional** |
| `due_date` | `date` | **Optional**. Date in the format: d/m/Y H:M |

#### Tasks - Get A Task - (_Authentication Required_)

```http
  GET /api/v1/companies/tasks/${id}
```

| Parameter   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Required**. task ID |

#### Tasks - Edit A Task - (_Authentication Required_)

```http
  PUT /api/v1/companies/tasks/${id}
```

| Parameter   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Required**. task ID |
| `employee_id` | `number` | **Optional**. employee ID | 
| `status_id` | `number` | **Optional**. taks status ID |
| `title` | `string` | **Optional** |
| `description` | `string` | **Optional** |
| `due_date` | `date` | **Optional**. Date in the format: d/m/Y H:M |

#### Tasks - Delete a Task - (_Authentication Required_)

```http
  DELETE /api/v1/companies/tasks/${id}
```

| Parameter   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `number` | **Required**. task ID |


<!-- ## Suggestions
    1. impl views CRUD using viewsets.ModelViewSet
    2. add layer to serializers
    3. use Makefile to simplify commands
    4. Use SimpleRouter to auto route views -->
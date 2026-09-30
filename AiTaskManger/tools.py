from langchain_core.tools import tool
from databse import LocalSession, Todo
from datetime import datetime


##CRUD - 

def create_todo(title: str, description: str, priority: str = "medium", due_date:str = ""):
            """
            Create and save a new todo task.

            Args:
                title: Short title for the task(required)
                description: Optional details note of the task
                priority: 'low', 'medium', or 'high' (default medium)
                due_date: Optional due date of task. e.g. '25-03-2026'
            """
            task_priority = "medium"
            if priority.lower() in ['low', 'high', 'medium']:
                    task_priority = priority

            with LocalSession() as session:
                    todo =Todo(
                            title = title,
                            description = description,
                            priority = task_priority,
                            due_date = due_date,
                            create_at = datetime.now().strftime("%d-%m-%Y-%H"),
                    )

                    session.add(todo)
                    session.commit()

                    session.refresh(todo)

                    return f"""
                        Todo created!
                        id: {todo.id} | Title: {todo.title} | Priority: {todo.priority}
                        """


@tool
def list_todods(status: str = "all", priority: str="all"):
        """
        List all todos, Optionally filter by status or priority.

        Args:
            status: 'pending', 'in_progress', 'done', or 'all'
            priority: 'low', 'medium', 'high', or 'all'
        """

        with LocalSession() as sesion:
                query = sesion.query(Todo)

                if status != "all":
                        query = query.filter(Todo.status == status)

                if priority != "all":
                        query = query.filter(Todo.priority == priority)

                todos = query.order_by(Todo.id).all()

                if not todos:
                        return f"No todos for your filter values"

                allTodos = [todo.to_dict() for todo in todos]
                return allTodos
        



@tool
def update_todos(
        todo_id:int, 
        title: str, 
        description: str, 
        status = "",
        priority: str = "", 
        due_date:str = ""):

        """
           Update an existing todo by its ID. Only provide the fields you want to change.

            Args:
                todo_id:     ID of the todo to update (required)
                title:       New title (leave empty to keep current)
                description: New description (leave empty to keep current)
                status:      New status — 'pending', 'in_progress', or 'done'
                priority:    New priority — 'low', 'medium', or 'high'
                due_date:    New due date e.g. '2025-12-25'
        """
        with LocalSession() as sesion:
                todo = sesion.get(Todo, todo_id)
                if not todo:
                        return f"Todo with id {todo_id} not found"

                if title:
                        todo.title = title
                if description:
                        todo.description = description
                if status:
                        todo.status = status
                if priority:
                        todo.priority = priority
                if due_date:
                        todo.due_date = due_date

                sesion.commit()
                sesion.refresh(todo)

                return f"""
                    Todo: {todo.id} update
                    {todo.to_dict()}

                """
                
@tool
def delete_todos(todo_id:int):
        """
            Permanently delete a todo by its ID.

            Args:
                 todo_id: ID of the todo to delete (required)
        """
        with LocalSession() as sesion:
                todo = sesion.get(Todo, todo_id)
                if not todo:
                        return f"Todo with id {todo_id} not found"
                title =todo.title
                sesion.delete(todo)
                sesion.commit()

                return f"Todo #{title} delete successfully !"


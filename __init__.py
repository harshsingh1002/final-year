from flask_restful import Api

from app import flaskAppInstance
from .Task import Task
from .TaskById import TaskById


restserver = Api(flaskAppInstance)


restserver.add_resource(Task,"/api/v1.0/task")
restserver.add_resource(TaskById,"/api/v1.0/task/id/<string:taskId>")

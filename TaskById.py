from flask_restful import Resource
import logging as logger


class TaskById(Resource):

    def get(self,taskId):
        logger.debug("inside get method of task by Id")
        return {"message" : "inside get method of task by id. TASK-ID= {}".format(taskId)},200



    def post(self,taskId):
        logger.debug("inside post method of task by Id")
        return {"message": "inside post method of task by id. TASK-ID= {}".format(taskId)}, 200



    def put(self,taskId):
        logger.debug("inside put method of task by Id")
        return {"message": "inside put method of task by id. TASK-ID= {}".format(taskId)}, 200



    def delete(self,taskId):
        logger.debug("inside delete method of task by Id")
        return {"message": "inside delete method of task by id. TASK-ID= {}".format(taskId)}, 200


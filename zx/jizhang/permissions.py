__author__ = 'Administrator'

from rest_framework import permissions
from jizhang.log.logger import logger

class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    only owner can delete and edit his own object
    '''
    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        logger.info('==============IsOwnerOrReadOnly====================')
        ok = (obj.owner == request.user)
        if ok:
            logger.info('you are the owner, continue')
        else:
            logger.info( 'you are not the owner, can not edit current item')
        return ok


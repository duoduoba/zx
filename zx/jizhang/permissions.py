__author__ = 'Administrator'

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    only owner can delete and edit his own object
    '''
    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        print('==============IsOwnerOrReadOnly====================')
        ok = (obj.owner == request.user)
        if ok:
            print('you are the owner, continue')
        else:
            print( 'you are not the owner, can not edit current item')
        return ok


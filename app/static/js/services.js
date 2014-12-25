'use strict';

angular.module('angularFlaskServices', ['ngResource'])
    .factory('Post', function($resource) {
        return $resource('/api/v1/test', {}, {
            query: {
                method: 'GET',
                params: { postId: '' },
                isArray: true
            }
        });
    })
;




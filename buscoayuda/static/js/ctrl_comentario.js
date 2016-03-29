/**
 * Created by lm.ochoa750 on 19/02/2016.
 */

app.controller('ctrl_comentario', function ($scope, $http) {
    $scope.comentario = {};

    $scope.crear_comentario = function () {
        var url = window.location.href;
        var pathArray = url.split('/');
        $scope.comentario.idIndependiente = pathArray[pathArray.length-2];

        $http({
            method: 'POST',
            url: '/api/comentarios/',
            data: $scope.comentario,
            headers: {'Content-Type': 'application/json'}
        }).success(function (data, status) {
            $('#modal-comentario').modal('hide');
            window.location.href = url;
            }).error(function (data, status) {
        })
    };
});
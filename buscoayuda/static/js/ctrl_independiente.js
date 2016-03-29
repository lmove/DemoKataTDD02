/**
 * Created by lm.ochoa750 on 19/02/2016.
 */

app.controller('ctrl_independiente', function ($scope, $http) {

    var ver_comentarios = function () {
        var pathArray = window.location.href.split('/');
        var idIndependiente = pathArray[pathArray.length-2];

        $http({
            method: 'GET',
            url: '/api/independientes/' + idIndependiente + '/comentarios/'
        }).success(function (data, status) {
            $scope.comentarios = data
        }).error(function (data, status) {
        })
    };

    ver_comentarios();
});
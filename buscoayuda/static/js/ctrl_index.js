/**
 * Created by Lina8a on 22/02/2016.
 */

app.controller('ctrl_index', function ($scope, $http) {

    var listar_servicios = function() {
        $http({
            method: 'GET',
            url: '/api/servicios/'
        }).success(function (data, status) {
            $scope.servicios = data;
        }).error(function (data, status) {
        })
    }

    $scope.ver_independientes_por_filtro = function () {
        if($scope.servicio_seleccionado == -1) {
            window.location.href = '/';
        }
        else {
            window.location.href = '/' + $scope.servicio_seleccionado + '/';
        }
    };

    listar_servicios();
});
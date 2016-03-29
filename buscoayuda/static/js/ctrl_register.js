app.controller('ctrl_register', function ($scope, $http) {

    $scope.service = {};
    $scope.register = {};
    $scope.register.foto = {};
    $scope.fotoCompressed = {};

    $scope.save_register = function () {

        $scope.post_register();
    }

    $scope.get_service = function () {

        $http({method: 'GET', url: '/api/servicios/'})
            .success(function (data, status) {
                $scope.service = data;
            }).error(function (data, status) {
            $scope.service = {};
            alert(data);
        })
    };

    $scope.get_service();

    $scope.post_register = function () {
        $scope.register.foto = "http://es.fakenamegenerator.com/images/sil-male.png";
            $http({
                method: 'POST',
                url: '/api/independientes/',
                data: $scope.serialize($scope.register),
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            })
                .success(function (data, status) {
                    window.location.href = "/";
                }).error(function (data, status) {
                alert('Se presentó un error registrando la información, intente de nuevo\n\n' + data);
            })

    };

    $scope.serialize = function (obj) {
        var str = [];
        for (var p in obj) {
            if (obj.hasOwnProperty(p)) {
                str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
            }
        }
        return str.join("&");
    };

});
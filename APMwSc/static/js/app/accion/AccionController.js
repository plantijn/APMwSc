scrumModule.config(function ($routeProvider) {
    $routeProvider.when('/VAccion/:idAccion', {
                controller: 'VAccionController',
                templateUrl: 'app/accion/VAccion.html'
            }).when('/VCrearAccion/:idPila', {
                controller: 'VCrearAccionController',
                templateUrl: 'app/accion/VCrearAccion.html'
            });
});

scrumModule.controller('VAccionController', 
   ['$scope', '$location', '$route', 'flash', '$routeParams', 'accionService', 'prodService',
    function ($scope, $location, $route, flash, $routeParams, accionService, prodService) {
      $scope.msg = '';
      $scope.fAccion = {};

      accionService.VAccion({"idAccion":$routeParams.idAccion}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VProducto1 = function(idPila) {
        $location.path('/VProducto/'+idPila);
      };

      $scope.fAccionSubmitted = false;
      $scope.AModifAccion0 = function(isValid) {
        $scope.fAccionSubmitted = true;
        if (isValid) {
          
          accionService.AModifAccion($scope.fAccion).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              if (label == '/VAccion') {
                  $route.reload();
              } else {
                  $location.path(label);
              }
          });
        }
      };

    }]);
scrumModule.controller('VCrearAccionController', 
   ['$scope', '$location', '$route', 'flash', '$routeParams', 'accionService', 'prodService',
    function ($scope, $location, $route, flash, $routeParams, accionService, prodService) {
      $scope.msg = '';
      $scope.fAccion = {};

      accionService.VCrearAccion({"idPila":$routeParams.idPila}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VProducto1 = function(idPila) {
        $location.path('/VProducto/'+idPila);
      };

      $scope.fAccionSubmitted = false;
      $scope.ACrearAccion0 = function(isValid) {
        $scope.fAccionSubmitted = true;
        if (isValid) {
          
          accionService.ACrearAccion($scope.fAccion).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              if (label == '/VCrearAccion') {
                  $route.reload();
              } else {
                  $location.path(label);
              }
          });
        }
      };

    }]);

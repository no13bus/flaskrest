var PhoneListCtrl = ['$scope', '$http', function($scope, $http) {
    $http.get('static/phones/phones.json').success(function(data) {
        console.log(typeof(data));
        $scope.phones = data.data.splice(0, 5);;
    });

  // $scope.phones = [
  //   {"name": "Nexus S",
  //    "snippet": "Fast just got faster with Nexus S.",
  //    "age": 0},
  //   {"name": "Motorola XOOM™ with Wi-Fi",
  //    "snippet": "The Next, Next Generation tablet.",
  //    "age": 1},
  //   {"name": "MOTOROLA XOOM™",
  //    "snippet": "The Next, Next Generation tablet.",
  //    "age": 2}
  // ];

  $scope.orderProp = 'age';
}]
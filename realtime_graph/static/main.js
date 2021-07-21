var ctx = document.getElementById('myChart').getContext('2d');

var graphData = {
    type: 'line',
    data: {
        labels: ['1', '2', '3', '4', '5', '6'],
        datasets: [{
            label: 'REAL-Time EEG APP',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
             
            ],
      
            borderWidth: 1
        }]
    },
    options: {}
}

var myChart = new Chart(ctx, graphData);

var socket = new WebSocket('ws://localhost:8000/ws/graph/');



socket.onmessage =function(e){
    var djangoData =JSON.parse(e.data);
    console.log(djangoData);

    var newGraphData = graphData.data.datasets[0].data;
    newGraphData.shift();
    newGraphData.push(djangoData.value);

    graphData.data.datasets[0].data = newGraphData;
    myChart.update();



}
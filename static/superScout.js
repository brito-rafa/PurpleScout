var socket = io();
socket.on('connect', function() {
    socket.emit('my event', {data: 'I\'m connected!'});
});

// super scouter knows status of each scout
// socket.on('scouterReady', function(data) {
//     console.log('Scouter ' + data.name + ' is ready!');

//     let team = prompt('Scouter ' + data.name + ' is ready! What team are they scouting?'); // this will be eventually be determined automatically
//     socket.emit('scoutAssign', {name: data.name, team: team});

// });

// disable the start match button until teams are fetched
$('#startMatch').prop('disabled', true);


// Fetch teams button handler
$('button#fetchTeams').click(function() {
    console.log('fetching teams')
    socket.emit('getTeams', {matchNum: $('#matchNum').val()});
    $('#red1teamNum').text('...');
    $('#red2teamNum').text('...');
    $('#red3teamNum').text('...');
    $('#blue1teamNum').text('...');
    $('#blue2teamNum').text('...');
    $('#blue3teamNum').text('...');
});
// ... receive the teams and display them
socket.on('sendTeams', function(data) {
    console.log(data);
    $('#red1teamNum').text(data.red1);
    $('#red2teamNum').text(data.red2);
    $('#red3teamNum').text(data.red3);
    $('#blue1teamNum').text(data.blue1);
    $('#blue2teamNum').text(data.blue2);
    $('#blue3teamNum').text(data.blue3);

    // enable the start button if there is no error
    if (data.red1 != 'error') {
        $('#startMatch').prop('disabled', false);
    } else {
        $('#startMatch').prop('disabled', true);
    }
});

// receive status updates from scouts
socket.on('scoutSelect', function(data) {
    console.log(data);
    if (data.action == 'select') {
        $('#' + data.type + 'Status').text('Ready');
    } else {
        $('#' + data.type + 'Status').text('...');
    }
});

// start the match
$('button#startMatch').click(function() {
    socket.emit('scoutAssign', {
        red1: $('#red1teamNum').text(),
        red2: $('#red2teamNum').text(),
        red3: $('#red3teamNum').text(),
        blue1: $('#blue1teamNum').text(),
        blue2: $('#blue2teamNum').text(),
        blue3: $('#blue3teamNum').text()
    });
});
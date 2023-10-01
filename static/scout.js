var socket = io();

// Tell the server that this scouter is ready
//const username = prompt('Enter your name: ');
//socket.emit('scouterReady', {name: username});

const assign = document.getElementById('assign');
const waiting = document.getElementById('waiting');
const form = document.getElementById('scoutForm');

var selectedTeam = null;

assign.style.display = 'block';
waiting.style.display = 'none';
form.style.display = 'none';

// Team select handler
$('button.teamSelect').click(function() {
    //assign.style.display = 'none';
    //waiting.style.display = 'block';
    
    // emit scoutSelect event with the id of the button clicked
    if (this.id != 'deselect') {

        // deselect the current one, and select the new one
        socket.emit('scoutSelect', {type: selectedTeam, action: 'deselect'})
        socket.emit('scoutSelect', {type: this.id, action: 'select'});

        // show the waiting message
        waiting.style.display = 'block';
        $('#waiting b span').text(this.id);
        selectedTeam = this.id;

    } else {
        // hide the waiting message
        waiting.style.display = 'none';
        socket.emit('scoutSelect', {type: selectedTeam, action: 'deselect'});
    }
});

// When another scouter clicks a button, disable it
socket.on('scoutSelect', function(data) {
    console.log(data);
    if (data.action == 'select') {
        $('#' + data.type).prop('disabled', true);
    } else {
        $('#' + data.type).prop('disabled', false);
    }
});


// When the server tells us that a scouter is ready, log it
socket.on('scoutAssign', function(data) {
    console.log('Scouter ' + selectedTeam + ' is assigned to team ' + data[selectedTeam]);
    alert("The super scout has started the match! You've been assigned to team " + data[selectedTeam] + ".");
    // update ui
    $('#preMatch').hide();
    $('#scoutForm').show();

    $('#teamNumSpan').text(data[selectedTeam] + " (" + selectedTeam.toUpperCase() + ")");
    $('#teamNum').val(data[selectedTeam]);
});


$(document).ready(function () {
    console.log('cargado..')

    setInterval(
        function () {
            const d = new Date();
            const datestring = `${d.getFullYear()}-${d.getMonth() + 1}-${d.getDate()} ${d.getHours()}:${d.getMinutes()}:${d.getSeconds()}`;
            //console.log(datestring);
            $('#time').html(datestring);
        },
        1000
    );
   


})
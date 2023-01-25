(function (){
    const btnEliminacion= document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn=>{
        btn.addEventListener('click', (e) =>{
            const confirmacion = confirm('¿Estas seguro de eliminar este curso?');

            if(!confirmacion){
                e.preventDefault();
            }
        });
    });
})();
function abrirPopup(id, texto){
    document.getElementById('input-meta').value = texto;
    const form = document.getElementById('form-editar');
    form.action = '/atualizar_meta/' + id;
    document.getElementById('popup-editar').classList.add('show');
    document.getElementById('overlay').classList.add('show');
}

function fecharPopup(){
    document.getElementById('popup-editar').classList.remove('show');
    document.getElementById('overlay').classList.remove('show');
}
document.querySelectorAll('.btn-editar').forEach(btn => {
    btn.addEventListener('click', () => {
        const id = btn.dataset.id;
        const texto = btn.dataset.texto;
        abrirPopup(id, texto);
    });
});
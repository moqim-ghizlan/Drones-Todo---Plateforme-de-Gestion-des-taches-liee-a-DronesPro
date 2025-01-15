function open_close_GM_costum_modal(trigger) {
    var modal = document.getElementById(trigger.dataset.modalTargget);
    var holder = modal.parentElement;
    if (holder.classList.contains("active")) {
      holder.classList.remove("active");
      modal.classList.remove("active");
    } else {
      holder.classList.add("active");
      modal.classList.add("active");
    }
  }

function close_GM_modal_btns(btn) {
  var modal = btn.parentElement.parentElement;
  var holder = modal.parentElement;
  holder.classList.remove("active");
  modal.classList.remove("active");
}



function handleAddTodo(btn){
  const form = document.querySelector('#new-todo-form');
  const title = form.querySelector('#title');
  const description = form.querySelector('#description');
  const error = form.querySelector('.errer');
  if (!title.value){
    error.textContent = 'Please fill at least the title field';
    return;
  }else{
    error.textContent = '';
    btn.disabled = true;
    btn.innerHTML = 'In progress ...';
    form.submit();
  }
}

function handleSubmitChanges(btn) {
  const id = btn.getAttribute('id').split('-')[1];
  const form = document.querySelector(`#update-${id}-form`);
  const title = form.querySelector('.title');
  const description = form.querySelector('#description');
  if (title.value=="") {
    form.querySelector('.errer').innerHTML = 'Please fill all the fields';
    return;
  }else{
    form.querySelector('.errer').innerHTML = '';
    btn.disabled = true;
    btn.innerHTML = 'Updating ...';
    form.submit();
  }
}


function handleShowUncompletedOnly(){
  const sort = document.querySelector('#sort');
  const checkbox = sort.querySelector('#flexSwitchCheckDefault');
  const cards = document.querySelectorAll('.cards div.card');
  if (checkbox.checked) {
    cards.forEach(card => {
      if (card.getAttribute('data-completed') == 'true') {
        card.style.display = 'none';
      }
    });
  }else{
    console.log('checkbox.checked', checkbox.checked)
    cards.forEach(card => {
      card.style.display = 'flex';
    });
  }
}




function handleAddCategory(btn){
  const form = document.querySelector('#new-category-form');
  const name = form.querySelector('#category_name');
  const error = form.querySelector('.errer');
  if (!name.value){
    error.textContent = 'Please fill at least the title field';
    return;
  }else{
    error.textContent = '';
    btn.disabled = true;
    btn.innerHTML = 'In progress ...';
    form.submit();
  }
}
function handleDeleteCategory(btn){
  const form = document.querySelector('#delete-category-form');
  const name = form.querySelector('#category_id');
  const error = form.querySelector('.errer');
  if (!name.value){
    error.textContent = 'Please choose a category';
    return;
  }else{
    btn.disabled = true;
    btn.innerHTML = 'In progress ...';
    form.submit();
  }
}


